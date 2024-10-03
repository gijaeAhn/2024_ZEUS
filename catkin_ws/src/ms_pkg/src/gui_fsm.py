import os
import sys
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
        # self.label.setStyleSheet("background-color: orange;")
        self.label.setScaledContents(True)  # QLabel에서 이미지 크기를 조정할 수 있도록 설정
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 크기 정책 설정
        
        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.sub = rospy.Subscriber("gui_state_topic", String, self.callback)

        self.current_state = "idle"
        self.load_images()
        self.label.setPixmap(self.idle_img)
        print("im here")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ros_spin)
        self.timer.start(100)  # 100ms마다 호출

    def ros_spin(self):
        rospy.rostime.wallsleep(0.01)  # 잠시 대기
        # rospy.spin_once()  # 한 번의 콜백 처리


    def load_images(self):
        """ 이미지 로드 """
        # self.sad_img = QPixmap(os.path.join(media_dir, "sad.jpg"))
        self.listening_img = QPixmap(os.path.join(media_dir, "listen.jpg"))
        self.speaking_img = QPixmap(os.path.join(media_dir, "speak2.jpg"))
        
        self.idle_img = QPixmap(os.path.join(media_dir, "idle.png"))

    def update_image(self, state):
        """ 상태에 따라 이미지 업데이트 """
        if state == self.current_state:
            return  # 현재 상태와 동일하면 아무것도 하지 않음
      
        self.current_state = state
        if state == "idle":
            self.label.setPixmap(self.idle_img)
        elif state == "speaking":
            self.label.setPixmap(self.speaking_img)
        elif state == "listening":
            self.label.setPixmap(self.listening_img)
        # elif state == "sad":
        #     self.label.setPixmap(self.sad_img)

    def callback(self, topic):
        """ ROS 메시지를 수신했을 때 호출되는 콜백 함수 """
        state = topic.data
        self.update_image(state)

if __name__ == "__main__":
    rospy.init_node("gui_fsm")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    print("imhere")

    # ROS 이벤트 루프 실행
    sys.exit(app.exec_())