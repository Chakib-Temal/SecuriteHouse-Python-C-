# -*- coding: utf-8 -*-
# Module de lecture/ecriture du port série
from serial import *
import smtplib
import io
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Port série ttyACM0
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec


fromaddr = "chakibtemal@gmail.com"
toaddr = "chakibtemal@gmail.com"
msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Alert"

body = "Attention"
msg.attach(MIMEText(body, 'plain'))

filename = "Photo.jpg"
attachment = open("/Users/macbookpro/Desktop/Photo.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
msgs = ""
alert = ""
nomImage = ""
condition = ""

with Serial(port="/dev/cu.usbmodem1411", baudrate=9600, timeout=1, writeTimeout=1) as port_serie:
    if port_serie.is_open:
        while True:
            ligne = port_serie.readline()
            print(ligne.decode("utf-8"))
            msgs = ligne.decode("utf-8")
            print (len(msgs))
            if len(msgs) >= 1:
                #alert,nomImage,condition = msgs.split(",")
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(fromaddr, "*******")
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
                server.quit()
