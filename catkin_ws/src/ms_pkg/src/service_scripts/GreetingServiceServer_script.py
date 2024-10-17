import os, sys
import rospy

home_dir = os.path.expanduser("~")
ws_dir = os.path.join(home_dir, "2024_ZEUS")
config_dir = os.path.join(ws_dir, "config")
sys.path.append(config_dir)

print(sys.path)


from hri_config import HRIConfig
from ms_pkg.srv import Greeting_service, Greeting_serviceResponse

import anthropic
import base64
import json
import yaml


rospy.init_node("GreetingServiceNode")
print(HRIConfig.greeting_image_path)


class Vision_answer:

    def __init__(self):
        self.client = anthropic.Anthropic()
        self.image1_media_type = "image/png"
        print("vision model loading")
        self.introduction = """ 
        <instructions>
        당신은  바텐더 입니다.
        당신의 이름은 "싸이버"입니다.
        손님을 응대하고 주문을 받으세요.
        메뉴는 진토닉, 모히토, 섹스온더비치 가 있습니다.
        손님과 대화를 하세요. 
        2문장 이내로 대답하세요
        </instructions>
                """
    
        self.history_messages = [] ## this is for chatbot history!!!



    
    
    
    def encode_image(self):  #encode image to base64 for chat gpt prompt, first  need a path for imag
        with open(HRIConfig.greeting_image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")





    def Vision_chat(self, ):
        
        print("vision chat 실행중")
       
        captured_img = self.encode_image()

        self.vision = [
                        {
                        "role": "user", 
                        "content": [
                            {
                                "type": "image",
                                 "source": {
                                    "type": "base64",
                                    "media_type": self.image1_media_type,
                                    "data": captured_img,
                                },
                            },
                            
                            {
                                "type": "text", 
                                "text": "안녕 내 모습이야. 내 모습에 대해 칭찬해줄래?"
                            },
                        ],
                        }
        ]


        temp_history = {
                        "role": "user", 
                        "content": [
                            {
                                "type": "text", 
                                "text": "안녕 내 모습이야. 내 모습에 대해 칭찬해줄래?"
                            },
                        ],
                        }
        
        self.history_messages.append(temp_history)

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=200,
            messages=self.vision)
            
        
        output = response.content[0].text
        
        temp_history = {
                        "role": "assistant", 
                        "content": [
                            {
                                "type": "text", 
                                "text": f"{output}"
                            }
                        ],
                        }
        self.history_messages.append(temp_history)
      


        return output

#### self.messages should be sent to Chatbot class.

    def extract_history(self):
        print("extractng history")
        return self.history_messages


vis = Vision_answer()


def GreetingServiceCallback(req):
    if req.action == "inference":
        greeting_output = vis.Vision_chat()
        return Greeting_serviceResponse(greeting_output)

    elif req.action == "history":
        history = vis.extract_history()
        history_json_str = json.dumps(history) ####여기 관전 뽀인뜨
        return Greeting_serviceResponse(history_json_str)


def openGreetingServiceServer():
    _ = rospy.Service("GreetingService", Greeting_service, GreetingServiceCallback)
    print("Greeting Service activated")
    rospy.spin()

if __name__ == "__main__":
    openGreetingServiceServer()
 

