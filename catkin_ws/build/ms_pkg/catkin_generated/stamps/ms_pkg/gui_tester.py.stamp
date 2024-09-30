import rospy
from std_msgs.msg import String
rospy.init_node("fuck")




pub = rospy.Publisher("gui_state", String, queue_size=1)

while(True):
    temp = input("암거나 입력:")
    if temp in ["idle", "speak", "listen"]:
        pub.publish(temp)
