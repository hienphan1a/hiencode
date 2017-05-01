#!/usr/bin/python

import pexpect,time
import struct, fcntl, os, sys, signal
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
def ssh_server(server,prompt,user,passwd):
#prompt="root@hcmlab11"
        ssh_newkey = "Are you sure you want to continue connecting"
        #p=pexpect.spawn("ssh validation_local@10.38.12.31")
        #sys.stdout = os.fdopen (sys.stdout.fileno(), 'w', 0)
        #pfile=open("hien2.txt","wb")
        #os.dup2 (pfile.fileno(), sys.stdout.fileno())
        p=pexpect.spawn("ssh" + " " + user + "@" + server)
        p.logfile = sys.stdout
        log_file=open("test.log","wb")
        p.logfile_read=log_file
#       sys.stdout = os.fdopen (sys.stdout.fileno(), 'w', 0)
#       p_file=file("./hien.txt" , "wb")
        #p.setlog(p_file)
#       p.logfile=p_file
#       pfile=open("hien2.txt","wb")
#       p.setlog(pfile)
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
        print "value of i = %d" % i
        p.sendline ("pwd")
        i=p.expect(prompt)
        p.sendline ("ls")
        i=p.expect(prompt)
        p.send("\r")
        i=p.expect(prompt)
        #p.sendline("printenv \r")
        p.sendline("usb start")
        #p.timeout=1000
        i=p.expect(["ney#",pexpect.TIMEOUT],1000)
        if i==1:
                print "Timeout"
                sys.exit()
        elif i==0:
                print "run usb command successfully"
                p.close()
#               p.interact()
#               h=raw_input("enter")
#               p.sendline
        #print spawn_id
        return

#NPS_STATION("10.38.12.192","7","NPS>")
nps_port("10.38.12.192","7","NPS>","off")
time.sleep(10)
nps_port("10.38.12.192","7","NPS>","on")
time.sleep(40)
ssh_server("10.38.12.31", "root@hcmlab11","validation_local","amcc@123")
#global global_pexpect_instance
#global_pexpect_instance = p
#p.sendline("sudo su -")
#p.sendline("mypasswd")
#p.sendline("mkdir /home/hphan/test")
#print p.before
#print p.after
