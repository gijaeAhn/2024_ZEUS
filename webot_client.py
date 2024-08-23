from agent.agent import Agent

# ----------------- ROS Message -----------------

from geometry_msgs import PoseStamped, Quaternion
from sensor_msgs.msg import JointState 
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan, Image
# -----------------------------------------------

from cv_bridge import CvBridge

import lib.zeus_kinematics_module


from config.config import WebotsConfig


import tf
import rospy


class WebotsAgent(Agent) :

    def __init__(self) :

        self.initial_pose = WebotsConfig.initPose







            