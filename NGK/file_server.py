import sys
import socket
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST,PORT))
    sock.listen(1)

    print("Server is Ready")

    while True:
        connected, addr = sock.accept()
        print("client connected with <" + str(addr) + ">")

        wish = Lib.readTextTCP(connected)
        datasize = Lib.check_File_Exists(wish)
        if datasize != 0:
            connected.send("Sending file")
            sendFile(wish, datasize, connected)
        else:
            connected.send("file does not exist")

    connected.close()

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
    Lib.writeTextTCP(str(fileSize),conn)
    file = open(fileName, 'rb')
    data = file.recv(BUFFSIZE)
    while totalsend < fileSize:
        conn.send(data)
        data = file.read(BUFFSIZE)


if __name__ == "__main__":
   main(sys.argv[1:])
