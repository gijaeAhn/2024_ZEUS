#!/usr/bin/env python
import socket
import rospy
import sys
import signal
import time
import numpy as np
import struct


from trajectory_msgs.msg import JointTrajectory
from std_msgs.msg import Int32





# ----- For EXIT -------
def signal_handler(signal,frame):
    global server_socket, client_socket
    print("EXIT!")
    rospy.signal_shutdown("break")
    server_socket.close()
    client_socket.clos

start_time = time.time()

class zeusController:
    def __init__(self):

        
        # ----------- Server Socket Setting ----------
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('192.168.0.20',5003))
        self.server_socket.listen(0)
        print('ZEUS SERVER CONNECTED')

        self.client_socket , self.client_addr = self.server_socket.accept()
        self.client_socket.settimeout(1)

        # --------------------------------------------

        self.pub_ready = rospy.Publisher('/move_ready', Int32, queue_size=1)
    
    
    def trajectory_callback(self,data):
        global start_time
        cur_time=time.time()

        if cur_time-start_time<1.0:
            print("EARLY MESSAGE...IGNORED!!!")
        else:
            print("Joint trajectory message!")
            np_arr=np.array(data.points[0].positions, dtype=np.float32)*180.0/np.pi
            print(np_arr)
            msg=struct.pack("f",0)+np_arr.tostring()
            print(len(msg))
            b_msg=struct.unpack("fffffff",msg)
            print(b_msg)
            try:
                self.client_socket.send(msg) #send data to client
            except Exception as e:
                print(e)
            
        





