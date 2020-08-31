import os
print(os.getcwd())
a=input("enter a directory: " )
if os.path.isdir(a):
    os.chdir(a)
    print(os.getcwd())
else:
    print("please enter a valid directory")