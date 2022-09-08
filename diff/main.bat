@echo off
echo ----------- Agent Chatting Program ------------

for /f "delims=[] tokens=2" %%a in ('ping -4 -n 1 %ComputerName% ^| findstr [') do set ADDR1=%%a
echo Your IP address: %ADDR1%

set /p PORT1="Enter Local Agent Port Number: "
set /a PORT1R= %PORT1% + 1

echo ------

set /p ADDR2="Enter Remote Agent IP Address: "
set /p PORT2="Enter Remote Agent Port Number: "
set /a PORT2R= %PORT2% + 1

echo ------

echo Starting Your Local Agent...
echo Sending from %ADDR1%:%PORT1%
echo Sending to %ADDR2%:%PORT2R%
echo Receiving to %ADDR1%:%PORT1R%

start cmd /k python3 diff.py -s %ADDR1% %PORT1% %ADDR2% %PORT2R%
start cmd /k python3 diff.py -r %ADDR1% %PORT1R%
