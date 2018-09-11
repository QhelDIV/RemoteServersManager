import sys, paramiko
from config import *

def sshWraper(api):
    def wraped(arg):
        stdin, stdout, stderr = api(arg,get_pty=True)
        print(stdout.read().decode('utf'))
        print(stderr.read().decode('utf'))
    return wraped

class RemoteControl:
    def __init__(self, operatorCLS):
        self.optclass = operatorCLS
    def run(self, args = None):
        if args is None:
            print("NO INPUT!!")
            return
        if len(args) < 2:
            print("TOO FEW ARGUMENTS!!")
        hostname = args[0]
        print("Now connecting host: " + hostname)
        try:
            port = 22
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy)
            client.connect(hostname, port=port, username=username, password=password)

            self.operator = self.optclass(api = sshWraper(client.exec_command) )

            if args is None:
                self.operator.run(username,password)
            else:
                self.operator.run(username,password,*args)
            print("Operation Finished.")

        finally:
            client.close()


