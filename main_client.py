from agent.agent import Agent

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image



class ZeusAgent(Agent):

    def __init__(self,name):

        self.name = name
        
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
        pass