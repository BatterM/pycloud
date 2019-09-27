import paramiko

transport=paramiko.Transport(('192.168.132.10',22))
# private=paramiko.RSAKey.from_private_key_file('c:\\Users\WL\.ssh\id_rsa')
# transport.connect(username='root',pkey=private)
transport.connect(username='root',password='123!@#')
sftp=paramiko.SFTPClient.from_transport(transport)
# sftp.put(localpath='e:\\pycloud\monitor.tar',remotepath='/root/monitor.tar')
# sftp.put(localpath='e:\\pycloud\\test_request.py',remotepath='/root/test_request.py')
# sftp.put(localpath='e:\\pycloud\\main_monitor.py',remotepath='/root/main_monitor.py')
sftp.put(localpath='e:\\pycloud\\test\\三吉彩花.jpg',remotepath='/root/三吉彩花.jpg')
transport.close()