#!/usr/bin/env python

import socket
import struct
import signal
import sys
import time
from i611_MCS import *
from teachdata import *
from i611_extend import *
from rbsys import *
from i611_common import *
from i611_io import *
from i611shm import *

# Global variables for sockets
recv_socket = None
send_socket = None
rb = None

def signal_handler(signal, frame):
    global recv_socket, send_socket
    global rb
    rb.close()
    recv_socket.close()
    send_socket.close()
    print("EXIT!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    global recv_socket, send_socket
    global rb
    rb = i611Robot()
    _BASE = Base()
    rb.open()
    IOinit(rb)
    data = Teachdata("teach_data")

    m = MotionParam(jnt_speed=25, pose_speed=30, overlap=3)
    rb.motionparam(m)
    override1 = 70
    override2 = 30


    recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recv_socket.connect(('192.168.0.71', 5003)) 
    recv_socket.settimeout(1)

    time.sleep(0.1)

    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.connect(('192.168.0.71', 5004))  # Replace with Control PC's IP
    send_socket.settimeout(1)

    count = 0
    debug_time = time.time()
    
    curPos = rb.getjnt().jnt2list()
    print("Current joint positions:", curPos)
    msg = struct.pack("f", 8) + struct.pack("6f", *curPos)
    try:
    	send_socket.sendall(msg)
    except Exception as e:
    	print(e)

    while True:
        count += 1
        try:
            data = recv_socket.recv(65535)
            if len(data) == 0:
                print("Connection Lost on port 5003!!")
                recv_socket.close()
                send_socket.close()
                rb.close()
                sys.exit(0)
            header = struct.unpack("f", data[0:4])[0]
            maindata = data[4:]
            print("Received command with header:", header)
            # Process data
            if header == 0:  # Joint command
                if len(maindata) != 4*6:
                    print("Incorrect data size for joint command")
		        else :
                    msg = struct.unpack("6f", maindata)
                    print("Joint command:", msg)
                    j1 = Joint(msg[0], msg[1], msg[2], msg[3], msg[4], msg[5])
                    rb.move(j1)
	 	            rb.join()

            elif header == 1:  # Joint Trajectory command
                pointNum = 100
                if len(maindata) != 4 * 6 * pointNum:
                    print("Incorrect data size for relative move command")
                    continue
                msg = struct.unpack("600f", maindata)
                print("Joint Trajectory command ")
                for i in range(0, len(msg), 6):
                    j = Joint(msg[0+i], msg[1+i], msg[2+i], msg[3+i], msg[4+i], msg[5+i])
                    rb.move(j)
                rb.join()
                response = struct.pack("f", 9) + struct.pack("f", 1)
                send_socket.sendall(response)        

            elif header == 2:  # Relative move command
                print("Deprecated : Rel Move")
                if len(maindata) != 4*6:
                    print("Incorrect data size for relative move command")
                    continue
                msg = struct.unpack("6f", maindata)
                print("Relative move command:", msg)
                rb.relline(dx=msg[0]*1000, dy=msg[1]*1000, dz=msg[2]*1000)  # in millimeters
                response = struct.pack("f", 9) + struct.pack("f", 1)
                send_socket.sendall(response)

            elif header == 3:
                print("Motion param Override! : ",override1)
                rb.override(override1)
            
            elif header == 4:
                print("Motion param Override! : ",override2)
                rb.override(override2)

            elif header == 5:
                print("Just Retunning Joint Position")   

            curPos = rb.getjnt().jnt2list()
            print("Current joint positions:", curPos)
            msg = struct.pack("f", 8) + struct.pack("6f", *curPos)
            response = struct.pack("f", 9) + struct.pack("f", 1)
            try:
                send_socket.sendall(msg)
		        time.sleep(0.1)
                send_socket.sendall(response)
            except Exception as e:
                print(e)

        except socket.timeout:
            pass 
        except Exception as e:
            print("Exception in receiving data:", e)

        rb.sleep(0.1)

    rb.close()

if __name__ == '__main__':
    main()

