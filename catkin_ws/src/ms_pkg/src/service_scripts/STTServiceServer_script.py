import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))


import rospy
from ms_pkg.srv import STT_service, STT_serviceResponse
import whisper
from custom_utils import EasyLogger as EL

node_name = "STTServiceServerNode"
rospy.init_node(node_name)
config = {}
config["weight_type"] = rospy.get_param("~weight_type", "large")
config["service_name"] = rospy.get_param("~service_name", "STTService")
config["device"] = rospy.get_param("~device", "cpu")
el = EL(node_name, config)

stt_model = whisper.load_model(config["weight_type"], device='cuda')
# rospy.loginfo(f"model weight {config['weight_type']} loaded")

def STTServiceCallback(req):
    file_path = req.file_path
    result = stt_model.transcribe(file_path, language="ko")
    rospy.loginfo(result)
    return STT_serviceResponse(result["text"])

def openSTTServiceServer():
    _ = rospy.Service(config["service_name"], STT_service, STTServiceCallback)
    el.initHello()
    rospy.spin()


if __name__ == "__main__":
    openSTTServiceServer()