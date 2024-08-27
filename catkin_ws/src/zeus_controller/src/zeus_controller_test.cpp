// ROS INCLUDE //
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>


// STD INCLUDE // 
#include <iostream>
#include <chrono>
#include <cmath>
#include <array>
#include <map>
#include <memory>
// ------------- //


class ZeusJointPublisher {
public:
    ZeusJointPublisher() {
        // Initialize the node handle
        nh_ = std::make_shared<ros::NodeHandle>();
        
        // Create a publisher for the JointState messages
        joint_pub_ = nh_->advertise<sensor_msgs::JointState>("/zeus/webots/jointCommand", 1000);
        
        // Set initial state
        current_angle_ = M_PI / 4;
        direction_ = -1;  // This will be used to oscillate the angle
        
        // Create a timer to change the joint state every 2 seconds
        timer_ = nh_->createTimer(ros::Duration(2.0), &ZeusJointPublisher::timerCallback, this);
    }

    void timerCallback(const ros::TimerEvent&) {
  
    sensor_msgs::JointState msg;
    msg.header.stamp = ros::Time::now(); 


    std::vector<std::string> joints = {"joint1", "joint2", "joint3", "joint4", "joint5", "joint6"};
    msg.name.insert(msg.name.end(), joints.begin(), joints.end());

    std::vector<double> positions(6);
    positions[0] = -0.2319595;
    positions[1] =  0.156886;
    positions[2] =  1.77;
    positions[3] =  0.0;
    positions[4] = 1.214719;
    positions[5] = 0.0;


    msg.position.insert(msg.position.end(), positions.begin(), positions.end());

    // Publish the joint state
    joint_pub_.publish(msg);


    current_angle_ += direction_ * 0.1;  

    // Check bounds and reverse direction if necessary
    if (std::abs(current_angle_) > M_PI / 4) {
        direction_ = -direction_;  // Reverse the direction
        current_angle_ = M_PI / 4 * direction_;  // Ensure angle stays within bounds
    }
}

private:
    std::shared_ptr<ros::NodeHandle> nh_;
    ros::Publisher joint_pub_;
    ros::Timer timer_;
    double current_angle_;
    int direction_;  // Direction of angle change
};

int main(int argc, char** argv) {
    ros::init(argc, argv, "zeus_controller_test");

    ZeusJointPublisher zeus_joint_publisher;

    ros::spin();

    return 0;
}