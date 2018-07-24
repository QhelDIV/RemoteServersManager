import sys, paramiko
from UserCreater import *
from config import *
from remoteControl import *

command = "ls"

port = 22
def apiWraper(api):
    def wraped(arg):
        stdin, stdout, stderr = api(arg)
        print(stdout.read().decode('utf'))
        print(stderr.read().decode('utf'))
    return wraped
remoteController = RemoteControl(UserCreater)
for newUserInfo in newUserInfos:
    newuser = newUserInfo[0]
    newpass = newUserInfo[1]
    remoteController.run(args=(newuser,newpass))

