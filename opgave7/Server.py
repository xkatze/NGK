import sys
from socket import *

HOST = '10.0.0.1'
TARGET = '10.0.0.2'
PORT = 5000
BUFSIZE = 1000

def main():
    serversock = socket(AF_INET, SOCK_DGRAM)
    serverAdress = (HOST, PORT)
    target = (TARGET,PORT)
    serversock.bind(serverAdress)

    print("UDP server er oppe")

    while True:
        data, addr = serversock.recvfrom(1000)



        if data == 'u':
            with open("/proc/uptime","r") as f:
            	sec = float(f.readline().split()[0])
  
            serversock.sendto(str(sec) + " sekunder",target)

        if data == 'l':
            with open("/proc/loadavg","r") as f:
            	load = f.readlines()
            serversock.sendto("cpu load er <" + str(load) + ">" ,target)

if __name__ == "__main__":
   main()
