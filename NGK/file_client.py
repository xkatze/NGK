import sys
import socket
from lib import Lib

TARGET = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print(sys.argv[1])
    client.connect((sys.argv[1],PORT))
    #client.connect((sys.argv[1:],PORT))
    Lib.writeTextTCP(sys.argv[2], client)
    size = Lib.readTextTCP(client)
    receiveFile(sys.argv[2], client)

    client.close()
def receiveFile(fileName,  conn):
	# TO DO Your Code
    file = open(fileName, 'wb')
    Lib.readTextTCP(conn)

if __name__ == "__main__":
   main(sys.argv[1:])
