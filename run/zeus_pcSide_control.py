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

# Global variables for sockets
server_socket_5003 = None  
client_socket_5003 = None
server_socket_5004 = None  
client_socket_5004 = None
start_time = None

angle_modification_enabled = None

def signal_handler(signal, frame):
    global server_socket_5003, client_socket_5003, server_socket_5004, client_socket_5004
    print("Exiting!")
    rospy.signal_shutdown("break")
    
    try:
        client_socket_5003.close()
        server_socket_5003.close()
        print("Closed sockets on port 5003")
    except Exception as e:
        print(f"Failed to close sockets on port 5003: {e}")

    try:
        client_socket_5004.close()
        server_socket_5004.close()
        print("Closed sockets on port 5004")
    except Exception as e:
        print(f"Failed to close sockets on port 5004: {e}")

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    global server_socket_5003, client_socket_5003, server_socket_5004, client_socket_5004, start_time, angle_modification_enabled
    start_time = time.time()

    if len(sys.argv) > 2:
        if sys.argv[1] == 'bottle':
            angle_modification_enabled = False
        elif sys.argv[1] == 'bartender':
            angle_modification_enabled = True
        else:
            print("Unknown argument:", sys.argv[1])
            angle_modification_enabled = None

        address = sys.argv[2]
        print("Server Address :",address)
    else:
        print("Need 2 Arguments.")
        print("Mode : 'bottle' or 'bartender'i")
        print("Server IP address")
        sys.exit()

    rospy.init_node('zeuscontrol')
    pub_ready = rospy.Publisher('/zeus/real/move_ready', Int32, queue_size=1)
    zeus_joint_read = rospy.Publisher('/zeus/real/joint', JointTrajectory, queue_size=1)

    server_socket_5003 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_5003.bind((address, 5003))  
    server_socket_5003.listen(1) 
    print('Waiting for connection on port 5003 (command socket)...')
    client_socket_5003, addr = server_socket_5003.accept() 
    client_socket_5003.settimeout(1)
    print('Robot connected on port 5003:', addr)

    server_socket_5004 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_5004.bind((address, 5004)) 
    server_socket_5004.listen(1) 
    print('Waiting for connection on port 5004 (data socket)...')
    client_socket_5004, addr_5004 = server_socket_5004.accept() 
    client_socket_5004.settimeout(1)
    print('Robot connected on port 5004:', addr_5004)


    def returnJoint_callback(data):
        global start_time
        cur_time = time.time()
        print("Received getJoint message from PC")
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            print("Returning joint positions")
            data_payload = struct.pack("f", 5)
            msg =  data_payload
            try:
                client_socket_5003.sendall(msg)
            except Exception as e:
                print("Error sending data to robot:", e)
    

    def jointCommand_callback(data):
        global start_time
        cur_time = time.time()
        print("Received JointCommand message from PC")
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            np_arr = np.array(data.points[0].positions, dtype=np.float32)
            if angle_modification_enabled == True :
                if np_arr[5] < 0:  
                    np_arr[5] += 360.0 
                if np_arr[3] < 0:
                    np_arr[3] += 360.0  
            print("Sending joint positions:", np_arr)
            data_payload = struct.pack("f", 0) + np_arr.tobytes()
            msg = data_payload
            print("Sending message of length:", len(msg))
            try:
                client_socket_5003.sendall(msg)
            except Exception as e:
                print("Error sending data to robot:", e)

    def linearCommand_callback(data):
        global start_time
        cur_time = time.time()
        print("Received JointCommand message from PC")
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            np_arr = np.array(data.points[0].positions, dtype=np.float32)
            if angle_modification_enabled == True :
                if np_arr[5] < 0:  
                    np_arr[5] += 360.0 
                if np_arr[3] < 0:
                    np_arr[3] += 360.0  
            print("Sending joint positions:", np_arr)
            data_payload = struct.pack("f", 1) + np_arr.tobytes()
            msg = data_payload
            print("Sending message of length:", len(msg))
            try:
                client_socket_5003.sendall(msg)
            except Exception as e:
                print("Error sending data to robot:", e) 


    def trajectory_callback(data):
        global start_time
        cur_time = time.time()
        print("Received Trajectory message from PC")
        pointNum = len(data.points)
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            np_arr = np.array([val for point in data.points for val in point.positions], dtype=np.float32)
            np_arr[5::6] = np.where(np_arr[5::6] < 0, np_arr[5::6] + 360.0, np_arr[5::6])

            data_payload = struct.pack("f", 2) + np_arr.tobytes()
            msg = data_payload
            print(f"Sending message of length: {len(msg)} bytes")
            for i in range(pointNum):
                if i % 1 == 0:
                    print(f"Step {i}: Joint positions = {data.points[i].positions}")
            try:
                client_socket_5003.sendall(msg)
            except Exception as e:
                print("Error sending data to robot:", e)




    def motionParam_callback(msg):
        global start_time
        cur_time = time.time()
        print("Received Motion Param message from PC")
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            paramType = msg.data
            if paramType == 0:   # Slow Motion Param
                data_payload = struct.pack("f", 3.0)
                print("Sending slow motion parameter")
            elif paramType == 1: # Fast Motion Param
                data_payload = struct.pack("f", 4.0)
                print("Sending fast motion parameter")
            else:
                print("Unknown motion parameter type:", paramType)
                return  
            msg = data_payload
            
            print(f"Sending message of length: {len(msg)} bytes")
            try:
                client_socket_5003.sendall(msg)
            except Exception as e:
                print("Error sending data to robot:", e)

    # Subscribe to ROS topics
    rospy.Subscriber("/zeus/real/jointCommand"   , JointTrajectory, jointCommand_callback )
    rospy.Subscriber("/zeus/real/linearCommand"  , JointTrajectory, linearCommand_callback)
    rospy.Subscriber("/zeus/real/jointTrajectory", JointTrajectory, trajectory_callback   )
    rospy.Subscriber("/zeus/real/param"          , Int32          , motionParam_callback  )
    rospy.Subscriber("/zeus/real/getJoint"       , Int32          , returnJoint_callback  )



    debug_time = time.time()
    while not rospy.is_shutdown():
        try:
            data_5004 = client_socket_5004.recv(65535)  
            if len(data_5004) == 0:
                print("Connection Lost on port 5004!!")
                rospy.signal_shutdown("break")
                client_socket_5004.close()
                server_socket_5004.close()
                sys.exit(0)
            else:
                header = struct.unpack('f', data_5004[0:4])[0]
                if header == 8:  # Joint positions
                    if len(data_5004) != 4 + 4*6:
                        print("Incorrect data size for joint positions")
                        continue
                    print("Recived Joint message from Robot")
                    floats = struct.unpack('6f', data_5004[4:])
                    traj_msg = JointTrajectory()
                    traj_msg.header.stamp = rospy.Time.now()
                    traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
                    traj_point = JointTrajectoryPoint()
                    traj_point.positions = floats
                    traj_point.time_from_start = rospy.Duration(0.0)
                    traj_msg.points.append(traj_point)
                    zeus_joint_read.publish(traj_msg)
                else:
                    print("Unknown header received on port 5004:", header)
        except socket.timeout:
            pass  
        except Exception as e:
            print("Exception on client_socket_5004:", e)

        time.sleep(0.01)


if __name__ == '__main__':
    main()

