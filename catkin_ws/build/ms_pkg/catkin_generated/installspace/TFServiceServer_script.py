import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))


import rospy
from ms_pkg.srv import TF_service, TF_serviceResponse
from custom_utils import EasyLogger as EL


node_name = "TFServiceServerNode"
rospy.init_node(node_name)
config = {}
config["wordset"] = rospy.get_param("recommand_wordset", default=["추천"])
config["service_name"] = rospy.get_param("~service_name", default="TFService")
el = EL(node_name, config)


def TFServiceCallback(req):
    user_sentence = req.text
    recommand_flag = False
    for word in config["wordset"]:
        if word in user_sentence:
            recommand_flag = True
            break
    
    if recommand_flag:
        return TF_serviceResponse(1)
    else:
        return TF_serviceResponse(0)
    

def openTFServiceServer():
    _ = rospy.Service(config["service_name"],TF_service ,TFServiceCallback)
    el.initHello()
    rospy.spin()

if __name__ == "__main__":
    openTFServiceServer()