from tljh.hooks import hookimpl
import os

@hookimpl
def tljh_new_user_create(username):
    print ("CB_NEW_USER")
    os.system("touch foofoo")