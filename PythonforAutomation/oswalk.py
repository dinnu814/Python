import os
path="C:\\Users\\dchanna\\Documents\\Learning\\Python\\pythonforautomation"
#print(list(os.walk(path)))

for fpath,adir,files in os.walk(path):
    if len(adir) !=0:
        if len(files) !=0:
            #print(fpath,adir,files)
            for eachfile in files:
                print(os.path.join(fpath,eachfile))
                print("**************************")
    #print(adir)
    #print(files)