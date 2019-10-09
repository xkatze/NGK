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

        wish = lib.readTextTCP(sock)
        datasize = lib.check_File_Exists(wish)
        if datasize != 0:
            sock.send("Sending file")
            sendFile(wish, datasize, sock)
        else:
            sock.send("file does not exist")

    sock.close()

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
    totalsend = 0
    data = conn.recv(BUFFSIZE)
    while totalsend < fileSize:
        writeTextTCP(fileName, conn)
        totalsend += data


if __name__ == "__main__":
   main(sys.argv[1:])
