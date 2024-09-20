#!/usr/bin/env python
import socket
import rospy
import sys
import signal
import time
import numpy as np
import struct

from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint   
from std_msgs.msg import Int32

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.50',5003)) #ip and port
server_socket.listen(0) #wait for the client to connect
print('Robot connected!!!')

client_socket, addr = server_socket.accept() #create socket for data
client_socket.settimeout(1)


def is_socket_closed(sock):
    try:
        sock.recv(1,socket.MSG_PEEK)
        return False
    except sock.error:
        return True

def signal_handler(signal,frame):
    global server_socket, client_socket
    print("Exiting!")
    rospy.signal_shutdown("break")
    
    while not is_socket_closed(server_socket):
        try:
            server_socket.close()
            print(" Try to close the Server socket")
        except Exception as e:
            print(f"Failed to close the Server socket : {e}")
            time.sleep(0.1)
        client_socket.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

rospy.init_node('zeuscontrol')
pub_ready       = rospy.Publisher('/zeus/real/move_ready',Int32, queue_size=1)
zeus_joint_read = rospy.Publisher('/zeus/real/joint', JointTrajectory, queue_size = 1)


start_time = time.time()
def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def trajectory_callback(data):
    global start_time
    cur_time=time.time()
    if cur_time-start_time<1.0:
        print( "EARLY MESSAGE...IGNORED!!!")
    else:
        print("Joint trajectory message!")
        
        np_arr=np.array(data.points[0].positions, dtype=np.float32)
        print(np_arr)

        msg=struct.pack("f",0)+np_arr.tostring()
        print(len(msg))
        b_msg=struct.unpack("fffffff",msg)
        print(b_msg)
        try:
            client_socket.send(msg) #send data to client
        except Exception as e:
            print(e)

def relmove_callback(data):
    global start_time
    cur_time=time.time()
    if cur_time-start_time<1.0:print( "EARLY MESSAGE...IGNORED!!!")
    else:
        print("Relative movement message!")
        np_arr=np.array(data.points[0].positions, dtype=np.float32)
        print(np_arr)        
        msg=struct.pack("f",1)+np_arr.tostring()
        print(len(msg))
        b_msg=struct.unpack("fffffff",msg)
        print(b_msg)
        try:
            client_socket.send(msg) #send data to client
        except Exception as e:
            print(e)

def multimove_callback(data):
    global start_time
    cur_time=time.time()
    if cur_time-start_time<1.0:print ("EARLY MESSAGE...IGNORED!!!")
    else:
        traj_num=len(data.points)
        print("Multiple movement message!",traj_num )
        msg=struct.pack("f",2)
        for i in range(traj_num):
            msg=msg+np.array(data.points[i].positions, dtype=np.float32).tostring()
        print("Data size:",len(msg))
        try:
            client_socket.send(msg) #send data to client
        except Exception as e:
            print(e)

def gripper_callback(data):
    global start_time
    cur_time=time.time()
    if cur_time-start_time<1.0:print ("EARLY MESSAGE...IGNORED!!!")
    else:
        datavar=data.data
        if datavar==0:
            print("Gripper open")
            msg=struct.pack("f",3)
        elif datavar==1:
            print("Gripper close")
            msg=struct.pack("f",4)
        elif datavar==2:
            print("Gripper clear")
            msg=struct.pack("f",5)
        elif datavar==3:
            print("Motion param 1")
            msg=struct.pack("f",6)
        try:
            client_socket.send(msg) #send data to client
        except Exception as e:
            print(e)


rospy.Subscriber("/zeus/real/jointCommand", JointTrajectory,trajectory_callback)
rospy.Subscriber("/zeus/real/fingerPositionCommand", JointTrajectory,relmove_callback)
rospy.Subscriber("/zeus/real/jointTrajectory", JointTrajectory,multimove_callback)
rospy.Subscriber("/mapcmd", Int32,gripper_callback)

debug_time=time.time()
while True:
    time.sleep(0.02)
    try:
        data = client_socket.recv(65535) #receive data from client
        print (data,len(data))
        if len(data)==0:
            print("Connection Lost!!")
            rospy.signal_shutdown("break")
            server_socket.close()
            client_socket.close()
            sys.exit(0)
        else:
            header = struct.unpack("f",data[0:4])
            maindata = data[4:len(data)]
            if header[0] == 9: #Ready msg
                ready_msg=Int32()
                pub_ready.publish(ready_msg)
            elif header[0] == 8: # joint msg
                msg = struct.unpack("f",maindata)
                traj_msg = JointTrajectory()
                traj_msg.header.stamp = rospy.Time.now()
                traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
                traj_point = JointTrajectoryPoint()
                traj_point.positions = msg
                traj_point.time_from_start = rospy.Duration(1.0)
                traj_msg.points.append(traj_point)
                zeus_joint_read.publish(traj_msg)
                
    except socket.timeout as e:
        err=e.args[0]
        if err=='timed out':
            cur_time=time.time()
            if cur_time-debug_time>5:
                debug_time=cur_time
                print('Timeout!')
            continue
        else:
            print(e)
