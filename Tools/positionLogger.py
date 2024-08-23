import rospy 
from sensor_msgs.msg import JointState
from lib.transform import Transform







class positionLogger :

    def __init__(self,name):

        self._savedTransform =    None

        self.transSub        =    rospy.Subscriber("/zeus_trans",)

        self.



    def transSubCallback(self,data):




    def getPosition(self,Transform):
        self._savedTransform = Transform


def main(args):
    zeusPositionLogger = positionLogger()

    rospy.init_node('zeus_position_logger', anonymous=True)

    try:
        rospy.spin()

    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main(sys.args)        


