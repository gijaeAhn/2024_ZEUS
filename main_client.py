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
        self._eeCommandSub                 = rospy.Subscriber('/zeus/real/eeCommand'               ,  String               , self._eeControlCallback         )
        self._realSimpleMoveSub            = rospy.Subscriber('/zeus/real/simpleMoveCommand'       ,  String               , self._simpleMoveCallback        )
        self._realmenuSub                  = rospy.Subscriber('/zeus/real/menu'                    ,  String               , self._menuCallback              )
        self._jointSub                     = rospy.Subscriber('/zeus/real/joint'                   ,  JointTrajectory      , self._jointUpdateCallback       )

        #----- Additional Threads
        threading.Thread(target=self._publishFsmState,daemon=True).start()

        # Temp to Skip HRI Section
        self._fsm.handleEvent("hri_start")
        self._fsm.handleEvent("get_menu")

        # --- Run 
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
        
        # ---- Below is just for Debugging
        #self._curTrans.printTransform(self._curTrans)
    
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

            # --- For Dispenser Test    
            elif command == 'g' :
                self._moveY(realConfig.componentOffset['A'][1])
            elif command == 'h' :
                self._moveZ(realConfig.componentOffset['A'][2])
            elif command == 'j' :
                self._moveZ(realConfig.componentOffset['A'][3])
            elif command == 'k' :
                self._moveZ(-(realConfig.componentOffset['A'][2] + realConfig.componentOffset['A'][3]))
            # ----------------------

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
        print("Arrived at the dispensor")
        self.rateNormal.sleep()

        # Check EE is opened
        if self._EE.getState != 'open':
            print("EE is closed")
            self._EE.open()
            return
        self.rateNormal.sleep()

        if not self._fsm.getState() == 'moving':
            print("Current State is not Moving Quit!!!")
            return
        else :        
            # Moving sequence should be (x) - (y) - (z) - (z) | (-z) - (x) - (z) - (z) - (-z) - (-y)
            self._moveX(realConfig.componentOffset[realConfig.menuComponent[menu][0]][0])                
            self._moveY(realConfig.componentOffset[realConfig.menuComponent[menu][0]][1])
            self._moveZ(realConfig.componentOffset[realConfig.menuComponent[menu][0]][2])
            self._moveZ(realConfig.componentOffset[realConfig.menuComponent[menu][0]][3])
            self.rateSlow.sleep()
            # Second Element
            self._moveZ(-( realConfig.componentOffset[realConfig.menuComponent[menu][0]][2] +
                          realConfig.componentOffset[realConfig.menuComponent[menu][0]][3] ))  
            self.rateNormal.sleep()
            self._moveX(realConfig.componentOffset[realConfig.menuComponent[menu][1]][0] -
                        realConfig.componentOffset[realConfig.menuComponent[menu][0]][0])
            self._moveZ(realConfig.componentOffset[realConfig.menuComponent[menu][1]][2])
            self._moveZ(realConfig.componentOffset[realConfig.menuComponent[menu][1]][3])
            self.rateSlow.sleep()
            self._moveZ(-( realConfig.componentOffset[realConfig.menuComponent[menu][1]][2] +
                           realConfig.componentOffset[realConfig.menuComponent[menu][1]][3] ))
            self.rateNormal.sleep()
            self._moveY(-realConfig.componentOffset[realConfig.menuComponent[menu][1]][1])   # << Insert here if third or more elements is needed
            self.rateNormal.sleep()
            print("Success to get base bevarge\n")
            # Now We get the componenets

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
            self.movePoseT(realConfig.shakingT)
            print("Making Menu Done\n")


    def _shake(self):
        self._fsm.handleEvent('shake')

        if not self._fsm.getState() == 'shaking':
            print("Current State is not Shaking Quit!!!")
        else :

            # Shaking Implementation Required :



            # --------------------------------

            self._fsm.handleEvent('finish_shake')
            print("Shaking Done\n")

    def _pour(self):
        self._rotateZ(realConfig.pourAngle) 
        self.rateSlow.sleep()

    def _hereYouare(self):
        if not self._fsm.getState() == 'moving':
            print("Current State is not Moving Quit!!!")
            return
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

    # ----------- Above Actions are Fully tested ----    


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
    rospy.init_node('realNode',anonymous=True)
    zeusAgent = realAgent()


if __name__ == '__main__':
    main()
