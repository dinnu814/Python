import csv
with open('c:\\users\\dchanna\\desktop\\test.csv','w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name','age']
    names=[{'first_name': 'Baked', 'last_name': 'Beans','age':'25'},{'first_name': 'Lovely', 'last_name': 'Spam','age':'25'},{'first_name': 'Wonderful', 'last_name': 'Spam','age':'25'}]
    writer = csv.DictWriter(csvfile, fieldnames=list(names[0].keys()))
    writer.writeheader()
    writer.writerows(names)
    csvfile.close()
    
