@echo off
echo ----------- Agent Chatting Program ------------

echo ------

set /p PORT1="Enter Agent 1 Port Number: "
set /a PORT1R= %PORT1% + 1

echo ------

echo Enter Agent 2 Port Number
set /p PORT2="(Neither %PORT1% nor %PORT1R%): "
set /a PORT2R= %PORT2% + 1

echo ------

echo Starting Agent 1...
echo Sender PORT: %PORT1%
echo Receiver PORT: %PORT2R%

start cmd /k python3 same.py -s %PORT1% %PORT2R%
start cmd /k python3 same.py -r %PORT1R%

pause
echo ------

echo Starting Agent 2....
echo Sender PORT: %PORT2%
echo Receiver PORT: %PORT1R%

start cmd /k python3 same.py -s %PORT2% %PORT1R%
start cmd /k python3 same.py -r %PORT2R%