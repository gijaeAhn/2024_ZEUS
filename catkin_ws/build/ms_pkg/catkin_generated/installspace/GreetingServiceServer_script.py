import os, sys
import rospy

home_dir = os.path.expanduser("~")
module_dir = os.path.join(home_dir, "Desktop/2024_ZEUS/module")
sys.path.append(module_dir)

from ms_pkg.srv import Greeting_service, Greeting_serviceResponse
from chatgptwithvision import Vision_answer

import requests
import base64
import json
import yaml


arai_key_path = os.path.join(home_dir, ".temp_files/gpt_key.yaml")

with open(arai_key_path) as f:
    api_config = yaml.load(f, Loader=yaml.FullLoader)

rospy.init_node("GreetingServiceNode")


class VisionBot(Vision_answer):
    def __init__(self):
        
        super().__init__(api_config["api_key"])
        

    def Vision_chat(self, usr_prompt):
  
        # self.user_prompt = input('Enter: ')

        self.vision = [
                        {
                        "role": "user", 
                        "content": [
                            {
                                "type": "text", 
                                "text": usr_prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{self.image}"
                                }
                            }
        
        ]
        }
        ]


        # self.messages.append(self.vision)

        self.payload = {
            "model": self.model,
            "messages": self.messages+self.vision,
            "max_tokens": 100

        }


        self.history = {"role": "user", "content": usr_prompt}
        self.history_messages.append(self.history)




        self.response = requests.post("https://api.openai.com/v1/chat/completions", headers=self.headers, json=self.payload)
        print(self.response.json())
        
        self.output = self.response.json()['choices'][0]['message']['content']
        

        self.history = {"role": "assistant", "content": self.output}
        self.history_messages.append(self.history)
      
        return self.output
    


        # return self.messages



vis = VisionBot()



def GreetingServiceCallback(req):
    if req.action == "inference":
        image_path = req.image_path
        user_prompt = req.user_prompt
        vis.get_image(image_path)
        gpt_output = vis.Vision_chat(user_prompt)

        return Greeting_serviceResponse(gpt_output)

    elif req.action == "history":
        history = vis.extract_history()
        history_json_str = json.dumps(history)
        return Greeting_serviceResponse(history_json_str)


def openGreetingServiceServer():
    _ = rospy.Service("GreetingService", Greeting_service, GreetingServiceCallback)
    print("Greeting Service activated")
    rospy.spin()

if __name__ == "__main__":
    openGreetingServiceServer()
 

