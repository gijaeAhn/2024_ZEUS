// ------------------------------- //
// ------------------------------- //
// ------------------------------- //

// WEBOTS INCLUDE //
#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/PositionSensor.hpp>
// -------------- //

// ROS INCLUDE //
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>


// STD INCLUDE // 
#include <iostream>
#include <chrono>
#include <math.h>
#include <array>
#include <map>
#include <memory>
// ------------- //


#define TIME_STEP       32
#define DOF             6
#define NEAR_VALUE      1e-6



class zeusController : public webots::Robot {

    public :

        zeusController() : Robot(){
            int argc = 0;
            char** argv = nullptr;
            double jointSpeed = 2.0;
            ros::init(argc, argv, "zeus_controller");
            nhPtr_ =  std::make_shared<ros::NodeHandle>();
            commandSub_   = nhPtr_->subscribe("/zeus/webots/jointCommand",1000, &zeusController::jointStateCallback, this);
            realJointPub_ = nhPtr_->advertise<sensor_msgs::JointState>("/zeus_states",1000); 

            motors_[0] = std::shared_ptr<webots::Motor>(getMotor("joint1"), [](webots::Motor*){});
            motors_[1] = std::shared_ptr<webots::Motor>(getMotor("joint2"), [](webots::Motor*){});
            motors_[2] = std::shared_ptr<webots::Motor>(getMotor("joint3"), [](webots::Motor*){});
            motors_[3] = std::shared_ptr<webots::Motor>(getMotor("joint4"), [](webots::Motor*){});
            motors_[4] = std::shared_ptr<webots::Motor>(getMotor("joint5"), [](webots::Motor*){});
            motors_[5] = std::shared_ptr<webots::Motor>(getMotor("joint6"), [](webots::Motor*){});

            positionSensors_[0] = std::shared_ptr<webots::PositionSensor>(getPositionSensor("joint1Sensor"), [](webots::PositionSensor*){});
            positionSensors_[1] = std::shared_ptr<webots::PositionSensor>(getPositionSensor("joint2Sensor"), [](webots::PositionSensor*){});
            positionSensors_[2] = std::shared_ptr<webots::PositionSensor>(getPositionSensor("joint3Sensor"), [](webots::PositionSensor*){});
            positionSensors_[3] = std::shared_ptr<webots::PositionSensor>(getPositionSensor("joint4Sensor"), [](webots::PositionSensor*){});
            positionSensors_[4] = std::shared_ptr<webots::PositionSensor>(getPositionSensor("joint5Sensor"), [](webots::PositionSensor*){});
            positionSensors_[5] = std::shared_ptr<webots::PositionSensor>(getPositionSensor("joint6Sensor"), [](webots::PositionSensor*){});

            for (int i = 0; i < 6; ++i) {
            positionSensors_[i]->enable(TIME_STEP);
            motors_[i]->setVelocity(jointSpeed);
            }
        }

        
        void run() {
            // Ensure TIME_STEP is defined correctly, it should match the WorldInfo basicTimeStep
            if (TIME_STEP <= 0) {
                ROS_ERROR("Invalid TIME_STEP defined. It must be a positive integer.");
                return;
            }

            while (true) {
                int timeStepResult = webots::Robot::step(TIME_STEP);
                if (timeStepResult == -1) {
                    ROS_ERROR("Simulation has stopped or an error occurred.");
                    break;
                }

                ros::spinOnce(); // Handle ROS events
                webotsControlFunc(); // Your control function
            }
        } 
            
        

    private :

        

        // ROS SIDE //
        std::shared_ptr<ros::NodeHandle>      nhPtr_;
        ros::Subscriber                       commandSub_;
        ros::Publisher                        realJointPub_;


        // WEBOTS SIDE //
        
        std::shared_ptr<webots::Motor>          motors_[6];
        std::shared_ptr<webots::PositionSensor> positionSensors_[6];

        // MEMORY SIDE //
        std::array<double,DOF> motorGoal_;
        std::array<double,DOF> sensorPosition_;
        std::array<double,DOF> motorGoalPrev_; 


        void jointStateCallback(const sensor_msgs::JointState::ConstPtr& msg){

            for(size_t i = 0; i < msg->name.size() ; i++){
            ROS_INFO("Succeed to recieve joint states :");
            // ROS_INFO("Joint : %s, Position : %f, Velocity : %f , Effort : %f"  , msg->name[i].c_str()
            //                                                                    , msg->position[i]
            //                                                                    , msg->velocity[i]
            //                                                                    , msg->effort[i]);
            // Update Goal Position                                                                
            motorGoal_[i] = msg->position[i];
            }       
        }

        void webotsControlFunc(){

            sensor_msgs::JointState realJointMsg;
            realJointMsg.header.stamp = ros::Time::now();
            // Read Current Position
            for(size_t i = 0; i < DOF ; ++i){
                sensorPosition_[i] = positionSensors_[i]->getValue();
                realJointMsg.name.push_back("joint" + std::to_string(i));
                realJointMsg.position.push_back(sensorPosition_[i]);
            }
            realJointPub_.publish(realJointMsg);

            // Compare Current position and previous command
            
            bool positionCheck = true;
            for(size_t i = 0; i < DOF ; i++){
                if(std::abs(sensorPosition_[i] - motorGoalPrev_[i]) > NEAR_VALUE){
                    positionCheck = false;
                }
            }
            if( positionCheck){
            ROS_INFO("ROBOT CAN NOT REACH THE GOAL POSITION");
            }


            // Set webots model position
            for(size_t i = 0 ; i < DOF ; i++){
                motors_[i]->setPosition(motorGoal_[i]);
            }

            // Update the previous goal to the current goal
            for (size_t i = 0; i < DOF; ++i) {
                motorGoalPrev_[i] = motorGoal_[i];
            } 
        }


};


int main(int argc, char **argv){
    zeusController controller;
    controller.run();
    return 0;
}




