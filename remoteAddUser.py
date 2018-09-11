import sys, paramiko
from UserCreater import *
import config
from remoteControl import *

remoteController = RemoteControl(UserCreater)
newUserInfos = config.records
for newUserInfo in newUserInfos:
    print(newUserInfo)
    host = newUserInfo[0]
    newuser = newUserInfo[1]
    newpass = newUserInfo[2]
    remoteController.run(args=(host,newuser,newpass))

