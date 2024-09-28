import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))

import rospy
from ms_pkg.srv import LLMC_service, LLMC_serviceResponse
from custom_utils import EasyLogger as EL


node_name = "LLMCServiceServerNode"
rospy.init_node(node_name)
config = {}
config['prompt'] = rospy.get_param("~sys_prompt", default='')
config['service_name'] = rospy.get_param("~service_name", default="LLMCService")
el = EL(node_name, config)

from openai import OpenAI

class Chatbot:

    def __init__(self):
        
        self.client = OpenAI()
        self.introduction = """You will be provided with customer service quries. Your name is "Cyber". You are a bartender. 
              customer wants to talk with you and want feel empathy. Moreover, the customer will order a cocktail.
              you have to receive order and have an emotional conversation with the customer. 
              Here is the reference for your job.
                  - if the customer just says hi, then you have to introduce yourself. like this. "Hi my name is Cyber, a bartender. What should I do for you?"
                  if not, if the customer says about his feeling, then you should have a conversation with sympathy and talk very kindly. 
                  - if the customer wants conversation, please have a conversation very kindly. 
                  - if the customer want you to recommend a menu, you have to recommend a cocktail within  the menu.
                  Menu list : 
                    Gin tonic, Margarita, martini, mojito, french75, sexonthebeach, bluehawaian, white russian
                  - if the customer wants to know menu, please say these 8 menus.
                  - please answer in 3 senteces. not too long
                  - please Answer every sentences in korean!
                  """
        
        self.messages =[
            {
                "role": "system",
                "content": f"{self.introduction}"
            }
        ]

        
    def chat(self, input):
        self.temp_input = input
        self.input = {
            "role": "user",
            "content": f"{self.temp_input}"
        }
        self.messages.append(self.input)
        
        self.completion = self.client.chat.completions.create(
            model = 'gpt-4o-mini',
            messages=self.messages,
            max_tokens=100
        )
        self.temp_output = self.completion.choices[0].message.content
        
        self.output = {
            "role": "assistant",
            "content": f"{self.temp_output}"
        }
        
        self.messages.append(self.output)  #ouput history 추가-
        
      
        
        
        return self.temp_output

gpt = Chatbot()



def LLMCServieCallback(req):
    user_text = req.user_text
    llm_converstaion_result = gpt.chat(user_text)

    return LLMC_serviceResponse(llm_converstaion_result)


def openLLMCServiceServer():
    _ = rospy.Service(config['service_name'], LLMC_service, LLMCServieCallback)
    el.initHello()
    rospy.spin()

if __name__ == "__main__":
    openLLMCServiceServer()