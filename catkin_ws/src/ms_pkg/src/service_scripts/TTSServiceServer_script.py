import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))

import rospy
from ms_pkg.srv import TTS_service, TTS_serviceResponse
from custom_utils import EasyLogger as EL
##################3
# from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

from google.cloud import texttospeech



node_name = "TTSServiceServerNode"
rospy.init_node(node_name)
config = {}
config["temp_dir"] = os.path.expanduser("~/.temp_files")
config["mp3_path"] = os.path.join(config["temp_dir"], "tts.mp3")
config["service_name"] = rospy.get_param("~service_name", default="TTSService")
config['language'] = rospy.get_param("~lang", default='ko')
el = EL(node_name, config)

client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",
        name="ko-KR-Neural2-C",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    )
audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )



def TTSServiceCallback(req):
    # text =  req.text
    input_text = texttospeech.SynthesisInput(text=req.text)
    # print("im in TTS service callback function")

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )
    
    # tts = gTTS(text=text, lang=config['language'])
    # tts.save(config["mp3_path"])
    
    try:
    # print("tts updated")

        with open(config["mp3_path"], 'wb') as tts_res:
            tts_res.write(response.audio_content)
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