import yagmail


# 建立发送客户端
sendClient = yagmail.SMTP(user='batterm@163.com',
                          password='good123',
                          host='smtp.163.com')
# 创建邮件正文
contents = [
    'i am a test emil'
]
# 发送邮件并添加附件
sendClient.send(to=['943523023@qq.com'],
                subject='[python]Test email send',
                contents=contents)
                # attachments=['getinfo.py', 'README.md'])