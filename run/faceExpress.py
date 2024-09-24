#!/usr/bin/env python

import sys
import os

home_dir = os.path.expanduser('~')
project_root = os.path.join(home_dir, 'Desktop/2024_ZEUS')
print(f"Project root: {project_root}")

import rospy
from std_msgs.msg import String
import cv2

class FSMImageDisplayNode:
    def __init__(self):
        rospy.init_node('fsmImageDisplayNode', anonymous=True)
        global project_root
        self.image_dir = os.path.join(project_root, 'media', 'face')
        print(f"Image directory: {self.image_dir}")

        # Initialize OpenCV window
        cv2.namedWindow('FSM State Image', cv2.WINDOW_AUTOSIZE)

        # Initialize the current image to None
        self.current_image = None

        # Subscribe to the FSM state topic
        rospy.Subscriber('/zeus/fsm', String, self.state_callback)

        rospy.on_shutdown(self.cleanup)

        # Start the main loop
        self.main_loop()

    def main_loop(self):
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            # Process any pending callbacks
            rospy.sleep(0.001)  # Short sleep to allow callbacks to be processed

            if self.current_image is not None:
                cv2.imshow('FSM State Image', self.current_image)

            # Wait for 1 ms and capture any key press (required for OpenCV GUI)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                rospy.signal_shutdown('User requested shutdown.')
                break

            rate.sleep()

    def state_callback(self, msg):
        state = msg.data
        rospy.loginfo(f"Received FSM state: {state}")

        image_file = os.path.join(self.image_dir, f"{state}.jpg")
        print(f"Image file path: {image_file}")

        if os.path.exists(image_file):
            image = cv2.imread(image_file)

            if image is not None:
                self.current_image = image
            else:
                rospy.logwarn(f"Failed to load image: {image_file}")
        else:
            rospy.logwarn(f"Image file does not exist: {image_file}")

    def cleanup(self):
        cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        FSMImageDisplayNode()
    except rospy.ROSInterruptException:
        pass
