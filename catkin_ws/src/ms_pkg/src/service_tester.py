import rospy
from ms_pkg.srv import Greeting_service, Greeting_serviceResponse
from ms_pkg.srv import IC_service




if __name__ == "__main__":
    # GreetingServicerq = rospy.ServiceProxy("GreetingService", Greeting_service)

    # image_path = "/home/sjlab3090/Desktop/2024_ZEUS/media/face/listen.jpg"
    # user_text =  "이 이미지에 대해 설명해줘"
    # result = GreetingServicerq("inference", image_path, user_text).chat_result
    # print(result)
    # result = GreetingServicerq("inference", image_path, "이 이미지랑 다른점은?").chat_result
    # print(result)


    # history = GreetingServicerq("history", "", "").history
    # print(history)

    ICServicerq = rospy.ServiceProxy("ICService", IC_service)
    a = ICServicerq().result