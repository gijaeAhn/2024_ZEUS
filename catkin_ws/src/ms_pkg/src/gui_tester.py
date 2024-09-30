import rospy
from std_msgs.msg import String
rospy.init_node("fuck")




pub = rospy.Publisher("gui_state_topic", String, queue_size=1)
for _ in range(10000):
    temp = input("암거나 입력:")
    rospy.loginfo(_)
    pub.publish(temp)