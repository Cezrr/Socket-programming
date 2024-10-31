@echo off
start cmd /k "cd /d C:\gitProjects\Socket programming\SocketProgrammingScripts && python socketServer.py" 
echo Starting both scripts in 3 seconds...

timeout /t 3 /nobreak >nul

start cmd /k "cd /d C:\gitProjects\Socket programming\SocketProgrammingScripts && python socketClient.py"
start cmd /k "cd /d C:\gitProjects\Socket programming\SocketProgrammingScripts && python socketClient2.py"