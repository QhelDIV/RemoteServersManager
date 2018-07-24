from UserCreater import *
from config_local import *

if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(description='create user in GPU server of VCC@SZU')
        parser.add_argument('-u',help="username")
        parser.add_argument('-p',help="password")
        args = parser.parse_args()
        if args.u is None or args.p is None:
            print("No usrename or password given")
        else:
            userCreater = UserCreater(os.system)
            userCreater.run(username, password, args.u ,args.p)

