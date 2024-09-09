from agent.agent import Agent
from agent.webots_endeffector import webotsEE

# ----------------- ROS Message -----------------

from geometry_msgs import PoseStamped, Quaternion
from sensor_msgs.msg import JointState 
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan, Image
from std_msgs.msg import Header
# -----------------------------------------------

from cv_bridge import CvBridge

import lib.zeus_kinematics_module


from config.config import WebotsConfig


import tf
import rospy


class WebotsAgent(Agent) :

    def __init__(self) :

        self._initJoint = WebotsConfig.initPoseA
        self._initTrans = WebotsConfig.initPoseT

        self._curJoint = self._initJoint
        self._commandJoint = self._curJoint
        self._eeController = webotsEE()


        self._jointVelocity = WebotsConfig.defaultAngleVelocity
        

        self._webotsJointCommandPub        = rospy.Publisher('/zeus/webots/jointCommand'        , JointState    , queue_size = 10             )  
        
        self._eeCommandSub                 = rospy.Subscriber('/zeus/webots/eeCommand'          , String        , self._eeControlCallback     )
        self._paramPoseSub                 = rospy.Subscriber('/zeus/webots/paramPose'          , String        , self.__paramPoseCallback  )
        self._webotsJointStateSub          = rospy.Subscriber('/zeus/webots/jointState'         , JointState    , self._updateJointCallback   )
        self._webotsSimpleMoveSub          = rospy.Subscriber('/zeus/webots/simpleMoveCommand'  , String        , self._simpleMoveCallback    )
        self._webotsPositionMoveSub        = rospy.Subscriber('/zeus/webots/positionCommnad'    ,  String       , self._paramPoseCallback     )


        

# ---------------- Callback Functions ----------------

    def _updateJointCallback(self,jointState) :

        print("Updating Joint :", end=' ')
        for index, (name, position) in enumerate(zip(jointState.name, jointState.position)):
            self._curJoint[index] = position
            print(f"{{{position:.2f}}}", end=' ')  # Adjust the format as needed for your specific output

        print()  # Print a newline after the joint updates


    def _simpleMoveCallback(self,command, scale = 'small') :

        if scale == 'small':
            if command == 'w' :
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
        

    def __paramPoseCallback(self,command):
        pass

    

# ---------------- Webots Action ---------------------



    def movePoseA(self, Angle):
        msg = JointState()
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()
        for i in range(self._DOF):
            msg.name.append(self._jointNames[i])
        msg.position = Angle
        #
        msg.velocity = self._jointVelocity
        msg.effort = []

        self._webotJointPub(msg)

        self.rate1.sleep()

    def movePoseT(self,Transform):
        solvedAngle = zeus_kinematics.ARM6_kinematics_inverse_arm(Transform)
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

    def ___rotateZ(self,zAngle)  :
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






            