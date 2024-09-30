import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from std_msgs.msg import String

import rospy
from PIL import Image
import numpy as np
import cv2




def load_pixmap(path):
    img = Image.open(path)
    img_byte = img.tobytes('raw', "RGB")
    q_img = QImage(img_byte, img.width, img.height, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(q_img)
    return pixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_path = rospy.get_param("~image_path", default="~/.temp_files/sample_images")
        print(image_path)
        self.idle_img = load_pixmap(os.path.join(image_path, "idle.png"))
        self.listen_img = load_pixmap(os.path.join(image_path, "speak.jpg"))
        self.speak_img = load_pixmap(os.path.join(image_path, "listen.jpg"))


        self.setWindowTitle("PyQt 창 예제")
        self.setGeometry(900, 900, 600, 400)  # x, y, width, height

        self.view = QGraphicsView(self)
        self.view.setGeometry(0,0,400 ,400)
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)


        self.scene.addPixmap(self.listen_img)

    def update_image(self, state):
        if state == "speak":
            self.scene.addPixmap(self.speak_img)
        
        if state =="listen":
            self.scene.addPixmap(self.listen_img)

        if state =="idle":
            self.scene.addPixmap(self.idle_img)
    








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    def GUICallback(self, msg):
        state = msg.data
        window.update_image(state)

    rospy.init_node("gui_node")
    stateListener = rospy.Subscriber("gui_state", String ,GUICallback)
    print("hereerererer")
    sys.exit(app.exec_())
    rospy.spin()



