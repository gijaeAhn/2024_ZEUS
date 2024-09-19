
import sys
import os

home_dir = os.path.expanduser('~')

sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))

from positionLogger import *

class ModifiedPositonLogger(positionLogger):
    def __init__(self):

    def on_press(self, key):
        try :
            key_str = '{0}'.format(key.char)
        except :
            key_str = '{0}'.format(key)
        print(key_str)
        if key_str == 'r':
            self._HRICommandPub.publish(key_str)
        else:
            self._moveCommandPub.publish(key_str)



def main():
    zeusPositionLogger = positionLogger()

    rospy.init_node('zeus_position_logger', anonymous=True)

    try:
        rospy.spin()

    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main()        

