import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))

import rospy
import anthropic

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


        # self.history_load_sub = rospy.Subscriber("chatbot_history_load_signal", String, self.load_history)
        # self.history_unload_sub = rospy.Subscriber("chatbot_history_unload_siganl", String, self.unload_history)


class Chatbot:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.introduction = """ 
        <instructions>
        당신은  바텐더 입니다.
        당신의 이름은 "싸이버"입니다.
        손님을 응대하고 주문을 받으세요.
        메뉴는 진토닉, 모히토, 소맥, 프랜치75, 마가리타, 마티니가 있습니다.
        소맥의 비율에 대해서는 언급하지 말아주세요.
        추천할 때는 메뉴를 랜덤으로 추천하세요.
        손님과 대화를 하세요. 
        2문장 이내로 대답하세요.
        주문이 확정되면 메뉴를 언급하고 '준비해드리겠습니다' 라고 하세요
        주문이 확정되기 전에는 준비해드리겠습니다 금지.

        


        </instructions>
        
        <example>
        Input:아무거나 주세요
        Ouput:추천해 드릴까요?
        Input: 네
        Ouput: 그럼 마가리타를 추천드립니다
        Input: 좋아요
        Ouput: 네 모히토 준비해드리겠습니다</example>
        

        <example>
        Input:마가리타 하나 주세요
        Ouput: 네 마가리타 준비해드리겠습니다</example>
    
        <example>
        Input: 그래 내일 학교가야해
        Output:  학교 가는 날이군요. 오늘 밤엔 충분히 쉬시길 바랍니다. 
        Input:  고맙다
        Output:  천만에요. 즐거운 시간 보내세요. 무슨 칵테일 필요하신가요?</example>

        <example>
        Input:아무거나 주세요
        Output:추천해 드릴까요?
        Input: 네
        Output: 그럼 모히토를 추천드립니다
        Input: 좋은걸 
        Output: 모히토 준비해드리겠습니다!
        </example>        
        """
                
        

        self.messages =[]


        
    def load_history_messages(self, history_messages):

        print("DEBUG:", history_messages)
        
        self.messages.extend(history_messages)
        
        return None

    def chat(self, user_input):

        request = {
            "role": "user",
            "content": [
                {
                    "type":"text",
                    "text":f"{user_input}"
                }
            ]  
        }
        self.messages.append(request)

        completion = self.client.messages.create(
            model = 'claude-3-5-sonnet-20240620',
            messages=self.messages,
            max_tokens=200,
            temperature=0,
            system=self.introduction
        )

        inference_output = completion.content[0].text

        inference_message = {
            "role": "assistant",
            "content": [
                {
                    "type":"text",
                    "text":f"{inference_output}"
                }
            ]
        }

        self.messages.append(inference_message)

        return inference_output



    def load_history(self, msg):
        history_str = msg.data
        history_json = json.loads(history_str)
        self.load_history_messages(history_json)
        print("In LLMCServiceServer: success to load history")

    def unload_history(self, msg):
        self.messages.clear()
        print("In LLMCServiceServer: success to unload history")
     




claude = Chatbot()



def LLMCServieCallback(req):
    user_text = req.user_text
    llm_converstaion_result = claude.chat(user_text)

    return LLMC_serviceResponse(llm_converstaion_result)


def openLLMCServiceServer():
    _ = rospy.Service(config['service_name'], LLMC_service, LLMCServieCallback)
    el.initHello()
    rospy.spin()

if __name__ == "__main__":
    openLLMCServiceServer()