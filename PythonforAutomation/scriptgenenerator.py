#version 1.0
#Author dchanna
#Python script for inserting bulk permissions into the database
import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};'
                      'Server=aaa-ffsqldev01.prod.factset.com;'
                      'Database=ff_icons;'
                      'UID=dochist_admin_stage;'
                      'PWD=gDng7TbdfvAqB73F;'
                      )
cursor = conn.cursor()
emp_id=input("enter user employee id: ")
first=cursor.execute(f'SELECT id FROM dbo.attr_user_master where factset_id in ({emp_id})')
eid=first.fetchall()
permissionskeys=input("enter the required permissions: " )
second=cursor.execute(f"SELECT id FROM dbo.attr_wf_permission where mnemo in ({permissionskeys})")
pid=second.fetchall()
if len(eid)>0:
    for empid in eid:
        if len(pid)>0:
            for permid in pid:
                print(f"insert into wf_link_user_permission values ({empid.id},{permid.id})")
                #cursor.execute(f"insert into wf_link_user_permission values ({empid.id},{permid.id})")
                #conn.commit()
        else:
            print("Permission keyword not exists in the database,please enter a valid permission keyword")
else:
    print("Emploees does not exists in the databases,please enter a valid employee id")
conn.close()