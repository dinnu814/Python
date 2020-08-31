#copying file content to another file 
sfile="C:\\Users\\dchanna\\Documents\\Projects\\ProdEngineering_JIRALinks.xlsx"
dfile="C:\\Users\\dchanna\\Documents\\dest.txt"
sfo=open(sfile,'r')
content=sfo.read()
print(content)
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
dfo.close()
