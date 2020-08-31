import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname='54.235.227.102',username='ec2-user',password='',port=22)
ssh.connect(hostname='54.235.227.102',username='ec2-user',key_filename='',port=22)
stdin, stdout, stderr=ssh.exec_command("uptime")
print("The output is : " ,stdout.read())
ssh.close()