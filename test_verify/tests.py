from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:34:10 2020

@author: hp
"""
import datetime
from twilio.rest import Client
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import random
import json


def get_current_time():
    current_time = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
    return current_time


def randomse():
    str = ""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    return str


def Mobileauthentication(mobile_authentication):
    account_sid = 'AC9acf442cc1818ff4f8ba0eb47a7a1ca7'
    auth_token = '17011422662ac6f51485515991a04841'
    try:
        se = str(randomse())
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+86" + str(mobile_authentication),  # 接受短信的手机号，也就是注册界面验证过的那个自己的手机号，注意 写中国区号  +86
            from_="+12622879319",  # 发送短信的美国手机号  区号 +1
            body="【Born To Win】您的验证码为：" + se + " （5分钟内有效），为了保证您的账户安全，请勿向任何人提供此验证码。感谢您使用Born To Win")
        # 打印发送结果
        t = {}
        t['captcha'] = int(se)
        t['code'] = 1
        t['time'] = get_current_time()
        return t
        # return json.dumps(t, ensure_ascii=False)
    except BaseException as e:
        g = {}
        g['code'] = 0
        return g
        # return json.dumps(g, ensure_ascii=False)


def Emailauthentication(postbox):
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "zzjw527@163.com"  # 用户名
    mail_pass = "FBBUWAVMRDHYSNZC"  # 授权密码，非登录密码

    sender = 'zzjw527@163.com'  # 发件人邮箱(最好写全, 不然会失败)
    postbox = str(postbox)
    receivers = [postbox]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    #    receivers = ['1259648270@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    se = str(randomse())
    content = "亲爱的Born To Win用户：您好！\n" + "您收到这封这封电子邮件是因为您 (也可能是某人冒充您的名义) 申请了修改账号密码。假如这不是您本人所申请, 请不用理会这封电子邮件, 但是如果您持续收到这类的信件骚扰, 请您尽快联络网站管理员。\n" + "请使用以下验证码完成后续修改密码流程\n\n" + se + "\n\n注意:请您在收到邮件10分钟内使用，否则该验证码将会失效。\n"

    title = '【Born To Win】修改账号密码'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
        t = {}
        t['captcha'] = int(se)
        t['code'] = 1
        t['time'] = get_current_time()
        return t
        # return json.dumps(t, ensure_ascii=False)
    except smtplib.SMTPException as e:
        g = {}
        g['code'] = 0
        # return json.dumps(g, ensure_ascii=False)
        return g

def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
    email_client.quit()

# if __name__ == '__main__':
#    gg=get_current_time()
#    print(gg)
##    Emailauthentication('1259648270@qq.com')
##    Mobileauthentication(19927466621)

