import csv
with open('c:\\users\\dchanna\\desktop\\test.csv','r', newline='') as csvfile:
    
    csvdicreader=csv.DictReader(csvfile) #reading values via Dictionary
   
    #logic to traverse through the items in the csv
    for i,row in enumerate(csvdicreader):
        print(row)
        if(i>=2):
            break
    csvdata=csv.reader(csvfile)  #reading values via list
    #logic to traverse through the items in the csv
    while True:
        try:
            rowdata=next(csvdata)
            print(rowdata)
        except StopIteration:
            break