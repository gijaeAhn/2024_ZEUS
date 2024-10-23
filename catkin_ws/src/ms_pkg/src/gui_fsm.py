import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import rospy

home_dir = os.path.expanduser('~')
ws_dir = os.path.join(home_dir, "Desktop/2024_ZEUS")
media_dir = os.path.join(ws_dir, "media/face")
ui_file_path = os.path.join(ws_dir, "media/ui/gui.ui")


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # .ui 파일을 로드 (파일 경로를 적절히 변경)
        uic.loadUi(ui_file_path, self)
        self.setupBasic()
        self.current_state = "idle"
        self.load_images()
        self.label.setPixmap(self.idle_img)
        print("im here")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ros_spin)
        self.timer.start(33)  # 100ms마다 호출

        self.state_sub = rospy.Subscriber("gui_state_topic", String, self.StateCallback)
        self.img_sub = rospy.Subscriber("captured_img", Image, self.ImgCallback)
        self.subtitle_sub = rospy.Subscriber("hri_subtitle", String, self.SubtitleCallback)
        self.bridge = CvBridge()

    def setupBasic(self):
        font = QFont("Arial", 24)
        self.subtitle_label.setFont(font)
        self.subtitle_label.setWordWrap(True)

        
        self.guide_label.setText("빨강: 입장, 퇴장하실 때 눌러주세요. \n초록: 말씀하실 때 누르신 상태로 말씀해주세요." )
        guide_font = QFont("Arial", 24)
        self.guide_label.setFont(guide_font)
        self.guide_label.setWordWrap(True)

    def ros_spin(self):
        rospy.rostime.wallsleep(0.01)  # 잠시 대기
        # rospy.spin_once()  # 한 번의 콜백 처리

    def load_images(self):
        self.listening_img = QPixmap(os.path.join(media_dir, "listen.jpg")).scaled(900, 900)
        self.speaking_img = QPixmap(os.path.join(media_dir, "speak.jpg")).scaled(900, 900)
        self.idle_img = QPixmap(os.path.join(media_dir, "idle.jpg")).scaled(900, 900)

    def StateCallback(self, topic):
        """ ROS 메시지를 수신했을 때 호출되는 콜백 함수 """
        state = topic.data
        self.update_image(state)
    
    def ImgCallback(self, topic):
        cv_image = self.bridge.imgmsg_to_cv2(topic, "bgr8")
        q_img = self.cv2pix(cv_image)
        self.update_user_image(q_img)

    def cv2pix(self, cv):
        rgb_image = cv2.cvtColor(cv, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        # QImage를 QPixmap으로 변환
        return QPixmap.fromImage(q_image)


    def update_user_image(self, qimg):
        self.user_face_label.setPixmap(qimg)
    
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

    def SubtitleCallback(self, msg):
        self.subtitle_label.setText(msg.data)

    








if __name__ == "__main__":
    rospy.init_node("gui_fsm")
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    

    # ROS 이벤트 루프 실행
    sys.exit(app.exec_())