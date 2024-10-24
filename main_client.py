import sys
import os
import time
import threading

home_dir = os.path.expanduser('~')
sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))

import rospy
import numpy as np

# ----------------- ROS Message -----------------

from geometry_msgs.msg import PoseStamped, Quaternion
from sensor_msgs.msg import JointState 
from std_msgs.msg import String , Int32
from sensor_msgs.msg import LaserScan, Image
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory ,JointTrajectoryPoint

# -----------------------------------------------

from agent.agent import Agent
from agent.real_endeffector import realEE
from lib.zeus_kinematics import *
from config.config import realConfig
from utils.interpolation import inter_solve
from utils.traj_processing import dataTrajectory

openEE_WhileMoving = None


class realAgent(Agent):

    def __init__(self):

        global openEE_WhileMoving

        if len(sys.argv) > 1:
            if sys.argv[1] == 'bottle':
                openEE_WhileMoving = True
            elif sys.argv[1] == 'bartender':
                openEE_WhileMoving = False
            else:
                print("Unknown argument:", sys.argv[1])
                openEE_WhileMoving = None
        else:
            print("No Argument Error.")
            openEE_WhileMoving = None
        
        self._EEMoving = openEE_WhileMoving

        print("Open EE while Moving : ",self._EEMoving)

        Agent.__init__(self)

        self._EE  = realEE()

        self._initJoint                 = realConfig.initPoseA
        self._initTrans                 = realConfig.initPoseT
        self._jointNames                = realConfig.jointNameList
        self._curJoint                  = self._initJoint
        self._robotJoint                = []
        self._curTrans                  = self._initTrans
        self._commandJoint              = self._curJoint
        self._eeController              = realEE()
        self._jointVelocity             = realConfig.defaultAngleVelocity
        self._robotReadyState           = threading.Event()
        self._robotReadyStateLock       = threading.RLock()
        self._shakingType               = 0
    

    
        #----- Publisher
        self._realJointCommandPub          = rospy.Publisher('/zeus/real/jointCommand'             ,  JointTrajectory    , queue_size = 1    )
        self._realJointTrajCommandPub      = rospy.Publisher('/zeus/real/jointTrajectory'          ,  JointTrajectory    , queue_size = 1    )  
        self._realFSMPub                   = rospy.Publisher('/zeus/fsm'                           ,  String             , queue_size = 1    )
        self._realMotionParamPub           = rospy.Publisher('/zeus/real/param'                    ,  Int32              , queue_size = 1    )
        self._getJointPub                  = rospy.Publisher('/zeus/real/getJoint'                 ,  Int32              , queue_size = 1    )

        #----- Subscriber
        self._eeCommandSub                 = rospy.Subscriber('/zeus/real/eeCommand'               ,  String               , self._eeControlCallback         )
        self._realSimpleMoveSub            = rospy.Subscriber('/zeus/real/simpleMoveCommand'       ,  String               , self._simpleMoveCallback        )
        self._realmenuSub                  = rospy.Subscriber('/zeus/real/menu'                    ,  String               , self._menuCallback              )
        self._jointSub                     = rospy.Subscriber('/zeus/real/joint'                   ,  JointTrajectory      , self._jointUpdateCallback       )
        self._fsmHandlingSub               = rospy.Subscriber('/zeus/fsmHandling'                  ,  String               , self._fsmHandlingCallback       )

        # Check Robot is ON
        self._robotReadyState.clear()
        while (not self._robotReadyState.is_set()) :
            print("Robot OFFLINE")
            self._getJoint()
            rospy.sleep(2)

        # Temp to Skip HRI Section
        self._fsm.handleEvent("hri_start")
        self._fsm.handleEvent("get_menu")
    
        #----- Additional Threads
        threading.Thread(target=self._publishFsmState,daemon=True).start()
        # threading.Thread(target=self._printingReadyState ,daemon= True).start()
        print("Robot Start")

        # --- Run 
        rospy.spin()

