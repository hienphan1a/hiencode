import pexpect
import time,sys
### to access the serial port -> please import subprocess
#user="amcclab"
#password="amcc1234"
#hostip="10.38.6.218"
#telconn = pexpect.spawn('telnet 10.38.6.218')
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
def sendmail(title):
	recipients = ['hphan@apm.com','tayduki614@gmail.com']
	emaillist = [elem.strip().split(',') for elem in recipients]
	msg = MIMEMultipart()
	msg['Subject'] = title ####str(sys.argv[1])
	msg['From'] = 'hphan@apm.com'
	msg['Reply-to'] = 'hphan@apm.com'

	msg.preamble = 'Multipart massage.\n'

	part = MIMEText("Hi, please find the attached file")
	msg.attach(part)

	############# This following function is used for the attachment file
	#part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
	#part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[2]))
	#msg.attach(part)


	server = smtplib.SMTP("smtp.gmail.com:587")
	server.ehlo()
	server.starttls()

	server.login("hphan@apm.com", "Thichca@9876543")


	server.sendmail(msg['From'], emaillist , msg.as_string())
	return
	
total=len(sys.argv)
if ( total < 4 ):
        print "Need to put argument again\n"
        sys.exit()

hostip=sys.argv[1]
user=sys.argv[2]
password=sys.argv[3]
#total = len(sys.argv)
#if ( total < 3 ):
#       print "Need to put argument again\n"
#       sys.exit()
prompt="amcclab09:"
telconn = pexpect.spawn("telnet" + " " +  hostip)
#time.sleep(2)
telconn.logfile = sys.stdout
telconn.expect("login:")
#time.sleep(2)
#telconn.send("amcclab" + "\r")
telconn.send (user + "\r")
telconn.expect(":")
telconn.send (password + "\r")
#telconn.send("amcc1234" + "\r")
#telconn.send("\r\n")
#time.sleep(2)
telconn.expect(prompt)
telconn.send ("ls" + "\r" )
#time.sleep(10)
telconn.expect(prompt)
#time.sleep(2)
telconn.send ("cd /DATA1/hphan/shadowcat/new_shadowcat/xval_skylark/aptio " + "\r")
telconn.expect(prompt)
#time.sleep(10)
telconn.send ("./compile.sh vIOCZ_USB" + "\r")
telconn.expect(prompt, timeout=5000)

#telconn.send ("exit" + "\r" )

