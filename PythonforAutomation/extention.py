import os
rpath=input("Enter your directory: ")
if os.path.isfile(rpath):
    print(f'the given {rpath} is a file. Please pass directory only')
else:
    listdire=os.listdir(rpath)
    if len(listdire)>0:
        ext=input("Required files extention .py/.sh/.bat/.log/.txt: ")
        allfiles=[]
        for eachfile in listdire:
            if eachfile.endswith(ext):
                allfiles.append(eachfile)
        if len(allfiles)>0:
            print(f'The directory consists of {len(allfiles)} number of matching files out of {len(listdire)} and the files are {allfiles}')
          
        else:
            print(f'no matching files with extention {ext} in the location {rpath}')
    else:
        print("directory is empty, please provide the directory which consiste of files")
        
    