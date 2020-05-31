from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import urllib

def main():
    sender = 'WZP_1995@163.com'
    receivers = ['weizp_1995@163.com']
    message = MIMEText('send email with python', 'plain', 'utf-8')
    message['from'] = Header('weizhaopeng', 'utf-8')
    message['to'] = Header('weichaopeng', 'utf-8')
    message['Subject'] = Header('example', 'utf-8')
    smtper = SMTP('smtp.163.com')
    smtper.login(sender, '1234')
    smtper.sendmail(sender, receivers, message.as_string())
    print('mail has been sent')

def main1():
    message = MIMEMultipart()
    textContent = MIMEText('please take case of the attactment', 'plain', 'utf-8')
    message['Subject'] = Header('the date this month', 'utf-8')
    message.attach(textContent)

    with open('/usr/Hao/Desktop/hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['content_tyep'] = 'text/plain'
        txt['content-disposition'] = 'attachment;filename=hello.txt'
        message.attach(txt)
    with open('/usr/Hao/Desktop/data.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['content_type'] = 'application/vnd.ms-excel'
        xls['content-disposition'] = 'attachment;filename=data.xlsx'
        message.attach()

    smtper = SMTP('smtp.163.com')
    smtper.starttls()
    sender = 'wzp_1995@163.com'
    receiver = 'weizp_1995@163.com'
    smtper.login(sender, '1245')
    smtper.sendmail(sender, receiver, message.as_string())
    smtper.quit()
    print('alreadly sent')



if __name__ == '__main__':
    main()

