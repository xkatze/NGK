import sys
from socket import *

HOST = '10.0.0.1'
PORT = 5000
BUFSIZE = 1000

def main():
    serversock = socket(AF_INET, SOCK_DGRAM)
    serverAdress = (HOST, PORT)

    serversock.bind(serverAdress)

    while True:
        data, addr = serversock.recvfrom(1000)

        if data == 'u':
            sec = open("/proc/uptime","r")
            print(sec + "virker det?")

        if data == 'l':
            load = open("/proc/loadavg","r")
            print(load +"virker det?")

if __name__ == "__main__":
   main()
