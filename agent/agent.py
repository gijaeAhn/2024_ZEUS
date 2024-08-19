# ----------------- ROS Message -----------------
from actionlib
from geometry_msgs import PoseStamped, Quaternion
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan, Image
# -----------------------------------------------

from cv_bridge import CvBridge



import tf
import rospy


class Agent:
    def __init__(self):
        
        # PUB
            #Output Display Setting
        self.head_display_image_pub = rospy.Publisher('/output_display'     , Image, queue_size = 10)
        self.head_text_pub          = rospy.Publisher('/output_display_text', String, queue_size = 10)
        self.arm_joint_pub          = rospy.Publisher('')

        # SUB 

        self.fer_sub                = rospy.Subscriber('/fer', String, self.fer_callback )


        # INTERNAL ESTIMATE

        self.cur_pose = None

    def fer_callback(self,msg):     

