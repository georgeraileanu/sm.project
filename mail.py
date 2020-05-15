import smtplib
from datetime import datetime

def sendMail():

  smtpUser='test.gyro.sm@gmail.com'
  smtpPass='testac123'

  toAdd='test.gyro.sm@gmail.com'
  fromAdd=smtpUser

  now = datetime.now()
  dt_string = now.strftime("%d-%b-%Y (%H:%M:%S)")
  #print dt_string

  msg="The alarm on your motorcycle has been activated at "

  subject= msg + dt_string

  header='To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject

  body= ' From within a Python script'

  print header + '\n' + body

  server=smtplib.SMTP('smtp.gmail.com', 587)

  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(smtpUser,smtpPass)
  server.sendmail(fromAdd,toAdd, header + '\n' + body)
  server.quit()
