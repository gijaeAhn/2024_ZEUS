import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))


import rospy
from ms_pkg.srv import TF_service, TF_serviceResponse
from custom_utils import EasyLogger as EL


node_name = "TFServiceServerNode"
rospy.init_node(node_name)
config = {}
config["recommand_wordset"] = rospy.get_param("recommand_wordset", default=["추천"])
config["checking_wordset"] = rospy.get_param("cheking_wordset", default=["좋아"])
config["service_name"] = rospy.get_param("~service_name", default="TFService")
el = EL(node_name, config)


def TFServiceCallback(req):
    
    user_sentence = req.text
    if req.mode == "recommand":
        recommand_flag = False
        for word in config["recommand_wordset"]:
            if word in user_sentence:
                recommand_flag = True
                break
            
        if recommand_flag:
            return TF_serviceResponse(1)
        else:
            return TF_serviceResponse(0)
    
    
    elif req.mode == "check_answer":
    
        #사용자 응답중 특정 단어를 검출해 yes 인지 no 인지 판단
        
        for yes_word in config["checking_wordset"]["positive_wordset"]:
            if word in yes_word:
                return TF_serviceResponse(1)
    
        for no_word in config["checking_wordset"]["negative_wordset"]:
            if no_word in user_sentence:
                return TF_serviceResponse(1)
            
        return TF_serviceResponse(0)
    

def openTFServiceServer():
    _ = rospy.Service(config["service_name"],TF_service ,TFServiceCallback)
    el.initHello()
    rospy.spin()

if __name__ == "__main__":
    openTFServiceServer()