#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.126.com"
mail_user = "shiguofu2012@126.com"
mail_pass = "pass"

local_host = "mail.bainainfo.com"
local_user = "gfshi@baina.com"
local_pass = "pass"

local_send = "gfshi@baina.com"
receivers = "shiguofu2012@126.com"

sender = "shiguofu2012@126.com"
receivers = ['738960197@qq.com']

message = MIMEText('python text ...', 'plain', 'utf-8')
message['From'] = Header('cainiao jiaocheng', 'utf-8')
message['To'] = Header("ceshi", 'utf-8')

subject = 'python text ...'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(local_host, 587)
    smtpObj.starttls()
    print smtpObj.login(local_user, local_pass)
    smtpObj.sendmail(local_send, receivers, message.as_string())
except smtplib.SMTPException as e:
    print "error"
    print e
#try:
#    smtpObj = smtplib.SMTP()
#    smtpObj.connect(mail_host, 25)
#    smtpObj.login(mail_user,mail_pass)
#    smtpObj.sendmail(sender, receivers, message.as_string())
#    print "ok"
#except smtplib.SMTPException as e:
#    print e
