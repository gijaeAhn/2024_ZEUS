import os


class HRIConfig():
    menu_wordset = ["진토닉", "마가리타", "마티니", "모히또", "프렌치75", "프렌치 75", "섹스온더비치"]
    # recommand_wordset= ["추천"]
    order_wordset = ["메뉴 준비해 드리겠습니다", "준비해 드리겠습니다"]

    positive_wordset = ['좋아', '맞아' ,'맞']
    negative_wordset = ['싫어', '아니야', '아니']

    greeting_image_path = "/home/sjlab3090/.temp_files/captured_img.png"


if __name__ == "__main__":
    print(HRIConfig.greeting_image_path)