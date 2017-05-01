#!/usr/bin/python

import pexpect,time
import struct, fcntl, os, sys, signal
import logging

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("log.dat", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
#       self.terminal.log_open = open("hien.dat", 'w', 0)
 #       self.terminal.log_open.write("Time:  %s\n%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S"), "-"*80))

        #self.stdout.flush()
#sys.stdout = Logger()


#var i
def NPS_STATION(server,port,prompt):
        nps=pexpect.spawn("telnet" + " " + server)
        nps.logfile=sys.stdout
        nps.expect(prompt)
#       nps.sendline("/off " + port)
        cmd="/off " + port
        nps.send (cmd  + "\r")
        nps.expect(prompt)
#       nps.sendline("/x")
#       time.sleep(10)

#       nps=pexpect.spawn("telnet" + " " + server)
#        nps.logfile=sys.stdout
#        nps.expect(prompt)

        nps.send("\r " )
        nps.expect(prompt)
        cmd="/on " + port
#       nps.sendline("/on  " + port)
        nps.send(cmd + "\r")
        nps.expect(prompt)
        nps.sendline("/x")
        return

global hien
global test_mode
hien=5
global pid

global p

#def Compile_code():
#       hien=0
#       logging.basicConfig(stream=sys.stdout,filename='myapp.log', level=logging.INFO)
#       print "Started"
#       logging.info("Started")
#       logging.info(sys.stdout)
#       print hien
#       print "Finished"
#       logging.info("Finished")
#       return
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
def connect_uart (prompt):
        global p
        print "Connect to uart"
        p.sendline("kermit -c -y ~/.kermrc_USB1")
        #p.sendline("minicom /dev/ttyUSB1")
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
                p.sendline("usb tree")
                i=p.expect([prompt,pexpect.TIMEOUT],1000)
                #p.interact()
        return
def ssh_server(server,prompt,user,passwd):
        global p
#prompt="root@hcmlab11"
        ssh_newkey = "Are you sure you want to continue connecting"
        #p=pexpect.spawn("ssh validation_local@10.38.12.31")
        p=pexpect.spawn("ssh" + " " + user + "@" + server)
        p.logfile = sys.stdout
		log_file=open("test.log","wb")
        p.logfile_read=log_file
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
#       print "value of i = %d" % i
        #print p.pid
        pid=p.pid
        p.sendline ("pwd")
        i=p.expect(prompt)
        p.sendline ("ls")
        i=p.expect(prompt)
        p.send("\r")
        i=p.expect(prompt)
        #exit()
        #sys.exit()
#       p.sendline("kermit -c -y ~/.kermrc_USB1")
#       p.send("\r")
#       i=p.expect("ney#")
        #p.sendline("printenv \r")
#       p.sendline("usb start")
        #p.timeout=1000
#       i=p.expect(["ney#",pexpect.TIMEOUT],1000)
#       if i==1:
#               print "Timeout"
#               sys.exit()
#       elif i==0:
#               print "run usb command successfully"
#               p.interact()
#               h=raw_input("enter")
#               p.sendline
        #print spawn_id
        return
def Compile_code():
#       hien=0
#        logging.basicConfig(stream=sys.stdout,filename='myapp.log', level=logging.INFO)
#       logger = logging.getLogger('./myapp1.log')
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger('myapp.log')
        #hdlr = logging.FileHandler('./myapp.log')
        #formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        #hdlr.setFormatter(formatter)
        #logger.addHandler(hdlr)
        #logger.setLevel(logging.INFO)
        print "Started"
        logging.info("Started")
#       logging.info(sys.stdout)
        nps_port("10.38.12.192","7","NPS>","off")
        time.sleep(10)
        nps_port("10.38.12.192","7","NPS>","on")
        time.sleep(40)
        ssh_server("10.38.12.31", "root@hcmlab11","validation_local","amcc@123")
        connect_uart("10.38.12.31","USB0")

        print hien
        print "Finished"
        logging.info("Finished")
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
                connect_uart(prompt)
                return

        def __del__(self):
                class_name = self.__class__.__name__
                print class_name, "destroyed"


#sys.stdout = Logger()
#sys.stdout.flush()
#Logger()
hien=runtest("10.38.12.31","validation_local","amcc@123","10.38.12.192","7")
hien.telnet_nps("NPS>","off")
time.sleep(10)
hien.telnet_nps("NPS>","on")
hien.connect_ssh("root@hcmlab11")
hien.connect_Uart("ney#")
                              