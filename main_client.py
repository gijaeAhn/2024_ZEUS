from agent.agent import Agent

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Image
from sensor_msgs.msg import JointState
from tf2_msgs.msg import TFMessage




class ZeusAgent(Agent):

    def __init__(self,name):

        self.name = name
        
        # PUB
            #Output Display Setting
        self._headDisplayImagePub  = rospy.Publisher('/zeus/real/outputDisplay_image'     , Image      , queue_size = 10)
        self._headTextPub          = rospy.Publisher('/zeus/real/outputDisplay_text'      , String     , queue_size = 10)
        self._paramPosePub         = rospy.Pulbicher('/zeus/real/parampose'               , TFMessage  , queue_size = 10)
        self._armJointPub          = rospy.Publisher('/zeus/real/armJoint'                , JointState , queue_size = 10)

        # SUB 

        self._menuSub                = rospy.Subscriber('/zeus/real/menu', String, self._menuCallback )
        

        # SERVICE

        self._paramPoseClient          = rospy.ServiceProxy('/zeus/real/paramPose', tf_servicef)


        # INTERNAL ESTIMATE

        self.cur_pose = None

    def _menuCallback(self,msg):    
        pass