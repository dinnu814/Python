import os
path=input("enter path: ")
filesanddir=os.listdir(path)
files=()
dire=()
#print(filesanddir)
count=0
for each in filesanddir:
    fullpath=os.path.join(path,each)
    if os.path.isfile(fullpath):
        print(f'{fullpath} is a file')
        
    else:
        print(f'{fullpath} is a directory')
