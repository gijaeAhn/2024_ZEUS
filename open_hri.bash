#!/bin/bash
setup_path="./catkin_ws/devel/setup.bash"

# tmux new-session -s roscore_session -d
# tmux send-keys -t roscore_session "source ${setup_path}" C-m
# tmux send-keys -t roscore_session "roscore" C-m

tmux new-session -s hri_dependencies_session -d
tmux send-keys -t hri_dependencies_session "source ${setup_path}" C-m
tmux send-keys -t hri_dependencies_session "roslaunch ms_pkg UserInterface.launch" C-m

tmux new-session -s hri_main_session -d
tmux send-keys -t hri_main_session "source ${setup_path}" C-m
tmux send-keys -t hri_main_session "python ./hri.py" C-m


