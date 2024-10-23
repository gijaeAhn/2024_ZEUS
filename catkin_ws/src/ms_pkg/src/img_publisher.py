import rospy

import os, sys
home_dir = os.path.expanduser('~')
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module"))
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge



rospy.init_node("img_publisher_node")

pub = rospy.Publisher("captured_img",Image, queue_size=10 )
bridge = CvBridge()
cap = cv2.VideoCapture(4) 
rate = rospy.Rate(10)


def openWebcamNode():
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            # rospy.logerr("Failed to capture image from webcam.")
            break
        
        # OpenCV 이미지를 ROS 메시지로 변환
        image_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        pub.publish(image_msg)
        rate.sleep()
    
    cap.release()

if __name__ == "__main__":
    openWebcamNode()
    pass