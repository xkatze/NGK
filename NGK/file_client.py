import sys
import socket
from lib import Lib

TARGET = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(sys.argv[1])
    client.connect((TARGET,PORT))
    #client.connect((sys.argv[1:],PORT))
    #receiveFile(sys.argv[2], client)

def receiveFile(fileName,  conn):
	# TO DO Your Code
    writeTextTCP(fileName, conn)
    readTextTCP(conn)

if __name__ == "__main__":
   main(sys.argv[1:])
