#!/usr/bin/env bash

cd catkin_ws || exit

catkin_make

cd build/zeus_controller

mv zeus_controller ../../../webots/controllers/zeus_controller


# Other ROS run files should be moved to run dir
