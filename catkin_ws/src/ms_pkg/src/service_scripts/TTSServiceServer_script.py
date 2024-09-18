import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))

import rospy
from ms_pkg.srv import TTS_service, TTS_serviceResponse
from custom_utils import EasyLogger as EL

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

node_name = "TTSServiceServerNode"
rospy.init_node(node_name)
config = {}
config["temp_dir"] = os.path.expanduser("~/.temp_files")
config["mp3_path"] = os.path.join(config["temp_dir"], "tts.mp3")
config["service_name"] = rospy.get_param("~service_name", default="TTSService")
config['language'] = rospy.get_param("~lang", default='ko')
el = EL(node_name, config)



def TTSServiceCallback(req):
    text=  req.text
    print("im in TTS service callback function")
    tts = gTTS(text=text, lang=config['language'])
    tts.save(config["mp3_path"])
    try:
        play(AudioSegment.from_mp3(config["mp3_path"]))
        return TTS_serviceResponse(1)
    except:
        return TTS_serviceResponse(0)

        
def openTTSServiceServer():
    _ = rospy.Service(config["service_name"], TTS_service, TTSServiceCallback)
    el.initHello()
    rospy.spin()


if __name__ == "__main__":
    openTTSServiceServer()