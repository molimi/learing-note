# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230419
# @Version: 1.0
# @Description: Python 发送普通文字邮件

from smtplib import SMTP_SSL
from email.header import Header 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main():
    # 设定邮件发送者和接受者
    host_server = 'smtp.qq.com'             # qq 邮箱smtp服务器
    sender = '2265066536@qq.com'            # 发件人邮箱
    pwd = "xyqidzwjoqaldiji"
    receivers = '19913776628@163.com'      # 收件人邮箱
    mail_title = "Python自动发送的邮件"      # 邮件标题  
    mail_content = "您好，这是使用python登录QQ邮箱发送邮件的测试——xq"   # 邮件正文内容

    message = MIMEMultipart()               # 初始化一个邮件主体
    message['Subject'] = Header(mail_title, 'utf-8')
    message['From'] = sender
    # MIMEText("用Python发送邮件的示例代码.", 'plain', 'utf-8')
    message['To'] = ";".join(receivers)
    message.attach(MIMEText(mail_content, 'plain', 'utf-8'))    # 邮件正文内容

    smtper = SMTP_SSL(host_server)      # ssl登录
    # login(user,password):
    # user:登录邮箱的用户名。
    # password：登录邮箱的密码，这里用的是QQ邮箱，
    # 需要用到客户端密码，需要在QQ邮箱中设置授权码，该授权码即为客户端密码
    smtper.login(sender, pwd)
    smtper.sendmail(sender, receivers, message.as_bytes())
    print("邮件发送完成!")
    # quit(): 用于结束SMTP会话
    smtper.quit()

if __name__ == '__main__':
    main()