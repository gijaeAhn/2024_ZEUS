import rospy
from std_msgs.msg import String

class TTS():

    def __init__(self):
        self._pub = rospy.Publisher('/zeus/both/tts', String, queue_size=0)

    def say(self, text):

        msg = String
        msg.data = text
        self._pub.publish(msg)


if __name__ == '__main__':
    rospy.init_node('cyberCocktail_tts')
    tts = TTS()
    # rospy.sleep(1)
    print('tts init')
    tts.say('hello')
    # rospy.sleep(1)