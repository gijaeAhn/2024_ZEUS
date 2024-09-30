import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from std_msgs.msg import String
import rospy



home_dir = os.path.expanduser('~')
ws_dir = os.path.join(home_dir, "Desktop/2024_ZEUS")
media_dir = os.path.join(ws_dir, "media/face")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROS Image Subscriber")
        
        self.label = QLabel("Waiting for images...")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.sub = rospy.Subscriber("gui_state_topic", String, self.callback)


        self.sad_img = QPixmap(os.path.join(media_dir,"sad.jpg"))
        self.shaking_img = QPixmap(os.path.join(media_dir,"shaking.jpg"))
        self.speaking_img = QPixmap(os.path.join(media_dir,"speaking.jpg"))
        self.idle_img = QPixmap(os.path.join(media_dir,"idle.jpg"))

        self.label.setPixmap(self.idle_img)

    def callback(self, topic):
        state = topic.data

        

        # self.image_subscriber = ImageSubscriber()
        # self.image_subscriber.set_label(self.label)

if __name__ == "__main__":
    rospy.init_node("gui_fsm")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()

    # ROS 이벤트 루프 실행
    rospy.spin()
    sys.exit(app.exec_())