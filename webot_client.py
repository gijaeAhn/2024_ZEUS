import sys
import os
import threading

home_dir = os.path.expanduser('~')

sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))


from agent.agent import Agent
from agent.webots_endeffector import webotsEE
import rospy

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



class WebotsAgent(Agent) :

    def __init__(self) :


        Agent.__init__(self)

        self._initJoint = WebotsConfig.initPoseA
        self._initTrans = WebotsConfig.initPoseT
        self._jointNames = WebotsConfig.jointNameList
        self._curJoint = self._initJoint
        self._curTrans = self._initTrans
        self._commandJoint = self._curJoint
        self._eeController = webotsEE()
        self._jointVelocity = WebotsConfig.defaultAngleVelocity




        #----- Publisher
        self._webotsJointCommandPub        = rospy.Publisher('/zeus/webots/jointCommand'           ,  JointState    , queue_size = 10             )  
        self._webotsFSMPub                 = rospy.Publisher('/zeus/fsm'                           ,  String        , queue_size = 10             )
        #----- Subscriber
        # self._paramPoseSub                 = rospy.Subscriber('/zeus/webots/paramPose'             ,  String              , self._paramPoseCallback         )
        # self._eeCommandSub                 = rospy.Subscriber('/zeus/webots/eeCommand'             ,  String              , self._eeControlCallback         )
        # self._webotsJointCommandSub        = rospy.Subscriber('/zeus/webots/prejointCommand'       ,  JointState          , self._preJointCommandCallback   )
        # self._webotsRealJointSub           = rospy.Subscriber('/zeus/webots/realJoint'             ,  JointState          , self._updateJointCallback       )
        self._webotsSimpleMoveSub          = rospy.Subscriber('/zeus/webots/simpleMoveCommand'     ,  String              , self._simpleMoveCallback        )
        # self._webotsHRICommandSub          = rospy.Subscriber('/zeus/webots/HRICommand'            ,  String              , self._HRIEventLoopCallback           )
        # self._webotsPositionMoveSub        = rospy.Subscriber('/zeus/webots/positionCommnad'       ,  String              , self._paramPoseCallback         )
        self._webotsMenuSub                = rospy.Subscriber('/zeus/webots/menu'                  ,  String              , self._menuCallback              )
        self._webotsCusMsgSub              = rospy.Subscriber('/zeus/webots/customerMsg'           ,  String              , self._cusMsgCallback            )
        
        #----- Additional Threads
        threading.Thread(target=self._publishFsmState,daemon=True).start()

        #Temp
        self._fsm.handleEvent('hri_start')
        self._fsm.handleEvent('get_menu')


        rospy.spin()



# ---------------- Thread Functions ------------------

    def _publishFsmState(self) :
        while not rospy.is_shutdown():
            stateMsg = String()
            stateMsg.data = self._fsm.getState()
            self._webotsFSMPub.publish(stateMsg)
            self.rateFast.sleep()


