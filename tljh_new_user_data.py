from tljh.hooks import hookimpl
import os
import sys

class Loggit:
    def __init__(self, path, prefix):
        self.path = path
        self.prefix = prefix
        try:
            f = open(self.path, 'a+')
            f.write(f"~~~{self.prefix}~~~" + "\n")
            f.close()
        except:
            print ("Loggit failed, disabling")
            self.path = None

    def log(self, *args):
        s = f"{self.prefix}|" + " ".join([f"{a}" for a in args])
        if self.path:
            f = open(self.path, 'a+')
            f.write(s + "\n")
            f.close()
        print (s)
        sys.stdout.flush()

logg = Loggit("/opt/tljh/state/debug.log", "tnuc2").log

@hookimpl
def tljh_new_user_create(username):
    logg(f"tljh_new_user_create({username})")
    f = open("/etc/passwd")
    for row in f.readlines():
        if username in row:
            pid, path = row.strip().split("::")
            path = path.split("/")[1]
            break
    home = f"/{path}/{username}"
    os.system(f"echo NEW USER: {username} HOME: {home} >> cb_new_user.log")
    os.chdir(home)
    os.system("touch foobaz")
