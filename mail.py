import smtplib
import ssl


port = 587
smtp_server = "smtp.outlook.com" 
receiver_email = "sivalakshan724@gmail.com"  # Change this address to the address where you want to recieve the email from the bot
# create a secure SSL context

context = ssl.create_default_context()


def sendmail(message, password, sender_email):
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
