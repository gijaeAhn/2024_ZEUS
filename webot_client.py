import sys

sys.path.append('/home/sj/Desktop/2024_zeus/')


from agent.agent import Agent
from agent.webots_endeffector import webotsEE

# ----------------- ROS Message -----------------

from geometry_msgs.msg import PoseStamped, Quaternion
from sensor_msgs.msg import JointState 
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan, Image
from std_msgs.msg import Header
# -----------------------------------------------

from cv_bridge import CvBridge

from lib.zeus_kinematics import *


from config.config import WebotsConfig


import tf
import rospy


class WebotsAgent(Agent) :

    def __init__(self) :

        self._initJoint = WebotsConfig.initPoseA
        self._initTrans = WebotsConfig.initPoseT

        self._jointNames = WebotsConfig.jointNameList

        self._curJoint = self._initJoint
        self._curTrans = self._initTrans
        self._commandJoint = self._curJoint
        self._eeController = webotsEE()


        self._jointVelocity = WebotsConfig.defaultAngleVelocity
        

        self._webotsJointCommandPub        = rospy.Publisher('/zeus/webots/jointCommand'           ,  JointState    , queue_size = 10             )  



        self._paramPoseSub                 = rospy.Subscriber('/zeus/webots/paramPose'             ,  String              , self._paramPoseCallback         )
        self._eeCommandSub                 = rospy.Subscriber('/zeus/webots/eeCommand'             ,  String              , self._eeControlCallback         )
        self._webotsJointCommandSub        = rospy.Subscriber('/zeus/webots/prejointCommand'       ,  JointState          , self._preJointCommandCallback   )
        self._webotsRealJointSub           = rospy.Subscriber('/zeus/webots/realJoint'             ,  JointState          , self._updateJointCallback       )
        self._webotsSimpleMoveSub          = rospy.Subscriber('/zeus/webots/simpleMoveCommand'     ,  String              , self._simpleMoveCallback        )
        self._webotsPositionMoveSub        = rospy.Subscriber('/zeus/webots/positionCommnad'       ,  String              , self._paramPoseCallback         )

        rospy.spin()

        

# ---------------- Callback Functions ----------------



    def _preJointCommandCallback(self,jointState):
        msg = JointState(jointState)
        self._webotsJointCommandPub.publish(msg)


    def _updateJointCallback(self, jointState):
        print("Updating Joint :", end=' ')
        tempPosition = [0] * 6  # Corrected list initialization for 6 elements
        for index, (name, position) in enumerate(zip(jointState.name, jointState.position)):
            if index < 6:  # Ensure we do not exceed the tempPosition list size
                tempPosition[index] = position
                print(f"{{{position:.2f}}}", end=' ')  # Print each joint position
            else:
                break  # Break out of the loop if more joints than expected

        self._curTrans = ARM6_forward_kinematics(tempPosition)  # Assuming this function is defined elsewhere
        self._curJoint = tempPosition
        print() 


    def _simpleMoveCallback(self,msg, scale = 'small') :
        
        command = msg.data
        print(command)

        

        if scale == 'small':
            if command == 'w' :
                print('Debug simpleMove w\n')
                self._moveX(WebotsConfig.smallCommandStep)
            elif command == 's' :
                self._moveX( -WebotsConfig.smallCommandStep)
            elif command == 'a' :
                self._moveY(WebotsConfig.smallCommandStep)
            elif command == 'd' :
                self._moveY(-WebotsConfig.smallCommandStep)
            elif command == 'q' :
                self._moveZ(WebotsConfig.smallCommandStep)
            elif command == 'e' :
                self._moveZ(WebotsConfig.smallCommandStep)
        elif scale == 'big' :
            if command == 'w' :
                self._moveX(WebotsConfig.bigCommandStep)
            elif command == 's' :
                self._moveX( -WebotsConfig.bigCommandStep)
            elif command == 'a' :
                self._moveY(WebotsConfig.bigCommandStep)
            elif command == 'd' :
                self._moveY(-WebotsConfig.bigCommandStep)
            elif command == 'q' :
                self._moveZ(WebotsConfig.bigCommandStep)
            elif command == 'e' :
                self._moveZ(WebotsConfig.bigCommandStep)


    def _eeControlCallback(self,command):

        if command == 'open' :
            self._openEE()
        elif command == 'close':
            self._closeEE()
        else :
            print("Wrong EE Command")
        

    def _paramPoseCallback(self,command):
        
        if command   == '1' :
            self.movePoseT(WebotsConfig.pose1T)
        elif command == '2' :
            self.movePoseT(WebotsConfig.pose2T)
        elif command == '3' :
            self.movePoseT(WebotsConfig.pose3T)
        elif command == '4' :
            self.movePoseT(WebotsConfig.pose4T)
        elif command == '5' :
            self.movePoseT(WebotsConfig.pose5T)

    

# ---------------- Webots Action ---------------------

    def movePoseA(self, Angle):
        print('Debug movePoseA\n')
        msg = JointState()
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()
        for i in range(WebotsConfig.DOF):
            msg.name.append(self._jointNames[i])
        msg.position = Angle
        #
        msg.velocity = self._jointVelocity
        msg.effort = []

        self._webotsJointCommandPub.publish(msg)

        

    def movePoseT(self,Transform):
        solvedAngle = ARM6_kinematics_inverse_arm(Transform,self._curJoint)
        self.movePoseA(solvedAngle)

        # Translate and Rotatae will gonnna modify the stored data
        # So another method should be needed

    def _moveX(self,xDistance) :
        goalTrans = self._curTrans.translateX(xDistance)
        self.movePoseT(goalTrans)

    def _moveY(self,yDistance) :
        goalTrans = self._curTrans.translateY(yDistance)
        self.movePoseT(goalTrans)

    def _moveZ(self,zDistance) :
        goalTrans = self._curTrans.translateZ(zDistance)
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
    wbAgent = WebotsAgent()


if __name__ == '__main__':
    main()







            