import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))


import rospy
from ms_pkg.srv import TF_service, TF_serviceResponse
from custom_utils import EasyLogger as EL


node_name = "TFServiceServerNode"
rospy.init_node(node_name)
config = {}
config["menu_wordset"] = rospy.get_param("recommand_wordset", default=["추천"])
config["recommand_wordset"] = rospy.get_param("cheking_wordset", default=["좋아"])
config["order_wordset"] = rospy.get_param("menu_set", default=[""])

config["service_name"] = rospy.get_param("~service_name", default="TFService")
el = EL(node_name, config)


def TFServiceCallback(req):
    sentence = req.text
    menu_flag = False 
    order_flag = False
    recommand_flag = False

    for w in config["order_wordset"]:
        if w in sentence:
            order_flag =True
            break

    for w in config["menu_wordset"]:
        if w in sentence:
            menu_flag = True
            break
    
    for w in config["recommand_wordset"]:
        if w in sentence:
            recommand_flag = True
            break

    if menu_flag and recommand_flag:
        return TF_serviceResponse(2) #메뉴를 추천시 2를 반환
    
    elif menu_flag and order_flag:
        return TF_serviceResponse(1) #메뉴를 추천시 1을 반환
    
    else:
        return TF_serviceResponse(0)


    
    
   
    

def openTFServiceServer():
    _ = rospy.Service(config["service_name"],TF_service ,TFServiceCallback)
    el.initHello()
    rospy.spin()

if __name__ == "__main__":
    openTFServiceServer()