# ---------------- Callback Functions ----------------

    def _cusMsgCallback(self,sentence):
        pass 


    def _menuCallback(self,menu):
        self._fsm.handleEvent("get_menu")
        self._makeMenu(menu)
        self._fsm.handleEvent("serve_menu")
        self._hereYouare()

    
    def _preJointCommandCallback(self,jointState):
        msg = JointState(jointState)
        self._webotsJointCommandPub.publish(msg)


    def _updateJointCallback(self, jointState):
        tempPosition = [0.0] * 6  
        for index, (name, position) in enumerate(zip(jointState.name, jointState.position)):
            if index < 6: 
                tempPosition[index] = position
            else:
                break  
        tempPosition = [angle * direction for angle, direction in zip(tempPosition, WebotsConfig.ROTATE_DIRECTION)]    
        self._curJoint = tempPosition

        self._curTrans = ARM6_kinematics_forward_armReal(self._curJoint)
        self._curTrans.printTransform(self._curTrans)  

    def _simpleMoveCallback(self,msg, scale = 'small') :
        
        command = msg.data        

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
                self._moveZ(-WebotsConfig.smallCommandStep)
            elif command == 'i' :
                self.movePoseT(WebotsConfig.startPoseT)
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
                self._moveZ(-WebotsConfig.bigCommandStep)
            elif command == 'i' :
                self.movePoseT(WebotsConfig.startPoseT)


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

    def _makeMenu(self,menu):


        self.movePoseT(WebotsConfig.dispensorT)
        print("Arrived at the dispensor")
        self.rateNormal.sleep()

        #Check the EE is opened
        if self._EE.getState != 'open':
            print("EE is closed")
            self._EE.open()

        if menu == WebotsConfig.menuList[0]:
            # Key characters should be replaced with actual menu name
            # Moving sequence should be y - x - z || z - x - y 
            self._moveY(WebotsConfig.menuOffset['A'][1])
            self._moveX(WebotsConfig.menuOffset['A'][0])
            self._moveZ(WebotsConfig.menuOffset['A'][2])
            # Move backward
            self._moveZ(-WebotsConfig.menuOffset['A'][2])
            self._moveX(-WebotsConfig.menuOffset['A'][0])
            self._moveY(-WebotsConfig.menuOffset['A'][1])
        elif menu == WebotsConfig.menuList[1]:
            self._moveY(WebotsConfig.menuOffset['B'][1])
            self._moveX(WebotsConfig.menuOffset['B'][0])
            self._moveZ(WebotsConfig.menuOffset['B'][2])
            self._moveZ(-WebotsConfig.menuOffset['B'][2])
            self._moveX(-WebotsConfig.menuOffset['B'][0])
            self._moveY(-WebotsConfig.menuOffset['B'][1])
        elif menu == WebotsConfig.menuList[2]:
            self._moveY(WebotsConfig.menuOffset['C'][1])
            self._moveX(WebotsConfig.menuOffset['C'][0])
            self._moveZ(WebotsConfig.menuOffset['C'][2])
            self._moveZ(-WebotsConfig.menuOffset['C'][2])
            self._moveX(-WebotsConfig.menuOffset['C'][0])
            self._moveY(-WebotsConfig.menuOffset['C'][1])
        elif menu == WebotsConfig.menuList[3]:
            self._moveY(WebotsConfig.menuOffset['D'][1])
            self._moveX(WebotsConfig.menuOffset['D'][0])
            self._moveZ(WebotsConfig.menuOffset['D'][2])
            self._moveZ(-WebotsConfig.menuOffset['D'][2])
            self._moveX(-WebotsConfig.menuOffset['D'][0])
            self._moveY(-WebotsConfig.menuOffset['D'][1])
        elif menu == WebotsConfig.menuList[4]:
            self._moveY(WebotsConfig.menuOffset['E'][1])
            self._moveX(WebotsConfig.menuOffset['E'][0])
            self._moveZ(WebotsConfig.menuOffset['E'][2])
            self._moveZ(-WebotsConfig.menuOffset['E'][2])
            self._moveX(-WebotsConfig.menuOffset['E'][0])
            self._moveY(-WebotsConfig.menuOffset['E'][1])
        
        print("Success to get base bevarge\n")

        self._EE.close()

        self.movePoseT(WebotsConfig.shakingT)

        print("Arrvied at the Shaking Position")

        if self._EE.getState != 'closed':
            print("EE is opened")
            return

        
        self._shake()

        

        print("Shaking Done\n")


    def _shake(self):
        self._fsm.handleEvent('shake')
        self._fsm.handleEvent('finish_shake')


    def _hereYouare(self):
        self.movePoseT(WebotsConfig.servicePositionT)
        sentence = 'Here you are'
        self._speak(sentence)
        self._EE.open()
        self._pour()

        self._fsm.handleEvent('serve_menu')

    
    def _pour(self):
        pourTransform = self._curTrans
        pourTransform = pourTransform.rotateZ(-WebotsConfig.pourAngle)
        solvedAngle   = ARM6_kinematics_inverse_arm(pourTransform)
        self.movePoseA(solvedAngle) 
        self.rateSlow.sleep()

        afterTransform = self._curTrans
        afterransform = afterTransform.rotateZ(WebotsConfig.pourAngle)
        solvedAngle   = ARM6_kinematics_inverse_arm(pourTransform)
        self.movePoseA(solvedAngle) 

        self.rateNormal.sleep()

    


# --------------- Base Action ------------------------
    def movePoseA(self, Angle):
        
        print(self._fsm.getState())
        if not(self._fsm.getState() == "moving" or self._fsm.getState() == "shaking"):
            print('State is not Moiving : Quit!!!')
            return 

        if len(Angle) != WebotsConfig.DOF:
            rospy.logerr("Incorrect number of angles provided. Expected {}, got {}.".format(WebotsConfig.DOF, len(Angle)))
            return
        
        # For debug
        # DEGREE_TO_RADIAN = 0.0174533
        # Angle = [angle * DEGREE_TO_RADIAN for angle in WebotsConfig.pose3A]
        Angle = [angle * direction for angle, direction in zip(Angle, WebotsConfig.ROTATE_DIRECTION)]

        msg = JointState()
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()
        for i in range(WebotsConfig.DOF):
            msg.name.append(self._jointNames[i])
            msg.position.append(Angle[i])
        
        msg.velocity = self._jointVelocity
        msg.effort = []

        self._webotsJointCommandPub.publish(msg)

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


# -------------- For HRI --------------------------------

    def _speak(self,ttsData):
        pass
    
    def _listen(self,sttData):
        pass

    # --- Facial Expression will be treated at another Node.
    @DeprecationWarning
    def _displayFace(self,face):
        pass




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







            