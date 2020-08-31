import os
import datetime
req_path=input("enter your path: ")
if not os.path.exists(req_path):
    print("please provide valid path")
if os.path.isfile(req_path):
    print("Please enter a valid directory")
today=datetime.datetime.now()
print(today)
age=input("enter the older no of files to be deleted: ")
for eachfile in os.listdir(req_path):
    full_path=os.path.join(req_path,eachfile)
    if os.path.isfile(full_path):
        file_creattion_date=datetime.datetime.fromtimestamp(os.path.getctime(full_path))
        diff=(today-file_creattion_date).days
        if int(diff)<int(age):
            print(f'{full_path} is older than {diff} days and {os.remove(full_path)} is deleted')
            
        