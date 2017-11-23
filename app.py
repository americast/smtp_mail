import os
import sys
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(str(os.environ['kossiitkgp@gmail.com']), str(os.environ['PASSWD']))

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "Kharagpur Winter of Code <kwoc@kossiitkgp.in>"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Registration successful"
msg['From'] = me
#Send the mail
html ="""\
<html>
  <head></head>
  <body>
    <p>Hello mentor!<br>
       Welcome to KWoC!<br>
       Please read the manual <a href="https://kwoc.kossiitkgp.in/static/files/KWoCMentorManual.pdf">here</a>.
    </p>
  </body>
</html>
""" 

#part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

#msg.attach(part1)
msg.attach(part2)

i=0
f = open('emails.txt')
while(1):
    text = f.readline()
    if not text:
        break
    msg['To'] = text
    try:
        server.sendmail(me, you, msg.as_string())
    except:
        del(server)
        os.system("sleep 5m")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        #Next, log in to the server
        #print(str(os.environ['PASSWD']))
        server.login(str(os.environ['EMAIL']), str(os.environ['PASSWD']))
        server.sendmail(me, you, msg.as_string())
    i+=1
    print(str(i)+"sent mail to: "+str(text))