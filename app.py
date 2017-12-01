import os
import sys
import smtplib
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(str(os.environ['EMAIL']), str(os.environ['PASSWD']))

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
    <p>Dear student,<br>
<br>
As stated in the timeline, KWoC's coding period officially begins today! Get ready with your coffee and buckle up for the rest of December, as we set to code and develop some awesome cool projects!<br>
<br>
By this time, we hope you have gone through the projects page well, chosen the projects according to your interests and contacted your mentors. If not, please join the communication channel of your project and contact your respective mentor, and begin contributing!<br>
<br>
A few things to keep in mind :<br>
<br>
1. Always ask smart questions. Don​'​t pester your mentor with questions that can easily be found on simple googling. They are busy people and are taking out time to help you get started. So, please respect their time and efforts and hence, put enough effort from your side too.<br>
<br>
2. Be active in the community bonding Facebook group. Use it to ask doubts in general or share your experiences.<br>
<br>
3. After 1 week, the Leaderboard will be up. If you have made at least one commit or Pull request,  you can see your name up there. If you don't see your name yet, don't get demotivated. Keep on trying and your name will come to the top ;)<br>
<br>
4. We will have a mid evaluation on 15th Decem​​ber. Please make sure you have made at​ ​least 1 commit till then, to continue in the program​me​.<br>
<br>
<br>
We hope you have an awesome winter ahead! Make the best out of this program​me​. All the best.<br>
<br>
In case of any issues, please contact us.<br>
<br>
​Regards,<br>
<a href="https://kossiitkgp.in">Kharagpur Open Source Society.</a><br>
<a href="http://iitkgp.ac.in">Indian Institute of Technology, Kharagpur.</a><br>
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
    you = text
    try:
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()
         #Next, log in to the server
         #print(str(os.environ['PASSWD']))
         server.login(str(os.environ['EMAIL']), str(os.environ['PASSWD']))   
         server.sendmail(me, you, msg.as_string())
         del(server)
    except:
        print("Mail server busy, will retry after some time. ")
        os.system("sleep 5m")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        #Next, log in to the server
        #print(str(os.environ['PASSWD']))
        server.login(str(os.environ['EMAIL']), str(os.environ['PASSWD']))   
        server.sendmail(me, you, msg.as_string())
        del(server)
    i+=1
    print(str(i)+". Sent mail to: "+str(text))