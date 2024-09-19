#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import sys
import select
import termios
import tty

def getKey():
    """Capture a single key press without waiting for Enter."""
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    # Save terminal settings
    settings = termios.tcgetattr(sys.stdin)
    # Initialize ROS node
    rospy.init_node('keyboard_publisher')
    # Create a publisher to the '/zeus/fsm' topic
    pub = rospy.Publisher('/zeus/fsm', String, queue_size=10)
    # Mapping of keys to messages
    key_mapping = {
        'z': 'idle',
        'x': 'speaking',
        'c': 'shaking',
        'v': 'moving',
    }
    print("Press 'z', 'x', 'c', or 'v' to publish messages. Press Ctrl-C to exit.")

    try:
        while not rospy.is_shutdown():
            key = getKey()
            if key in key_mapping:
                message = key_mapping[key]
                pub.publish(message)
                print("Published:", message)
    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        print("Error:", e)
    finally:
        # Restore terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)