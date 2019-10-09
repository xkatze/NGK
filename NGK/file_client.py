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
    receiveFile(sys.argv[2], client, size)

    client.close()
def receiveFile(fileName,  conn, size):
	# TO DO Your Code
    bytesToRead = 0
    file = open(fileName, 'wb')
    while (int(size)) > bytesToRead:
        data = conn.recv(BUFFSIZE)
        file.write(data)
        bytesToRead += data

        if bytesToRead == (int(size)):
            break
    file.close()
    print("completed transfering file")
if __name__ == "__main__":
   main(sys.argv[1:])
