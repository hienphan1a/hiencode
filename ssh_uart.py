import pexpect,time
import struct, fcntl, os, sys, signal
#var i
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import re
def sendmail(article,attachment,file_name):
        recipients = ['hphan@apm.com','tayduki614@gmail.com']
        emaillist = [elem.strip().split(',') for elem in recipients]
        msg = MIMEMultipart()
        msg['Subject'] =article ### str(sys.argv[1])
        msg['From'] = 'hphan@apm.com'
        msg['Reply-to'] = 'hphan@apm.com'

        msg.preamble = 'Multipart massage.\n'

        part = MIMEText("Hi, please find the attached file")
        msg.attach(part)
		if attachment==1:
			part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
			part.add_header('Content-Disposition', 'attachment', filename=file_name)
			msg.attach(part)


        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()

        server.login("hphan@apm.com", "Thichca@9876543")


        server.sendmail(msg['From'], emaillist , msg.as_string())
        return ;

global mode 
global p 
global h

def nps_port(server,port,prompt,cmd):
        nps=pexpect.spawn("telnet" + " " + server)
        nps.logfile=sys.stdout
        nps.expect(prompt)
        if cmd == "off":
                cmd1="/off " + port
                nps.send (cmd1 + "\r")
                nps.expect(prompt)
                nps.sendline("/x")
        elif cmd == "on":
                cmd1="/on " + port
                nps.send (cmd1 + "\r")
                nps.expect(prompt)
                nps.sendline("/x")
        else :
                print "Do nothing"
        return
def connect_uart(port,prompt):
	global p
	print "Connect to uart"
	#p.sendline("kermit -c -y ~/.kermrc_USB1")
	p.sendline("minicom /dev/ttyUSB1")
	p.send("\r")
	i=p.expect(prompt)
	p.sendline("usb start")
	#p.timeout=1000
	i=p.expect([prompt,pexpect.TIMEOUT],1000)
	if i==1:
			print "Timeout"
			sys.exit()
	elif i==0:
			print "run usb command successfully"
			p.interact()
	return
def telnet_server(server,user,password,prompt):
	telconn = pexpect.spawn("telnet" + " " +  hostip)
	telconn.logfile = sys.stdout
	telconn.expect("login:")
	telconn.send (user + "\r")
	telconn.expect(":")
	telconn.send (password + "\r")
	telconn.expect(prompt)
	telconn.send ("ls" + "\r" )
	telconn.expect(prompt)
	return
def ssh_server(server,prompt,user,passwd):
#prompt="root@hcmlab11"
		global p
        ssh_newkey = "Are you sure you want to continue connecting"
        #p=pexpect.spawn("ssh validation_local@10.38.12.31")
        p=pexpect.spawn("ssh" + " " + user + "@" + server)
		##### p_file=file("hien.txt" ,"wb")
        p.logfile = sys.stdout  ### help to print on the screen
        i=p.expect([ssh_newkey,'password:',pexpect.EOF])
        if i==0:
                print "I say yes"
                p.sendline("yes")
                i=p.expect([ssh_newkey,'password:',pexpect.EOF])
        #p.sendline("amcc@123")
                p.sendline(passwd)
        if i==1:
                print "I give password",
                #p.sendline("amcc@123")
                p.sendline(passwd)
        elif i==2:
                print "I either got key or connection timeout"
                pass
		#elif i==3: #timeout
#    pass
        i=p.expect(prompt)
#        print "value of i = %d" % i
        p.sendline ("pwd")
        i=p.expect(prompt)
        p.sendline ("ls")
        i=p.expect(prompt)
        p.send("\r")
        i=p.expect(prompt)
        #p.sendline("kermit -c -y ~/.kermrc_USB1")
        #p.send("\r")
        #i=p.expect("ney#")
        #p.sendline("printenv \r")
        #p.sendline("usb start")
        #p.timeout=1000
        #i=p.expect(["ney#",pexpect.TIMEOUT],1000)
        #if i==1:
        #       print "Timeout"
        #        sys.exit()
        #elif i==0:
        #        print "run usb command successfully"
        #        p.interact()
#               h=raw_input("enter")
#               p.sendline
        #print spawn_id
        return
def compile_code(dir,mode):
	global p
	p.sendline("cd " + dir)
	p.expect(prompt)
	return
class runtest:
        error = 0
        rc = 0
        global p
        global nps
#       global pexpect
        def __init__(self,serverip,user,passwd,npsip,port):
                self.serverip=serverip
                self.user=user
                self.passwd=passwd
                self.npsip=npsip
                self.port=port
                #self.nps=nps

        def telnet_nps(self,prompt, cmd):
                print self.port
                print self.npsip
                nps_port(self.npsip,self.port,prompt,cmd)
                return
        def connect_ssh(self,prompt):
                ssh_server(self.serverip,prompt,self.user,self.passwd)
                return
        def connect_Uart(self,prompt):
                connect_uart("USB0",prompt)
                return
		def sendmail(self,attachment,file_name):
				return
        def __del__(self):
                class_name = self.__class__.__name__
                print class_name, "destroyed"

hien=runtest("10.38.12.31","validation_local","amcc@123","10.38.12.192","7")
hien.telnet_nps("NPS>","off")
time.sleep(10)
hien.telnet_nps("NPS>","on")
hien.connect_ssh("root@hcmlab11")
hien.connect_Uart("ney#")

#nps_port("10.38.12.192","7","NPS>","off")
#time.sleep(10)
#nps_port("10.38.12.192","7","NPS>","on")
#time.sleep(40)
#ssh_server("10.38.12.31", "root@hcmlab11","validation_local","amcc@123")
