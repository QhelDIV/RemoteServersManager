import sys, paramiko
from UserCreater import *
from config import *
from remoteControl import *

remoteController = RemoteControl(UserCreater)
for newUserInfo in newUserInfos:
    newuser = newUserInfo[0]
    newpass = newUserInfo[1]
    remoteController.run(args=(newuser,newpass))

