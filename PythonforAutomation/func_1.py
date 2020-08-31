import os
import time
import platform


def mycode(cmd1,cmd2):
    time.sleep(2)
    os.system(cmd1)
    time.sleep(5)
    os.system(cmd2)
    
if platform.system()=="Windows":
    mycode("cls","dir")
else:
    mycode("clear","ls -lrt")