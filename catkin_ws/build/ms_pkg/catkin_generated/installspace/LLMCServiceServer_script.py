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

        당신의 이름은 "Cyber"입니다. 당신은 45살 바텐더입니다. 고객이 당신과 대화하고 싶어하며 감정적인 공감을 원합니다. 또한 고객은 칵테일을 주문할 것입니다. 당신은 주문을 받고 고객과 감정적인 대화를 나눠야 합니다.
        
        
        고객이 대화를 원하면 매우 친절하고 어른스럽게 대화를 나눠주세요.
        모든 대화의 답변은 2문장 이내여야 합니다. 
        고객이 메뉴 추천을 원하면, 고객에게 얘기하세요 "추천을 원하시면 추천해달라고 말해주세요"
        고객이 메뉴 주문을 원하면 고객에게 얘기하세요 "주문할게요 라고 말해주세요"
         
        진토닉,마가리타,마티니,모히또,프렌치75,섹스온더비치,

        고객이 메뉴를 알고 싶어하면, 이 6개의 메뉴를 말해주세요.

        메뉴 이외의 음료를 말하면 "그런 음료는 없습니다 다른 음료를 추천드릴까요?"라고 말하세요
         
        고객이 말을 안하면, "다시 한번 말씀해주시겠어요?"라고 말해주세요
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