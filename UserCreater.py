import os
class Executer:
    def __init__(self,api=os.system):
        self.api = api
class UserCreater(Executer):
        def __init__(self, api=os.system):
            super().__init__(api)
        def run(self,username, password, newuser, newpass):
                # For safty, forbid bash history to record any command contains sudo -S
                self.api('export HISTIGNORE="*sudo -S*"')

                self.api('echo "{0}" | sudo -S adduser --quiet --disabled-password --shell /bin/bash --home /home/{1} --gecos "User" {1}'.format(password,newuser))

                # set password
                # pass different parameters to different part of the instruction, see the link below for detail
                # https://unix.stackexchange.com/questions/391796/pipe-password-to-sudo-and-other-data-to-sudoed-command
                self.api('echo "{1}:{2}" | {{ echo "{0}"; cat -; }} | sudo -S chpasswd'.format(password,newuser,newpass))
                # add the new user to sudo group
                self.api('echo "{0}" | sudo -S adduser --quiet {1} sudo'.format(password,newuser))

                # add xrdp config file
                self.api('echo "xfce4-session" | {{ echo "{0}"; cat -; }} | sudo -S tee /home/{1}/.xsession'.format(password,newuser))
                self.api('echo "{0}" | sudo -S chown {1}:{1} /home/{1}/.xsession'.format(password,newuser))


