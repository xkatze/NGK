import sys
from socket import *

TARGET = '10.0.0.1'
HOST = '10.0.0.2'
PORT = 5000
BUFSIZE = 1000

def main():
    target = (TARGET,PORT)
    host = (HOST,PORT)
    client = socket(AF_INET, SOCK_DGRAM)
    client.bind(host)

    sending = raw_input("u/l ->")
    client.sendto(sending,target)

    data, addr = client.recvfrom(1000)

    print(data)

if __name__ == "__main__":
   main()
