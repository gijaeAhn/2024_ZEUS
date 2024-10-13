import time
import rospy

rospy.init_node('my_node')
a = rospy.Rate(10)

tic = time.time()
# rospy.sleep(0.1)
# time.sleep(0.1)
a.sleep()
toc = time.time()

print(toc-tic)