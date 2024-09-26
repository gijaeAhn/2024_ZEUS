import sys
import os
import threading

home_dir = os.path.expanduser('~')

sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))


from agent.agent import Agent
from agent.real_endeffector import realEE

import rospy
import numpy as np

# ----------------- ROS Message -----------------

from geometry_msgs.msg import PoseStamped, Quaternion
from sensor_msgs.msg import JointState 
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan, Image
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory ,JointTrajectoryPoint
# -----------------------------------------------

from lib.zeus_kinematics import *

from config.config import realConfig






class realAgent(Agent):

    def __init__(self):

        Agent.__init__(self)

        self._initJoint = realConfig.initPoseA
        self._initTrans = realConfig.initPoseT
        self._jointNames = realConfig.jointNameList
        self._curJoint = self._initJoint
        self._curTrans = self._initTrans
        self._commandJoint = self._curJoint
        self._eeController = realEE()
        self._jointVelocity = realConfig.defaultAngleVelocity

    
        #----- Publisher
        self._realJointCommandPub          = rospy.Publisher('/zeus/real/jointCommand'             ,  JointTrajectory    , queue_size = 1             )  
        self._realFSMPub                   = rospy.Publisher('/zeus/fsm'                           ,  String             , queue_size = 1             )
        #----- Subscriber
        self._eeCommandSub                 = rospy.Subscriber('/zeus/real/eeCommand'             ,  String              , self._eeControlCallback         )
        # self._reaJointCommandSub           = rospy.Subscriber('/zeus/real/prejointCommand'       ,  JointState          , self._preJointCommandCallback   )
        self._realSimpleMoveSub            = rospy.Subscriber('/zeus/real/simpleMoveCommand'     ,  String              , self._simpleMoveCallback        )
        self._realmenuSub                  = rospy.Subscriber('/zeus/real/menu'                  ,  String              , self._menuCallback              )
        self._jointSub                     = rospy.Subscriber('/zeus/real/joint'                 ,  JointTrajectory      , self._jointUpdateCallback       )

        #----- Additional Threads

        threading.Thread(target=self._publishFsmState,daemon=True).start()

        #Temp
        self._fsm.handleEvent("hri_start")
        self._fsm.handleEvent("get_menu")

        rospy.spin()


# ---------------- Thread Functions ------------------

    def _publishFsmState(self) :
        while not rospy.is_shutdown():
            stateMsg = String()
            stateMsg.data = self._fsm.getState()
            self._realFSMPub.publish(stateMsg)
            self.rateFast.sleep()


# --------------- Callback Functions -----------------

    def _menuCallback(self,menu):
        self._fsm.handleEvent("get_menu")
        self._makeMenu(menu)
        self._fsm.handleEvent("serve_menu")
        self._hereYouare()
        
    def _jointUpdateCallback(self,data):
        DEGREE_TO_RADIAN = 0.0174533
        joint = np.array(data.points[0].positions,dtype= np.float32).tolist()
        joint = [angle * DEGREE_TO_RADIAN for angle in joint]
        joint = [angle * direction for angle, direction in zip(joint, realConfig.ROTATE_DIRECTION)]
        self._curJoint = joint 
        self._curTrans = ARM6_kinematics_forward_armReal(joint)
        self._curTrans.printTransform(self._curTrans)
    
    def _simpleMoveCallback(self,msg, scale = 'small') :
    
        command = msg.data        
        if scale == 'small':
            if command == 'w' :
                print('Debug simpleMove w\n')
                self._moveX(realConfig.smallCommandStep)
            elif command == 's' :
                self._moveX( -realConfig.smallCommandStep)
            elif command == 'a' :
                self._moveY(realConfig.smallCommandStep)
            elif command == 'd' :
                self._moveY(-realConfig.smallCommandStep)
            elif command == 'q' :
                self._moveZ(realConfig.smallCommandStep)
            elif command == 'e' :
                self._moveZ(-realConfig.smallCommandStep)
            elif command == 'i' :
                self.movePoseT(realConfig.startPoseT)
            elif command == 'o' :
                self.movePoseT(realConfig.barPoseT)
            elif command == '0' :
                angle = [0,0,0,0,0,0]
                self.movePoseA(angle)

            elif command == 'g' :
                self._moveY(realConfig.menuOffset['A'][0])
            elif command == 'h' :
                self._moveZ(realConfig.menuOffset['A'][2])
            elif command == 'j' :
                self._moveZ(realConfig.menuOffset['A'][3])
            elif command == 'k' :
                self._moveZ(-(realConfig.menuOffset['A'][2] + realConfig.menuOffset['A'][3]))





        elif scale == 'big' :
            if command == 'w' :
                self._moveX(realConfig.bigCommandStep)
            elif command == 's' :
                self._moveX( -realConfig.bigCommandStep)
            elif command == 'a' :
                self._moveY(realConfig.bigCommandStep)
            elif command == 'd' :
                self._moveY(-realConfig.bigCommandStep)
            elif command == 'q' :
                self._moveZ(realConfig.bigCommandStep)
            elif command == 'e' :
                self._moveZ(-realConfig.bigCommandStep)
            elif command == 'i' :
                self.movePoseT(realConfig.startPoseT)
            elif command == 'o' :
                self.movePoseT(realConfig.barPoseT)
            elif command == '0' :
                angle = [0,0,0,0,0,0]
                self.movePoseA(angle)

    def _eeControlCallback(self,command) :
        
        if command == 'open' :
            self._openEE()
        elif command == 'close':
            self._closeEE()
        else :
            print("Wrong EE Command")
        

