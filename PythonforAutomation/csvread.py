import csv
req_file="C:\\Users\\dchanna\\Documents\\Dinesh\\Official\\Estimates\\folderList.csv"
fo=open(req_file,'r')
csvread=csv.reader(fo,delimiter=";")
#content=fo.readlines()
for each in csvread:
    print(each)
fo.close()