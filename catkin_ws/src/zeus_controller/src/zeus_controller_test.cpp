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
        joint_pub_ = nh_->advertise<sensor_msgs::JointState>("/zeus_command", 1000);
        
        // Set initial state
        current_angle_ = M_PI / 4;
        direction_ = -1;  // This will be used to oscillate the angle
        
        // Create a timer to change the joint state every 2 seconds
        timer_ = nh_->createTimer(ros::Duration(2.0), &ZeusJointPublisher::timerCallback, this);
    }

    void timerCallback(const ros::TimerEvent&) {
        // Prepare the JointState message
        sensor_msgs::JointState msg;
        msg.header.stamp = ros::Time::now();
        msg.name.push_back("joint1");  // Adjust the joint name as needed
        msg.position.push_back(current_angle_);
        
        // Publish the joint state
        joint_pub_.publish(msg);
        
        // Update the angle for next time
        current_angle_ *= direction_;
        if (std::abs(current_angle_) > M_PI / 4) {
            direction_ *= -1;  // Change the direction
            current_angle_ = M_PI / 4 * direction_;
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