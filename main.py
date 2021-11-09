import smtplib
from HTMLTestRunner import HTMLTestRunner
import unittest
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

test = unittest.defaultTestLoader.discover(r'C:\Users\Knight-YF\PycharmProjects\pythonProject\ST\keceng\day13', pattern='Test*.py')

runner = HTMLTestRunner.HTMLTestRunner(
    title='计算机测试报告',
    description='测试报告',
    verbosity=1,
    stream=open(file='计算机.html', mode='w+',encoding="utf-8")

)

runner.run(test)

# 发送邮件的服务器
smtpserver = 'smtp.qq.com'

# 发送邮件用户和密码
user = "957515856@qq.com"
password = "rlqtovxsujvgbfaa"

# 发送者
sender = "957515856@qq.com"

# 接收者
# receiver = "3584385399@qq.com"
receiver = "2431320433@qq.com"

# 邮件主题
subject = "测试"

# 发送附件
sendfile = open("C:\\Users\\Knight-YF\\PycharmProjects\\pythonProject\\ST\\keceng\\day13\\计算机.html", "r").read()

att = MIMEText(sendfile, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment;filename = 'test.html'"

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
