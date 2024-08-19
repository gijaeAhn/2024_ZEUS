/*
 * Copyright 1996-2022 Cyberbotics Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// #include "/usr/local/webots/include/controller/c/webots/distance_sensor.h"
// #include "/usr/local/webots/include/controller/c/webots/motor.h"
// #include "/usr/local/webots/include/controller/c/webots/position_sensor.h"
// #include "/usr/local/webots/include/controller/c/webots/robot.h"

#include <stdio.h>
#include <unistd.h>

#include <webots/distance_sensor.h>
#include <webots/motor.h>
#include <webots/position_sensor.h>
#include <webots/robot.h>



#define TIME_STEP 1000
 

enum State { WAITING, GRASPING, ROTATING, RELEASING, ROTATING_BACK };

int main(int argc, char **argv) {
  wb_robot_init();
  int  i = 0;
  // const double target_positions1[6] = {PI,0,0,0,0,0};
  // const double target_positions2[6] = {-PI,0,0,0,0,0};
  
  // const double target_positions1[6] = {0,PI,0,0,0,0};
  // const double target_positions2[6] = {0,-PI,0,0,0,0};
   
  // const double target_positions1[6] = {0,0,0,0,0,0};
  // const double target_positions2[6] = {0,0,0,0,0,0};
  
  // const double target_positions1[6] = {0,0,0,PI,0,0};
  // const double target_positions2[6] = {0,0,0,-PI,0,0};

  // const double target_positions1[6] = {0,0,0,0,1,0};
  // const double target_positions2[6] = {0,0,0,0,-1,0};
  
  // const double target_positions1[6] = {0,0,0,0,0,PI};
  // const double target_positions2[6] = {0,0,0,0,0,-PI};

  const double target_positions1[6] = {1,1,1,1,1,1};
  const double target_positions2[6] = {-1,-1,-1,-1,-1,-1};

  double speed = 1.0;


  WbDeviceTag zeus_motors[6];

  zeus_motors[0] = wb_robot_get_device("joint1");
  zeus_motors[1] = wb_robot_get_device("joint2");
  zeus_motors[2] = wb_robot_get_device("joint3");
  zeus_motors[3] = wb_robot_get_device("joint4");
  zeus_motors[4] = wb_robot_get_device("joint5");
  zeus_motors[5] = wb_robot_get_device("joint6");

  for (i = 0; i < 6; ++i)
    wb_motor_set_velocity(zeus_motors[i], speed);

  int setValue = 0;

  while (wb_robot_step(TIME_STEP) != -1) {
  	if(setValue ==0){
	  for(i = 0; i < 6; ++i){
		wb_motor_set_position(zeus_motors[i],target_positions1[i]);
		printf("Moving 1");
	  }
	  setValue = 1;
	  sleep(1);
	}else{
	  for(i = 0; i < 6; ++i){
		wb_motor_set_position(zeus_motors[i],target_positions2[i]);
		printf("Moving 2");
	  }
	  setValue = 0;
	  sleep(1);	  
	}
  };
  wb_robot_cleanup();
  return 0;
}
