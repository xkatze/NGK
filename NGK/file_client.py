import sys
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    if len(argv) > 0:
        TARGET = argv[0]
        FILE = argv[1]
    else:
        sys.exit()

    client = socket(AF_INET, SOCK_STREAM)
    client.connect((TARGET,PORT))

    Lib.writeTextTCP(FILE, client)
    sizer = Lib.readTextTCP(client)


    receiveFile(FILE, client, sizer)

    client.close()
    sys.exit()

def receiveFile(fileName,  conn, size):
	# TO DO Your Code
    bytesToRead = 0
    name = Lib.extractFilename(fileName)
    file = open(name, 'wb')
    while(int(size) > bytesToRead):
        data = conn.recv(BUFSIZE)
        file.write(data)
        bytesToRead += len(data)

        if bytesToRead == int(size):
            break

    file.close()
    print("completed transfering file")

if __name__ == "__main__":
   main(sys.argv[1:])
