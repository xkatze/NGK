import sys
import socket
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

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((TARGET,PORT))
    Lib.writeTextTCP(FILE, client)
    size = Lib.readTextTCP(client)
    receiveFile(FILE, client, size)

    client.close()
def receiveFile(fileName,  conn, size):
	# TO DO Your Code
    bytesToRead = 0
    file = open(fileName, 'wb')
    while int(size) > bytesToRead:
        data = conn.recv(BUFFSIZE)
        file.write(data)
        bytesToRead += data

        if bytesToRead == int(size):
            break
    file.close()
    print("completed transfering file")
if __name__ == "__main__":
   main(sys.argv[1:])
