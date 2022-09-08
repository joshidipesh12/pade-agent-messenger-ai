#!/bin/bash
echo ----------- Agent Chatting Program ------------

# taking port input for localhost
read -p "Enter Agent Port Number: " port
read -p "Enter Receiver Port Number: " r_port

# running sender/receiver in parallel
python3 same.py -r $port &
sleep 3
python3 same.py -s $port $r_port

$SHELL