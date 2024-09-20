#!/usr/bin/env python

from i611_MCS import *
from teachdata import *
from i611_extend import *
from rbsys import *
from i611_common import *
from i611_io import *
from i611shm import *
import socket
import struct
import signal,sys,time

rb = i611Robot()

def signal_handler(signal,frame):
    global server_socket, client_socket
    global rb
    rb.close()
    print("EXIT!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)



def main():
    _BASE = Base()
    rb.open()
    IOinit( rb )
    data = Teachdata( "teach_data" )
    m = MotionParam( jnt_speed = 40 , pose_speed=30, overlap = 3 ) 
    rb.motionparam( m )


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1)
    sock.connect(('192.168.0.50',5003))
    sock.settimeout(1)

    Socket_data = 'start'
    Socket_data = Socket_data.encode()
    sock.send(Socket_data)
    count=0
    debug_time=time.time()

    curPos = rb.getpos().pos2list()

    if len(curPos) != 6:
    	print(f"curPos has {len(curPos)} elements, expected 6. Adjusting the list.")
    	curPos = (curPos + [0] * 6)[:6]  # Extend or truncate to make it exactly 6 elements

    msg = struct.pack("f",8)+ struct.pack("6f",*curPos)	   
    try:
	sock.send(msg)
    except Exception as e:
	print(e)

    while True:
        count=count+1
        try:
	    curPos = rb.getpos().pos2list()
	    print("CUR POSE : {} {} {} {} {} {}".format(curPos[0],curPos[1], curPos[2],curPos[3],curPos[4],curPos[5]))		
            data = sock.recv(65535)
            header=struct.unpack("f",data[0:4])
            maindata=data[4:len(data)]
            print("Data size:",len(data),len(maindata))
            if header[0]==0: #joint command
                msg=struct.unpack("ffffff",maindata)
                print("Joint", msg)
                j1 = Joint( msg[0],msg[1],msg[2],msg[3],msg[4],msg[5])
                rb.move(j1)
		msg = struct.pack("f",9) + struct.pack("f",1)
                sock.send(msg)

            elif header[0]==1: #rel move command
                msg=struct.unpack("ffffff",maindata)
                print("LINEAR",msg)
		print("msg 0,1,2 : {}, {}, {}".format(msg[0]*1000,msg[1]*1000,msg[2]* 1000))

                rb.relline(dx = msg[0] * 1000, dy= msg[1] * 1000, dz = msg[2]*1000 ) #in milimeters

		msg = struct.pack("f",9) + struct.pack("f",1)
		sock.send(msg)
            elif header[0]==2:
                traj_num=len(maindata)/12
                print("Total traj:",traj_num)

                j1=rb.getjnt() #Get current joint
                p1=rb.Joint2Position(j1)
                points=[] #POINT LIST
                for i in range(traj_num):
                    pos=struct.unpack("fff", maindata[i*12:(i+1)*12] )
                    print(i,pos)
                    p2=p1.offset(pos[0],pos[1],pos[2])#in milimeters
                    points.append(p2)

                rb.asyncm(1) #Nonstop movement start
                rb.line(*points)
                rb.join() #Wait for the movement end
                rb.asyncm(2) #Nonstop movement end
		msg = struct.pack("f",9) + struct.pack("f",2)
		sock.send(msg)

            elif header[0]==3:
                print("Gripper open!")
                dout(50, '1')   # open gripper
            elif header[0]==4:
                print("Gripper close!")
                dout(48, '1')   # close gripper
            elif header[0]==5:
                print("Gripper clear!")
                dout(48,'000')  # Reset register
            elif header[0]==6:
                print("Motion param!")
                # msg=struct.unpack("f",maindata)
                # m = MotionParam( jnt_speed=25, lin_speed=msg[0], pose_speed=30, overlap = 3 )
                # rb.motionparam( m )
	    curPos = rb.getpos().pos2list()
	    print("CUR POSE : {} {} {} {} {} {}".format(curPos[0],curPos[1], curPos[2],curPos[3],curPos[4],curPos[5]))
	    if len(curPos) != 6:
    		print(f"curPos has {len(curPos)} elements, expected 6. Adjusting the list.")
    		curPos = (curPos + [0] * 6)[:6]  # Extend or truncate to make it exactly 6 elements	
	    msg = struct.pack("f",8)+ struct.pack("6f",*curPos)	   
            try:
		sock.send(msg)
	    except Exception as e:
		print(e)
        except socket.timeout, e:
            err=e.args[0]
            if err=='timed out':
                cur_time=time.time()
                if cur_time-debug_time>5:
                    debug_time=cur_time
                    print'Timeout!'
                continue
            else:
                print e

        rb.sleep(0.02)
    rb.close()
if __name__ == '__main__':
    main()