# ---------------- Thread Functions ------------------

    def _publishFsmState(self) :
        while not rospy.is_shutdown():
            stateMsg = String()
            stateMsg.data = self._fsm.getState()
            self._realFSMPub.publish(stateMsg)
            self.rateFast.sleep()
    
    def _printingReadyState(self) :
        while not rospy.is_shutdown():
            if self._robotReadyState.isSet() :
                print("Robot Ready !")
            else :
                print("Robot not Ready !!!")
            rospy.sleep(0.1)

# --------------- Callback Functions -----------------


    def _fsmHandlingCallback(self, msg) :

        event = msg.data
        if event not in self.fsm.event:
            print("Wrong Event!")
        else :
            print("Handling Event {}",event)
            self._fsm.handleEvent(event)


    def _jointUpdateCallback(self,data):
        DEGREE_TO_RADIAN = 0.0174533
        joint = np.array(data.points[0].positions,dtype= np.float32).tolist()
        # print("Joint : ", " ".join(str(j) for j in joint))
        self._robotJoint = joint
        joint = [angle * DEGREE_TO_RADIAN for angle in joint]
        joint = [angle * direction for angle, direction in zip(joint, realConfig.ROTATE_DIRECTION)]
        self._curJoint = joint 
        self._curTrans = ARM6_kinematics_forward_armReal(joint)
        # print(f"Robot Ready Time    : {time.time()}")
        self._robotReadyState.set()
        self._curTrans.printTransform(self._curTrans)

    def _menuCallback(self,menu):
        menu_num = int(menu.data)
        if menu_num in (1, 2, 3):
            self._shakingType = 1
        else: 
            self._shakingType = 2

        # self._fsm.handleEvent("get_menu")
        self._makeMenu(menu)
        self._hereYouare()
        # Ordered Task End
        rospy.sleep(3)

        self._fsm.handleEvent("hri_start")
        self._fsm.handleEvent("get_menu")
        self.movePoseT(realConfig.startPoseT)

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
            
            elif command == 'r' :
                self._pour()
            elif command == 't' :
                self._unpour()
            
            elif command == '0' :
                angle = [0,0,0,0,0,0]
                self.movePoseA(angle)
            elif command == '1' :
                self.movePoseT(realConfig.startPoseT)
            elif command == '2' :
                self.movePoseT(realConfig.barPoseT)
            elif command == '3' :
                self.movePoseT(realConfig.shakingT)
            elif command == '4' :
                self.movePoseT(realConfig.servicePositionT)


            elif command == '5' :
                self.movePoseT(realConfig.bfPosition1)
                self._openEE()
                rospy.sleep(1)
                moveBig =0.18
                self._moveZ(-moveBig)
                print("Moving Z Devide : ",realConfig.bfMovingDown + moveBig)
                self._moveZDevide(realConfig.bfMovingDown + moveBig)
                rospy.sleep(1)
                self._closeEE()
                rospy.sleep(1)
                self.movePoseT(realConfig.bfPosition1)
                rospy.sleep(0.1)
                self.movePoseA(realConfig.bfPosition2A)
                rospy.sleep(1)
                self.movePoseA(realConfig.bfPosition3A)
                rospy.sleep(1)
                self._motionFast()
                rospy.sleep(8.0)
                self.movePoseA(realConfig.bfPosition4A)
                rospy.sleep(0.3905)
                self._openEE()  
                self._moitionSlow()

            elif command == '7' :
                self._shakingTraj(2)
    
            # ---   Motion Param
            elif command == 'o' :
                self._moitionSlow()
            elif command == 'p' :
                self._motionFast()    

            # elif command == 'v' :
            #     joint = self._robotJoint
            #     joint[4] += 5
            #     traj_msg = JointTrajectory()
            #     traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
            #     traj_point = JointTrajectoryPoint()
            #     traj_point.positions = joint
            #     traj_point.time_from_start = rospy.Duration(1.0)
            #     traj_msg.points.append(traj_point)
            #     self._realJointCommandPub.publish(traj_msg)

            # elif command == 'b' :
            #     joint = self._robotJoint
            #     joint[5] += 5
            #     traj_msg = JointTrajectory()
            #     traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
            #     traj_point = JointTrajectoryPoint()
            #     traj_point.positions = joint
            #     traj_point.time_from_start = rospy.Duration(1.0)
            #     traj_msg.points.append(traj_point)
            #     self._realJointCommandPub.publish(traj_msg)

            # elif command == 'n' :
            #     joint = self._robotJoint
            #     joint[2] -= 5
            #     traj_msg = JointTrajectory()
            #     traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
            #     traj_point = JointTrajectoryPoint()
            #     traj_point.positions = joint
            #     traj_point.time_from_start = rospy.Duration(1.0)
            #     traj_msg.points.append(traj_point)
            #     self._realJointCommandPub.publish(traj_msg)
    

            # elif command == 'f' :
            #     joint = self._robotJoint
            #     joint[4] -= 5
            #     traj_msg = JointTrajectory()
            #     traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
            #     traj_point = JointTrajectoryPoint()
            #     traj_point.positions = joint
            #     traj_point.time_from_start = rospy.Duration(1.0)
            #     traj_msg.points.append(traj_point)
            #     self._realJointCommandPub.publish(traj_msg)

            # elif command == 'g' :
            #     joint = self._robotJoint
            #     joint[5] -= 5
            #     traj_msg = JointTrajectory()
            #     traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
            #     traj_point = JointTrajectoryPoint()
            #     traj_point.positions = joint
            #     traj_point.time_from_start = rospy.Duration(1.0)
            #     traj_msg.points.append(traj_point)
            #     self._realJointCommandPub.publish(traj_msg)

            # elif command == 'h' :
            #     joint = self._robotJoint
            #     joint[2] += 5
            #     traj_msg = JointTrajectory()
            #     traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
            #     traj_point = JointTrajectoryPoint()
            #     traj_point.positions = joint
            #     traj_point.time_from_start = rospy.Duration(1.0)
            #     traj_msg.points.append(traj_point)
            #     self._realJointCommandPub.publish(traj_msg)

            
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

    def _makeMenu(self,msg):
        print("Making Menu!!!")
        menu = msg.data
        self.movePoseT(realConfig.barPoseT)
        self.rateNormal.sleep()
        print("Arrived at the dispensor")

        if self._EE.getState() != 'open':
            print("EE is closed")
            self._EE.open()
            
        self.rateNormal.sleep()
        
        if not self._fsm.getState() == 'moving':
            print("Current State is not Moving Quit!!!")
            return
        else :
            first_comp = realConfig.menuComponent[menu][0]        
            second_comp = realConfig.menuComponent[menu][1]
            movingYtemp = 0.2
            print(f"Component : {first_comp} {second_comp}")

            # Moving sequence should be (y) - (x) - (z) - (z) | (-z) - (x) - (z) - (z) - (-z) - (-x) - (-y)
            print("Get First")
            self._moveX(realConfig.componentOffset[first_comp][0])
            self.rateNormal.sleep()
            self._moveY(realConfig.componentOffset[first_comp][1])
            self.rateNormal.sleep()
            self._moveZ(realConfig.componentOffset[first_comp][2])
            self.rateNormal.sleep()
            self._moveZ(realConfig.componentOffset[first_comp][3])
            time.sleep(8)
            # Second Element
            self._moveZ(-(realConfig.componentOffset[first_comp][2] + realConfig.componentOffset[first_comp][3]))
            self.rateNormal.sleep()
            print("moving Down")

            self._moveY(-movingYtemp)
            self.rateNormal.sleep()
            print("Get Second") 
            self._moveX(realConfig.componentOffset[second_comp][0] - realConfig.componentOffset[first_comp ][0])
            self.rateNormal.sleep()
            self._moveY(movingYtemp)
            self._moveZ(realConfig.componentOffset[second_comp][2])
            self.rateNormal.sleep()
            self._moveZ(realConfig.componentOffset[second_comp][3])
            time.sleep(8)
            self._moveZ(-(realConfig.componentOffset[second_comp][2] + realConfig.componentOffset[second_comp][3] ))
            self.rateNormal.sleep()
            print("moving Down")
            self._moveY(-movingYtemp)
            self.rateNormal.sleep() 
            self._moveX(-realConfig.componentOffset[second_comp][0])
            self.rateNormal.sleep()
            self._moveY(-realConfig.componentOffset[second_comp][1] + movingYtemp )
            self.rateNormal.sleep() 
            print("Success to get base bevarge\n")

            self.rateNormal.sleep()
            self._EE.close()

            if self._EE.getState() != 'closed':
                print("EE is opened")
                self._EE.close()
            rospy.sleep(3)
            
            self.movePoseT(realConfig.shakingT)
            print("Arrvied at the Shaking Position")
            self._motionFast()
            if self._shakingType not in (1, 2):
                print("Wrong Shaking Type")
            else:
                print("Shaking Type : ",self._shakingType)
                self._shake(self._shakingType)
            self._moitionSlow()
            self.movePoseT(realConfig.shakingT)
            rospy.sleep(3)

            print("Making Menu Done\n")

    def _shake(self,shakingType):
        self._robotReadyState.wait()
        self._fsm.handleEvent('shake')
        

        if not self._fsm.getState() == 'shaking':
            print("Current State is not Shaking Quit!!!")
        else :

            # Shaking Implementation Required :
            self._shakingTraj(shakingType)
            # --------------------------------

            self._fsm.handleEvent('finish_shake')
            print("Shaking Done\n")
        

    def _pour(self):
        self._robotReadyState.wait()
        self._robotReadyState.clear()
        joint = self._robotJoint
        joint[5] -= 120
        traj_msg = JointTrajectory()
        traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        traj_point = JointTrajectoryPoint()
        traj_point.positions = joint
        traj_point.time_from_start = rospy.Duration(1.0)
        traj_msg.points.append(traj_point)
        self._realJointCommandPub.publish(traj_msg)
    
    def _unpour(self):
        self._robotReadyState.wait()
        self._robotReadyState.clear()
        joint = self._robotJoint
        joint[5] += 120
        traj_msg = JointTrajectory()
        traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        traj_point = JointTrajectoryPoint()
        traj_point.positions = joint
        traj_point.time_from_start = rospy.Duration(1.0)
        traj_msg.points.append(traj_point)
        self._realJointCommandPub.publish(traj_msg)


    def _hereYouare(self):
        if not self._fsm.getState() == 'moving':
            print("Current State is not Moving Quit!!!")
            return
        else :   
            self.movePoseT(realConfig.servicePositionT)
            sentence = 'Enjoy your drink'
            print(sentence)
            self._EE.open()
            rospy.sleep(2)
            self._pour()
            rospy.sleep(5)
            self._unpour()
            rospy.sleep(1)
            self.movePoseT(realConfig.shakingT)
            self._fsm.handleEvent('serve_menu')


