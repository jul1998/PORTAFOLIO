import os
import smtplib, ssl

def send_email(email,password, to_address, msg):
    smtp_port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", smtp_port, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, to_address, msg=msg)
