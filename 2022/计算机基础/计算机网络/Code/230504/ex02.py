# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230419
# @Version: 1.0
# @Description: Python 发送HTML格式邮件

import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

host_server = "smtp.qq.com"             # qq邮箱smtp服务器
sender_qq = "2265066536@qq.com"         # 发件人邮箱
password = "xyqidzwjoqaldiji"           # 授权码
receiver = "19913776628@163.com"
mail_title = "Python自动发送html格式的邮件" # 邮件标题
# 邮件正文内容
mail_content = "您好！<p>这是使用python登录QQ邮箱发送\
                HTNL格式邮件的测试：</p> <p>\
                <a href='https://blog.csdn.net/xq151750111?spm=1010.2135.3001.5421'>CSDN个人主页</a></p>"

msg = MIMEMultipart()
msg["Subject"] = Header(mail_title, "utf-8")
msg["From"] = sender_qq
msg["To"] = Header("测试邮箱", "utf-8")

msg.attach(MIMEText(mail_content, 'html'))

try:
    smtp = SMTP_SSL(host_server)    # ssl登录连接到邮件服务器
    smtp.set_debuglevel(True)       # False to disable debug
    smtp.ehlo(host_server)          # 跟服务器打招呼，告诉它我们准备连接
    smtp.login(sender_qq, password)
    smtp.sendmail(sender_qq, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("无法发送邮件")