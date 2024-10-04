import os, sys
home_dir = os.path.expanduser('~')
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module"))

import rospy
from ms_pkg.srv import IC_service, IC_serviceResponse
import cv2


rospy.init_node("ICServiceNode")

def ICServiceCallback(req):
    image_save_path = os.path.join(home_dir, ".temp_files/captured_img.png")




    #웹캠으로 캡쳐 및 저장까지 성공한경우
    try:
        cap = cv2.VideoCapture(0) 
        ret, frame = cap.read()  
        cv2.imwrite(image_save_path, frame)
        print("in IC service: success to capture image")
        return IC_serviceResponse(1)
    
    #실패할시 그냥 지워버림
    except:
        if os.path.exists(image_save_path):
            os.system(f"rm {image_save_path}")
        return IC_serviceResponse(0)



def openICServiceServer():
    _ = rospy.Service("ICService", IC_service, ICServiceCallback)
    try: 
        rospy.spin()
    except Exception as e:
        print(f"ERROR ==>> {e}")
        print("failed to open ICServiceServer")

if __name__ == "__main__":
    openICServiceServer()