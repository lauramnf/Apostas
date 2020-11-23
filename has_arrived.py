import requests
import re
from email.message import EmailMessage
import smtplib

#Download page
response = requests.get(url)
response.raise_for_status() #if error it will stop the program

#Search for package's status
html_line = r'(<td width="100%" colspan="3" style="color: darkorange; font-size: 17px;"><center><b>)(.*)(</b></center></td>)'
code_status = re.search(html_line, response.text)
status = code_status[2]

#Defining email parameters
message = EmailMessage()
recipient = ['laura.neves2008@hotmail.com', 'heisson70@gmail.com']
sender = 'laura.neves2008@gmail.com'
password = input('Enter your password: ')
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Package Status'
body = 'Package Status: '+ status
message.set_content(body)

#Comfiguring SMTP to send it with a Gmail account
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
try:
    server.login(sender, password)
    print('It worked!')
except:
    print('Conection failed. Check if you entered the right password.')

#Sending email
try:
    server.send_message(message)
    print('The email was sent')
except:
    print('Fail on sending email')
server.quit()
