import smtplib  
from email.mime.text import MIMEText  
from email.header import Header 
import base64
 
def mail_test(): 
    sender = '1193009984@qq.com'  
    receiver = '1184866099@qq.com'  
    subject = 'python email test'  
    smtpserver = 'smtp.qq.com'  
    username = '1193009984'  
    password = 'mlcxcdlupwkcgjgc' 
    mail_body='收到邮件bqq告诉我一下'
    print('11');
     
    msg = MIMEText(mail_body, 'utf-8')  
    msg['Subject'] = Header(subject, 'utf-8')  
     
    smtp = smtplib.SMTP()

    smtp.connect(smtpserver)  
    #smtp.starttls()
    smtp.login(username,  password)  
    smtp.sendmail(sender, receiver, msg.as_string())  
    smtp.quit()  
     
def main():
    mail_test()

main()