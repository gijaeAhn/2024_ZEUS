import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))

import rospy
from ms_pkg.srv import LLMC_service, LLMC_serviceResponse
from custom_utils import EasyLogger as EL

import transformers
import torch

node_name = "LLMCServiceServerNode"
rospy.init_node(node_name)
config = {}
config['prompt'] = rospy.get_param("~sys_prompt", default='')
config['service_name'] = rospy.get_param("~service_name", default="LLMCService")
el = EL(node_name, config)


model_id = "MLP-KTLim/llama-3-Korean-Bllossom-8B"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.float16},
    device_map="auto",
)

pipeline.model.eval()



def LLMCServieCallback(req):
    messages = [
        {"role": "system", "content": f"{config['prompt']}"},
        {"role": "user", "content": f"{req.user_text}"}
    ]

    prompt = pipeline.tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True
        )

    terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = pipeline(
        prompt,
        max_new_tokens=2048,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9
    )

    llm_answer = outputs[0]["generated_text"][len(prompt):]
    return LLMC_serviceResponse(llm_answer)


def openLLMCServiceServer():
    _ = rospy.Service(config['service_name'], LLMC_service, LLMCServieCallback)
    el.initHello()
    rospy.spin()

if __name__ == "__main__":
    openLLMCServiceServer()