# ---------------- Real Action ---------------------

    def _makeMenu(self,menu):

        self.movePoseA(realConfig.pose2A)
        self.rateSlow.sleep()

        print("Arrived at the dispensor")
        self.rateNormal.sleep()

        #Check the EE is opened
        if self._EE.getState != 'open':
            print("EE is closed")
            self._EE.open()
        self.rateNormal.sleep()

        if not self._fsm.getState() == 'moving':
            print("Current State is not Moving Quit!!!")
        else :        
            if menu == realConfig.menuList[0]:
                # Key characters should be replaced with actual menu name
                # Moving sequence should be y - x - z || z - x - y 
                self._moveY(realConfig.menuOffset['A'][1])
                self._moveX(realConfig.menuOffset['A'][0])
                self._moveZ(realConfig.menuOffset['A'][2])
                self.rateNormal.sleep()
                # Move backward
                self._moveZ(-realConfig.menuOffset['A'][2])
                self._moveX(-realConfig.menuOffset['A'][0])
                self._moveY(-realConfig.menuOffset['A'][1])
            elif menu == realConfig.menuList[1]:
                self._moveY(realConfig.menuOffset['B'][1])
                self._moveX(realConfig.menuOffset['B'][0])
                self._moveZ(realConfig.menuOffset['B'][2])
                self.rateSlow.sleep()
                self._moveZ(-realConfig.menuOffset['B'][2])
                self._moveX(-realConfig.menuOffset['B'][0])
                self._moveY(-realConfig.menuOffset['B'][1])
            elif menu == realConfig.menuList[2]:
                self._moveY(realConfig.menuOffset['C'][1])
                self._moveX(realConfig.menuOffset['C'][0])
                self._moveZ(realConfig.menuOffset['C'][2])
                self.rateSlow.sleep()
                self._moveZ(-realConfig.menuOffset['C'][2])
                self._moveX(-realConfig.menuOffset['C'][0])
                self._moveY(-realConfig.menuOffset['C'][1])
            elif menu == realConfig.menuList[3]:
                self._moveY(realConfig.menuOffset['D'][1])
                self._moveX(realConfig.menuOffset['D'][0])
                self._moveZ(realConfig.menuOffset['D'][2])
                self.rateSlow.sleep()
                self._moveZ(-realConfig.menuOffset['D'][2])
                self._moveX(-realConfig.menuOffset['D'][0])
                self._moveY(-realConfig.menuOffset['D'][1])
            elif menu == realConfig.menuList[4]:
                self._moveY(realConfig.menuOffset['E'][1])
                self._moveX(realConfig.menuOffset['E'][0])
                self._moveZ(realConfig.menuOffset['E'][2])
                self.rateSlow.sleep()
                self._moveZ(-realConfig.menuOffset['E'][2])
                self._moveX(-realConfig.menuOffset['E'][0])
                self._moveY(-realConfig.menuOffset['E'][1])
            self.rateNormal.sleep()

            print("Success to get base bevarge\n")

            self._EE.close()
            self.rateNormal.sleep()
            self.movePoseT(realConfig.shakingT)
            self.rateNormal.sleep()
            print("Arrvied at the Shaking Position")

            if self._EE.getState != 'closed':
                print("EE is opened")
                return

            self._shake()
            self.rateNormal.sleep()
            print("Shaking Done\n")


    def _shake(self):
        self._fsm.handleEvent('shake')

        if not self._fsm.getState() == 'shaking':
            print("Current State is not Shaking Quit!!!")
        else :

            # Shaking Implementation Required :



            # --------------------------------

            self._fsm.handleEvent('finish_shake')

    def _pour(self):
        self._rotateZ(realConfig.pourAngle) 
        self.rateSlow.sleep()
        self.rateNormal.sleep()

    def _hereYouare(self):
        if not self._fsm.getState() == 'moving':
            print("Current State is not Moving Quit!!!")
        else :   
            self.movePoseT(realConfig.servicePositionT)
            sentence = 'Here you are'
            self._speak(sentence)
            self._EE.open()
            self.rateFast.sleep()

            self._pour()
            self._fsm.handleEvent('serve_menu')


