#!/bin/bash
tmux kill-session 
sleep 1

tmux new-session -d
tmux set -g mouse on
tmux split-window -h -p 50
tmux select-pane -L
tmux split-window -v
tmux select-pane -R
tmux split-window -v
# tmux select-pane -R
# tmux split-window -v

tmux select-pane -t 0
tmux send-keys "roscore" C-m

tmux select-pane -t 1
tmux send-keys "cd ~/Desktop/2024_ZEUS/run" C-m
tmux send-keys "python3 zeus_pcSide_control.py" C-m

tmux select-pane -t 2
tmux send-keys "ssh i611usr@192.168.0.23" C-m
sleep 1
tmux send-keys "i611" C-m
tmux send-keys "python zeus_robotSide_control.py" C-m

tmux select-pane -t 3
tmux send-keys "cd ~/Desktop/2024_ZEUS" C-m
tmux send-keys "python3 main_client.py" C-m

tmux select-pane -t 4
tmux send-keys "cd ~/Desktop/2024_ZEUS/tools" C-m
tmux send-keys "python3 positionLoggerReal.py" C-m

tmux select-pane -t 4
tmux split-window -v
tmux select-pane -t 5
tmux send-keys "cd ~/Desktop/2024_ZEUS/run" C-m
tmux send-keys "python3 shakerDyna.py" C-m


# tmux select-pane -t 4
# tmux split-window -v
# tmux select-pane -t 6
# tmux send-keys "echo 'Pane 6: Additional commands can be run here'" C-m

tmux attach-session
