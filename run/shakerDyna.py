#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import dynamixel_sdk as dxl

class DynamixelControlNode:
    def __init__(self):

        rospy.init_node('dynamixel_control_node', anonymous=True)

        self.DEVICENAME = rospy.get_param('~devicename', '/dev/ttyUSB0')
        self.BAUDRATE = rospy.get_param('~baudrate', 4000000)
        self.DXL_ID = rospy.get_param('~dynamixel_id', 1)
        self.PROTOCOL_VERSION = 2.0

        # Control Table ADDR
        self.ADDR_OP_MODE           = 11  
        self.ADDR_TORQUE_ENABLE     = 64
        self.ADDR_OPERATING_MODE    = 11
        self.ADDR_GOAL_POSITION     = 116
        self.ADDR_GOAL_CURRENT      = 102
        self.ADDR_PRESENT_POSITION  = 132

        # Data Byte Length
        self.LEN_GOAL_POSITION = 4
        self.LEN_GOAL_CURRENT = 2

        # Operating Modes
        self.OP_MODE_TORQUE = 0    # Current Control Mode
        self.OP_MODE_POSITION = 3  # Position Control Mode

        self.TORQUE_ENABLE = 1
        self.TORQUE_DISABLE = 0

        self.portHandler = dxl.PortHandler(self.DEVICENAME)
        self.packetHandler = dxl.PacketHandler(self.PROTOCOL_VERSION)

        if self.portHandler.openPort():
            rospy.loginfo("Succeeded to open the port")
        else:
            rospy.logerr("Failed to open the port")
            quit()

        if self.portHandler.setBaudRate(self.BAUDRATE):
            rospy.loginfo("Succeeded to change the baudrate")
        else:
            rospy.logerr("Failed to change the baudrate")
            quit()

        self.write1ByteTxRx(self.ADDR_TORQUE_ENABLE, self.TORQUE_ENABLE)


        # ------------ Requires Initial encoder Reading -------------

        result = self.read4ByteTxRx(self.ADDR_PRESENT_POSITION)
        if result is not None:
            self.initial_position = result
            rospy.loginfo("Inital Encoder Position : %d", self.initial_position)
        else:
            rospy.logerr("Reading Encoder Failure.")
            self.initial_position = 0 

        self.initial_position = 2550 

        # -----------------------------------------------------------
        rospy.Subscriber('/zeus/real/gripperCommand', String, self.control_mode_callback)

        rospy.loginfo("Dynamixel control node started")

    def control_mode_callback(self, msg):
        mode_str = msg.data.strip()
        if mode_str == 'n':
            # DIRECTION_CORRECTION_VAL = -1
            # DEGREE_PER_UNIT = 360.0 / 4096
            # units_per_degree = 1 / DEGREE_PER_UNIT
            # units_for_90_degrees =  DIRECTION_CORRECTION_VAL * int(units_per_degree * 90)
            goal_position = self.initial_position 
            # goal_position = (goal_position + 4096) % 4096

            self.set_operating_mode(self.OP_MODE_POSITION)
            rospy.loginfo("Switched to Position Control Mode")
            self.write4ByteTxRx(self.ADDR_GOAL_POSITION, goal_position)

        elif mode_str == 'm':
            DIRECTION_CORRECTION_VAL = -1
            
            DEGREE_PER_UNIT = 360.0 / 4096
            DEGREE = 88
            units_per_degree = 1 / DEGREE_PER_UNIT
            units_for_degrees =  DIRECTION_CORRECTION_VAL * int(units_per_degree * DEGREE)
            goal_position = (self.initial_position + units_for_degrees) % 4096
            self.set_operating_mode(self.OP_MODE_POSITION)
            rospy.loginfo("Switched to Position Control Mode")
            self.write4ByteTxRx(self.ADDR_GOAL_POSITION, goal_position)
            rospy.sleep(0.5)
            self.set_operating_mode(self.OP_MODE_TORQUE)
            rospy.loginfo("Switched to Torque Control Mode")
            goal_current = 200 * DIRECTION_CORRECTION_VAL  
            self.write2ByteTxRx(self.ADDR_GOAL_CURRENT, goal_current)

        else:
            rospy.logwarn("Received unknown mode: '%s'", mode_str)

    def set_operating_mode(self, mode):
        self.write1ByteTxRx(self.ADDR_TORQUE_ENABLE, self.TORQUE_DISABLE)
        self.write1ByteTxRx(self.ADDR_OPERATING_MODE, mode)
        self.write1ByteTxRx(self.ADDR_TORQUE_ENABLE, self.TORQUE_ENABLE)

    def write1ByteTxRx(self, address, value):
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(
            self.portHandler, self.DXL_ID, address, value)
        if dxl_comm_result != dxl.COMM_SUCCESS:
            rospy.logerr("Write1ByteTxRx failed: %s", self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            rospy.logerr("Write1ByteTxRx error: %s", self.packetHandler.getRxPacketError(dxl_error))

    def write2ByteTxRx(self, address, value):
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(
            self.portHandler, self.DXL_ID, address, value)
        if dxl_comm_result != dxl.COMM_SUCCESS:
            rospy.logerr("Write2ByteTxRx failed: %s", self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            rospy.logerr("Write2ByteTxRx error: %s", self.packetHandler.getRxPacketError(dxl_error))

    def write4ByteTxRx(self, address, value):
        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(
            self.portHandler, self.DXL_ID, address, value)
        if dxl_comm_result != dxl.COMM_SUCCESS:
            rospy.logerr("Write4ByteTxRx failed: %s", self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            rospy.logerr("Write4ByteTxRx error: %s", self.packetHandler.getRxPacketError(dxl_error))
    
    def read4ByteTxRx(self, address):
        result, dxl_comm_result, dxl_error = self.packetHandler.read4ByteTxRx(self.portHandler, self.DXL_ID, address)
        if dxl_comm_result != dxl.COMM_SUCCESS:
            rospy.logerr("Read4ByteTxRx failed: %s", self.packetHandler.getTxRxResult(dxl_comm_result))
            return None
        elif dxl_error != 0:
            rospy.logerr("Read4ByteTxRx error: %s", self.packetHandler.getRxPacketError(dxl_error))
            return None
        else:
            return result

    def close_port(self):
        self.write1ByteTxRx(self.ADDR_TORQUE_ENABLE, self.TORQUE_DISABLE)
        self.portHandler.closePort()

if __name__ == '__main__':
    try:
        node = DynamixelControlNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        node.close_port()