# --------------- Base Action ------------------------
    def movePoseA(self, Angle):

        if not(self._fsm.getState() == "moving" or self._fsm.getState() == "shaking"):
            print('State is not Moiving : Quit!!!')
            return 

        if len(Angle) != realConfig.DOF:
            rospy.logerr("Incorrect number of angles provided. Expected {}, got {}.".format(realConfig.DOF, len(Angle)))
            return
        RADIAN_TO_DEGREE = 57.2958
        Angle = [angle * RADIAN_TO_DEGREE for angle in Angle]
        Angle = [angle * direction for angle, direction in zip(Angle, realConfig.ROTATE_DIRECTION)]
        traj_msg = JointTrajectory()
        traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        traj_point = JointTrajectoryPoint()
        print(Angle)
        traj_point.positions = Angle
        traj_point.time_from_start = rospy.Duration(1.0)
        traj_msg.points.append(traj_point)
        print(traj_msg.points[0].positions)
        self._realJointCommandPub.publish(traj_msg)

    def movePoseT(self,Transform):
        solvedAngle = ARM6_kinematics_inverse_arm(Transform,self._curJoint)
        self.movePoseA(solvedAngle)

    def _moveX(self,xDistance) :
        goalTrans = self._curTrans

        goalTrans = goalTrans.setVal(0,3,self._curTrans(0,3) + xDistance)
        self.movePoseT(goalTrans)

    def _moveY(self,yDistance) :
        goalTrans = self._curTrans

        goalTrans = goalTrans.setVal(1,3,self._curTrans(1,3) + yDistance)
        self.movePoseT(goalTrans)

    def _moveZ(self,zDistance) :
        goalTrans = self._curTrans
        goalTrans = goalTrans.setVal(2,3,self._curTrans(2,3) + zDistance)
        self.movePoseT(goalTrans)
    
    def _rotateX(self,xAngle)  :
        goalTrans = self._curTrans.rotateX(xAngle)
        self.movePoseT(goalTrans)

    def _rotateY(self,yAngle)  :
        goalTrans = self._curTrans.rotateY(yAngle)
        self.movePoseT(goalTrans)

    def _rotateZ(self,zAngle)  :
        goalTrans = self._curTrans.rotateZ(zAngle)
        self.movePoseT(goalTrans)

    def _openEE(self) :
        self._eeController.open()

    def _closeEE(self) :
        self._eeController.close()


# -------------- For Debug ------------------------------

    def printTrans(self) :
        print(self._curTrans)

    def printAngle(self) :
        print(self._curJoint)

# --------------- Main ---------------------------------

def main():
        
    rospy.init_node('webotsNode',anonymous=True)
    wbAgent = realAgent()





if __name__ == '__main__':
    main()
