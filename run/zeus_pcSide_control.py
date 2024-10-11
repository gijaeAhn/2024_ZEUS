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
server_socket_5003 = None  # For sending data to robot (port 5003)
client_socket_5003 = None
server_socket_5004 = None  # For receiving data from robot (port 5004)
client_socket_5004 = None
start_time = None

def signal_handler(signal, frame):
    global server_socket_5003, client_socket_5003, server_socket_5004, client_socket_5004
    print("Exiting!")
    rospy.signal_shutdown("break")
    
    # Close sockets on port 5003
    try:
        client_socket_5003.close()
        server_socket_5003.close()
        print("Closed sockets on port 5003")
    except Exception as e:
        print(f"Failed to close sockets on port 5003: {e}")

    # Close sockets on port 5004
    try:
        client_socket_5004.close()
        server_socket_5004.close()
        print("Closed sockets on port 5004")
    except Exception as e:
        print(f"Failed to close sockets on port 5004: {e}")

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    global server_socket_5003, client_socket_5003, server_socket_5004, client_socket_5004, start_time
    start_time = time.time()
    
    rospy.init_node('zeuscontrol')
    pub_ready = rospy.Publisher('/zeus/real/move_ready', Int32, queue_size=1)
    zeus_joint_read = rospy.Publisher('/zeus/real/joint', JointTrajectory, queue_size=1)

    # Server socket for port 5003 (sending commands to robot)
    server_socket_5003 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_5003.bind(('192.168.0.71', 5003))  # Bind to all interfaces
    server_socket_5003.listen(1)  # Wait for the robot to connect
    print('Waiting for connection on port 5003 (command socket)...')
    client_socket_5003, addr = server_socket_5003.accept()  # Accept connection from robot
    client_socket_5003.settimeout(1)
    print('Robot connected on port 5003:', addr)

    # Server socket for port 5004 (receiving joint data from robot)
    server_socket_5004 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_5004.bind(('192.168.0.71', 5004))  # Bind to all interfaces
    server_socket_5004.listen(1)  # Wait for the robot to connect
    print('Waiting for connection on port 5004 (data socket)...')
    client_socket_5004, addr_5004 = server_socket_5004.accept()  # Accept connection from robot
    client_socket_5004.settimeout(1)
    print('Robot connected on port 5004:', addr_5004)


    def returnJoint_callback(data):
        # Data is useless 
        global start_time
        cur_time = time.time()
        print("Received JointCommand message from PC")
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            print("Retunning joint positions ")
            msg = struct.pack("f", 5) 
            # print("Sending message of length:", len(msg))
            try:
                client_socket_5003.sendall(msg)  # Send data to robot via port 5003
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
            print("Sending joint positions:", np_arr)
            msg = struct.pack("f", 0) + np_arr.tobytes()
            # print("Sending message of length:", len(msg))
            try:
                client_socket_5003.sendall(msg)  # Send data to robot via port 5003
            except Exception as e:
                print("Error sending data to robot:", e)

    def trajectory_callback(data):
        global start_time
        cur_time = time.time()
        print("Received Trajectory message from PC")
        pointNum = 100
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else :
            np_arr = np.array([val for i in range(pointNum) for val in data.points[i].position], dtype=np.float32)
            msg = struct.pack("f",1) + np_arr.tobytes()
            print(f"Sending message of length : {len(msg)}")
            try:
                client_socket_5003.sendall(msg)  # Send data to robot via port 5003
            except Exception as e:
                print("Error sending data to robot:", e)

    def motionParam_callback(msg):
        global start_time
        cur_time = time.time()
        print("Recieved Motion Param message from PC")
        if cur_time - start_time < 1.0 :
            print("EARLY MESSAGE...IGNORED!!!")
        else :
            paramType = msg.data
            if paramType == 0 :   # Slow Motion Param
                msg = struct.pack("f",3.0)
                print(f"Sending message of length : {len(msg)}")
            elif paramType == 1 : # Fast Motion Param
                msg = struct.pack("f",4.0)
                print(f"Sending message of length : {len(msg)}")
            try :
                client_socket_5003.sendall(msg)
            except Exception as e :
                print("Error sending data to robot:", e)

    @DeprecationWarning
    def relmove_callback(data):
        global start_time
        cur_time = time.time()
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            print("Relative movement message!")
            np_arr = np.array(data.points[0].positions, dtype=np.float32)
            print("Sending relative move positions:", np_arr)
            msg = struct.pack("f", 2) + np_arr.tobytes()
            print("Sending message of length:", len(msg))
            try:
                client_socket_5003.sendall(msg)  # Send data to robot via port 5003
            except Exception as e:
                print("Error sending data to robot:", e)

    @DeprecationWarning
    def gripper_callback(data):
        global start_time
        cur_time = time.time()
        if cur_time - start_time < 1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            datavar = data.data
            if datavar == 0:
                print("Gripper open")
                msg = struct.pack("f", 3)
            elif datavar == 1:
                print("Gripper close")
                msg = struct.pack("f", 4)
            elif datavar == 2:
                print("Gripper clear")
                msg = struct.pack("f", 5)
            elif datavar == 3:
                print("Motion param 1")
                msg = struct.pack("f", 6)
            else:
                print("Unknown gripper command:", datavar)
                return
            try:
                client_socket_5003.sendall(msg)  # Send data to robot via port 5003
            except Exception as e:
                print("Error sending data to robot:", e)

    # Subscribe to ROS topics
    rospy.Subscriber("/zeus/real/jointCommand"   , JointTrajectory, jointCommand_callback )
    rospy.Subscriber("/zeus/real/jointTrajectory", JointTrajectory, trajectory_callback   )
    rospy.Subscriber("/zeus/real/param"          , Int32          , motionParam_callback  )
    rospy.Subscriber("/zeus/real/getJoint"       , Int32          , returnJoint_callback  )



    debug_time = time.time()
    while not rospy.is_shutdown():
        time.sleep(0.02)
        # Handle data from robot (port 5004)
        try:
            data_5004 = client_socket_5004.recv(65535)  # Receive data from robot via port 5004
            if len(data_5004) == 0:
                print("Connection Lost on port 5004!!")
                rospy.signal_shutdown("break")
                client_socket_5004.close()
                server_socket_5004.close()
                sys.exit(0)
            else:
                # Process data from robot
                header = struct.unpack('f', data_5004[0:4])[0]
                if header == 8:  # Joint positions
                    if len(data_5004) != 4 + 4*6:
                        print("Incorrect data size for joint positions")
                        continue
                    floats = struct.unpack('6f', data_5004[4:])
                    traj_msg = JointTrajectory()
                    traj_msg.header.stamp = rospy.Time.now()
                    traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
                    traj_point = JointTrajectoryPoint()
                    traj_point.positions = floats
                    traj_point.time_from_start = rospy.Duration(0.0)
                    traj_msg.points.append(traj_point)
                    zeus_joint_read.publish(traj_msg)
                elif header == 9:  # Ready message
                    print("Received ready message from robot")
                    ready_msg = Int32()
                    ready_msg.data = 1
                    pub_ready.publish(ready_msg)
                else:
                    print("Unknown header received on port 5004:", header)
        except socket.timeout:
            pass  # Expected due to timeout setting
        except Exception as e:
            print("Exception on client_socket_5004:", e)

        # No need to handle data from port 5003 in the main loop since it's used for sending commands
        # If you expect to receive acknowledgments or other messages from the robot on port 5003, you can add handling here

if __name__ == '__main__':
    main()

