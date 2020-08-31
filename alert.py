import smtplib
from email.message import EmailMessage

def email_alert(subjec,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "dinesh.channa@gmail.com"
    password="jjozobtrgujhcngo"

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

    if __name__=='__main__':
        email_alert("Hey","Hello World","dinesh.channa@gmail.com")