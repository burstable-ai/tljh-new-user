from tljh.hooks import hookimpl
import os

@hookimpl
def tljh_new_user_create(username):
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
