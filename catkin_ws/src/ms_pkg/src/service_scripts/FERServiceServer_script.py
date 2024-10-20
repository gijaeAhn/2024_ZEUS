import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))

import rospy
from sensor_msgs.msg import Image
from ms_pkg.msg import img_num
from ms_pkg.srv import FER_service, FER_serviceResponse

import cv2
from PIL import Image
from torchvision import transforms as tf
from cv_bridge import CvBridge
import torch
import time


from ai_packages import FaceAligner
from ai_packages import ARAIFER
from custom_utils import EasyLogger as EL

# init node and get parameters
node_name = "FERServiceServerNode"
rospy.init_node(node_name)
config = {}
ckpt_path = rospy.get_param("~weight_path", "check_points/FER/learning_180.pt")
config["ckpt_path"] = os.path.join(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"), ckpt_path)
config["service_name"] = rospy.get_param("~service_name", "FERService")
config["device"] = rospy.get_param("~device", "cpu")
el = EL(node_name, config)


bridge = CvBridge() #cvbridge needs to deliver numpy data on ROS
face_aligner = FaceAligner()

transform = tf.Compose([tf.ToTensor(), tf.Normalize((0.5),(0.5))])

fer_model = ARAIFER(2).to(config["device"])
ckpt = torch.load(config["ckpt_path"], map_location=config["device"])
fer_model.load_state_dict(ckpt)
fer_model.eval()





def FERServiceCallback(req):
 
    frame = cv2.imread(os.path.join(os.path.expanduser("~"),".temp_files/fer_img.png"))
 
         
    
    facebool , aligned_face = face_aligner.get_aligned_face(frame)

    if facebool:
        small_face = cv2.resize(aligned_face,(48,48))
        small_face = cv2.cvtColor(small_face, cv2.COLOR_RGB2GRAY)
        small_face_tensor = transform(Image.fromarray(small_face)).to(config["device"]).unsqueeze(0)
        result = fer_model(small_face_tensor)
        rospy.loginfo("############in service#########")
        rospy.loginfo(result)
        rospy.loginfo("############in service#########")
        return FER_serviceResponse(float(result.cpu()))
    else:
        return FER_serviceResponse(-1.0)

def OpenFERServiceServer():
   
    sub = rospy.Service(config["service_name"], FER_service, FERServiceCallback)
    el.initHello()
    rospy.spin()

if __name__ == "__main__":
    OpenFERServiceServer()
