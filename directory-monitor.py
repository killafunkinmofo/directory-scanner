#!/usr/local/bin/python

import requests,smtplib,json,os
from time import sleep
from email.mime.text import MIMEText
from_email = ''
to_email = ''
smtp_server = ''

while True:
 try:
     current_dirlist = os.listdir('.')
     try: 
	list(previous_dirlist)
     except:
	previous_dirlist = list(current_dirlist)
     for file in current_dirlist:
         if file in previous_dirlist:
             continue
         else:
            msg = MIMEText("File {} has been found".format(file))
            msg['Subject'] = 'New File Found'
            msg['From'] = from_email
            msg['To'] = to_email
            s = smtplib.SMTP(smtp_server)
            print("New file found {}".format(file))
            s.sendmail(from_email, [to_email], msg.as_string())
            s.quit()
 except:
     pass
 sleep(1)
 previous_dirlist = list(current_dirlist)
