import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname='54.235.227.102',username='ec2-user',password='',port=22)
ssh.connect(hostname='54.235.227.102',username='ec2-user',key_filename='C:\\Users\\dchanna\\Documents\\Learning\\Ansible\\Ansible.pem',port=22)
sftp_client=ssh.open_sftp()
sftp_client.get('/home/ec2-user/paramiko_downloaded_file.txt','C:\\Users\\dchanna\\Documents\\Learning\\python\\paramiko_downloaded_file.txt')
sftp_client.put('C:\\Users\\dchanna\\Documents\\Learning\\python\\paramiko_downloaded_file.txt','/home/ec2-user/paramiko_downloaded_file.txt')
ssh.close()