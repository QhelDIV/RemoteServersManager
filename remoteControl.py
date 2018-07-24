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
        for hostname in hosts:
            print("Now connecting host: " + hostname)
            print()
            try:
                port = 22
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.WarningPolicy)
                client.connect(hostname, port=port, username=username, password=password)
                # enable sudo for 5 minuts(5 is the default value for sudo)
                stdin, stdout, stderr = client.exec_command("sudo touch ttest", get_pty = True)
                stdin.write(password+"\n")
                stdin.flush()
                for line in stdout:
                    print(line.strip('\n'))
                for line in stderr:
                    print(line.strip('\n'))
                #print(stdout.read().decode('utf'))


                self.operator = self.optclass(api = sshWraper(client.exec_command) )

                if args is None:
                    self.operator.run(username,password)
                else:
                    self.operator.run(username,password,*args)

            finally:
                client.close()

