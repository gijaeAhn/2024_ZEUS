import rospy

def main():
    rospy.init_node('my_node')
    param_value = rospy.get_param('~param_name', 5)

    # Launch 파일에서 전달된 인자 읽기
    
    rospy.loginfo(f"Received parameter: {param_value}")
    rospy.spin()

if __name__ == '__main__':
    main()
