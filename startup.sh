#!/bin/sh
iphostname=$(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
tmux new -d -s pythonsession
tmux send-keys -t pythonsession "python3 /Python-Http/lmao.py $iphostname" ENTER
/bin/bash