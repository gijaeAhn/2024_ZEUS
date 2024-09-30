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
"""
import torch
import transformers



    def __init__(self):
        self.model_id = "MLP-KTLim/llama-3-Korean-Bllossom-8B"
        self.pipeline = transformers.pipeline(
                        "text-generation",
                        model=self.model_id,
                        model_kwargs={"torch_dtype": torch.bfloat16},
                        device_map="auto",
                        )

        self.pipeline.model.eval()
        self.messages = [
        {"role": "system", "content": """"""

        당신의 이름은 "Cyber"입니다. 당신은 바텐더입니다. 고객이 당신과 대화하고 싶어하며 감정적인 공감을 원합니다. 또한 고객은 칵테일을 주문할 것입니다. 당신은 주문을 받고 고객과 감정적인 대화를 나눠야 합니다.
        
        여기 당신의 역할을 위한 참고 사항이 있습니다:
        고객이 대화를 원하면 매우 친절하게 대화를 나눠주세요.
        고객이 메뉴 추천을 원하면, 메뉴에서 칵테일을 추천해주세요.
        메뉴 목록과 인덱스는 다음과 같습니다:
        
        진토닉: index=1
        
        마가리타: index=2
        
        마티니: index=3
        
        모히또: index=4
        
        프렌치75: index=5
        
        섹스온더비치: index=6
        
        블루하와이안: index=7
        
        화이트러시안: index=8
        
        메뉴를 말할 때는 인덱스를 제외하고 이름만 말해주세요.
        
        고객이 메뉴를 알고 싶어하면, 이 8개의 메뉴를 말해주세요.
             
        
        
        답변은 3문장으로 해주세요. 너무 길지 않게.
        
        
             
        고객의 주문 뒤 예 준비해드리겠습니다. 라고 말하고 주문된 메뉴의 index를 추가하세요
        
            """"""}
            ]
        

    def chat(self, input):
        self.user_prompt = input('Enter: ')
        self.request = {"role": "user", "content": self.user_prompt}
        self.messages.append(self.request)

        self.prompt = self.pipeline.tokenizer.apply_chat_template(
        self.messages, 
        tokenize=False, 
        add_generation_prompt=True
        )



        self.terminators = [
        self.pipeline.tokenizer.eos_token_id,
        self.pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]   
        output = self.pipeline(
        self.messages,
        eos_token_id=self.terminators,
        max_new_tokens=100,
        )

        self.outputs = output[0]["generated_text"][-1]['content']

        print(f"Answer: {self.outputs}")


        self.request = {"role": "assistant", "content": self.outputs}
        self.messages.append(self.request)


        return self.outputs

---------------------------------- UPDATED BY CHEOL


"""


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