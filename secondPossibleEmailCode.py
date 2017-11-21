import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
s.starttls();
s.login("weatherstationdonotreply@gmail.com", "weatherstation");

msg = MIMEMultipart()

message = "this is a test message"

msg['From'] = "weatherstationdonotreply@gmail.com"
msg['To'] = "delias3@hawk.iit.edu";
msg['Subject'] = "weather"

msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)
Print("Done");
s.quit()
