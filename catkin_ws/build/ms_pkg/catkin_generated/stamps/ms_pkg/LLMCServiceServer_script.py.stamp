import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))

import rospy
import yaml
import json
from std_msgs.msg import String
from ms_pkg.srv import LLMC_service, LLMC_serviceResponse
from custom_utils import EasyLogger as EL

home_dir = os.path.expanduser("~")

node_name = "LLMCServiceServerNode"
rospy.init_node(node_name)
config = {}

config['service_name'] = rospy.get_param("~service_name", default="LLMCService")
el = EL(node_name, config)
from openai import OpenAI

# with open(api_key_path) as f:
#     api_config = yaml.load(f, Loader=yaml.FullLoader)




class Chatbot:
    def __init__(self):
        self.model="gpt-4o"

        print("chatbot model loading")
        
        self.messages = [
        {"role": "system", "content": """

        당신의 이름은 "Cyber"입니다. 당신은 바텐더입니다. 고객이 당신과 대화하고 싶어하며 감정적인 공감을 원합니다. 또한 고객은 칵테일을 주문할 것입니다. 당신은 주문을 받고 고객과 감정적인 대화를 나눠야 합니다.
        
        여기 당신의 역할을 위한 참고 사항이 있습니다:
        고객이 대화를 원하면 매우 친절하게 대화를 나눠주세요.
        고객이 메뉴 추천을 원하면, 메뉴에서 칵테일을 추천해주세요.
         
        진토닉,마가리타,마티니,모히또,프렌치75,섹스온더비치,블루하와이안,화이트러시안
        
        고객이 메뉴를 알고 싶어하면, 이 8개의 메뉴를 말해주세요.
  
        답변은 3문장으로 해주세요. 너무 길지 않게.

            """}
            ]
        self.client = OpenAI()

        self.history_load_sub = rospy.Subscriber("chatbot_history_load_signal", String, self.load_history)
        self.history_unload_sub = rospy.Subscriber("chatbot_history_unload_siganl", String, self.unload_history)

        
    def load_history_messages(self, history_messages):


        self.history_messages = history_messages
        self.messages.extend(self.history_messages)
        
        return None

    def chat(self, user_input):

        print("chat 실행중")
        self.user_prompt = user_input
        self.request = {"role": "user", "content": self.user_prompt}
        self.messages.append(self.request)


        # print(self.messages)



      
        self.response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            max_tokens=100,
        )




        self.output = self.response.choices[0].message.content

        print(f"Answer: {self.output}")


        self.request = {"role": "assistant", "content": self.output}
        self.messages.append(self.request)


        return self.request

    def load_history(self, msg):
        history_str = msg.data
        history_json = json.loads(history_str)
        self.load_history_messages(history_json)
        print("In LLMCServiceServer: success to load history")

    def unload_history(self, msg):
        self.messages.clear()
        print("In LLMCServiceServer: success to unload history")
     




gpt = Chatbot()



def LLMCServieCallback(req):
    user_text = req.user_text
    llm_converstaion_result = gpt.chat(user_text)["content"]

    return LLMC_serviceResponse(llm_converstaion_result)


def openLLMCServiceServer():
    _ = rospy.Service(config['service_name'], LLMC_service, LLMCServieCallback)
    el.initHello()
    rospy.spin()

if __name__ == "__main__":
    openLLMCServiceServer()