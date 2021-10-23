from tljh.hooks import hookimpl
import os, traceback, shutil

@hookimpl
def tljh_new_user_create(username):
    f = open("/etc/passwd")
    for row in f.readlines():
        if username in row:
            pid, path = row.strip().split("::")
            path = path.split("/")[1]
            break
    home = f"/{path}/{username}"
    os.system(f"echo NEW USER: {username} HOME: {home} >> tljh-new-user.log")
    if os.path.isdir('new_user_data'):
        os.system(f"echo ' ' copying new_user_data >> tljh-new-user.log")
        err = None
        try:
            shutil.copytree("new_user_data", home, dirs_exist_ok=True)
        except:
            f=open("tljh-new-user.log", 'a')
            print (traceback.format_exc(), file=f)
            f.close()
            err = traceback.format_exception_only()
    else:
        os.system(f"echo ' ' no new_user_data directory found, nothing to copy >> tljh-new-user.log")
    os.system(f"echo ' ' returns: {err} >> tljh-new-user.log")