# --------------- Base Action ------------------------

    def movePoseA(self, Angle):
        self._robotReadyState.wait()
        self._robotReadyState.clear()
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
        traj_point.positions = Angle
        traj_point.time_from_start = rospy.Duration(1.0)
        traj_msg.points.append(traj_point)
        self._realJointCommandPub.publish(traj_msg)
            
    def movePoseT(self,Transform):
        self._robotReadyState.wait()
        solvedAngle = ARM6_kinematics_inverse_arm(Transform,self._curJoint)
        self.movePoseA(solvedAngle)

    def _moveXDevide(self, xDistance):
        self._robotReadyState.wait()
        step_size = 0.15
        threshold = 0.3
        if abs(xDistance) >= threshold :
            num_steps = int(abs(xDistance) // step_size)
            remainder = abs(xDistance) % step_size
            sign = 1 if xDistance > 0 else -1
            for _ in range(num_steps):
                self._moveX(sign * step_size)
            if remainder > 0:
                self._moveX(sign * remainder)
        else:
            self._moveX(xDistance)

    def _moveZDevide(self, zDistance):
        self._robotReadyState.wait()
        step_size = 0.01
        threshold = 0.03
        if abs(zDistance) >= threshold :
            num_steps = int(abs(zDistance) // step_size)
            remainder = abs(zDistance) % step_size
            sign = 1 if zDistance > 0 else -1
            for _ in range(num_steps):
                self._moveZ(sign * step_size)
            if remainder > 0:
                self._moveZ(sign * remainder)
        else:
            self._moveZ(zDistance)        

    def _moveX(self,xDistance) :
        print(f"Move Rel Start Time : {time.time()}")
        self._robotReadyState.wait()
        goalTrans = self._curTrans
        goalTrans = goalTrans.setVal(0,3,self._curTrans(0,3) + xDistance)
        self.movePoseT(goalTrans)

    def _moveY(self,yDistance) :
        print(f"Move Rel Start Time : {time.time()}")
        self._robotReadyState.wait()
        goalTrans = self._curTrans
        goalTrans = goalTrans.setVal(1,3,self._curTrans(1,3) + yDistance)
        self.movePoseT(goalTrans)

    def _moveZ(self,zDistance) :
        print(f"Move Rel Start Time : {time.time()}")
        self._robotReadyState.wait()
        goalTrans = self._curTrans
        goalTrans = goalTrans.setVal(2,3,self._curTrans(2,3) + zDistance)
        self.movePoseT(goalTrans)

    def _interMove(self, trans1, trans2):
        print(f"Inter Move Start Time : {time.time()}")
        self._robotReadyState.wait()
        num_step = 16
        result = inter_solve(trans1, trans2, num_step)  

        RADIAN_TO_DEGREE = 57.2958
        traj_msg = JointTrajectory()
        traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']

        for angles in result:
            Angle = [angle * RADIAN_TO_DEGREE for angle in angles]
            Angle = [angle * direction for angle, direction in zip(Angle, realConfig.ROTATE_DIRECTION)]

            traj_point = JointTrajectoryPoint()
            traj_point.positions = Angle
            traj_point.time_from_start = rospy.Duration(1.0)
            traj_msg.points.append(traj_point)
        
        print("Trajectory Num : ", len(traj_msg.points))

        self._realJointTrajCommandPub.publish(traj_msg)

    def _shakingTraj(self, type) :
        print(f"Shaking Start Time : {time.time()}")
        self._robotReadyState.wait()
        self._robotReadyState.clear()
        shakeTrajec = None
        if type == 1 :
            shakeTrajec = dataTrajectory(realConfig.shakeType1)
        elif type == 2:
            shakeTrajec = dataTrajectory(realConfig.shakeType2)
        self._realJointTrajCommandPub.publish(shakeTrajec)

    def _rotateX(self,xAngle)  :
        print(f"Move Rel Start Time : {time.time()}")
        self._robotReadyState.wait()
        goalTrans = self._curTrans
        goalTrans = goalTrans.rotateX(xAngle)
        self.movePoseT(goalTrans)

    def _rotateY(self,yAngle)  :
        print(f"Move Rel Start Time : {time.time()}")
        self._robotReadyState.wait()
        goalTrans = self._curTrans
        goalTrans = goalTrans.rotateY(yAngle)
        self.movePoseT(goalTrans)

    def _rotateZ(self,zAngle)  :
        print(f"Move Rel Start Time : {time.time()}")
        self._robotReadyState.wait()
        goalTrans = self._curTrans
        goalTrans = goalTrans.rotateZ(zAngle)
        self.movePoseT(goalTrans)

    def _openEE(self) :
        if self._EEMoving == True : # For BottleFlip
            self._eeController.open()
        elif self._EEMoving == False : # For Bartender
            self._robotReadyState.wait()
            # self._robotReadyState.clear()
            self._eeController.open()  

    def _closeEE(self) :
        self._robotReadyState.wait()
        # self._robotReadyState.clear()
        self._eeController.close()
    
    def _moitionSlow(self) :
        self._robotReadyState.wait()
        self._robotReadyState.clear()
        motion_msg = Int32()
        motion_msg.data = 0
        self._realMotionParamPub.publish(motion_msg)

    def _motionFast(self) :
        self._robotReadyState.wait()
        self._robotReadyState.clear()
        motion_msg = Int32()
        motion_msg.data = 1
        self._realMotionParamPub.publish(motion_msg)

    def _getJoint(self) :
        getJoint_msg = Int32()
        getJoint_msg.data =1
        self._getJointPub.publish(getJoint_msg)


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
