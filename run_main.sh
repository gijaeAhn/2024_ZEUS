#! /bin/bash
tmux kill-session 
sleep 1

tmux new-session -d
tmux set -g mouse on
tmux split-window -h -p 50
tmux select-pane -L
tmux split-window -v
tmux select-pane -R
tmux split-window -v
tmux select-pane -R
tmux split-window -v

tmux select-pane -t 0
tmux send "roscore" C-m

tmux select-pane -t 1
tmux send "cd ~/Desktop/2024_ZEUS/run" C-m
tmux send "python3 zeus_pcSide_control.py" C-m

tmux select-pane -t 2
tmux send "ssh i611usr@192.168.0.23" C-m
sleep 1
tmux send "i611" C-m
tmux send "python zeus_robotSide_control.py"

tmux select-pane -t 3
tmux send "cd ~/Desktop/2024_ZEUS" C-m
tmux send "python3 main_client.py"

tmux select-pane -t 4
tmux send "cd ~/Desktop/2024_ZEUS/Tools" C-m
tmux send "python3 positionLoggerReal.py"
