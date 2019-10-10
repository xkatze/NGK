import sys
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
	if len(argv) > 0:
		SERVER = argv[0]
		FILE = argv[1]
	else:
		print("Benyt formatet 'python file_client.py <IP>'\n")
		sys.exit()

	sock = socket(AF_INET, SOCK_STREAM) # this socket wants to connect rather than binding. Therefore:
	sock.connect((SERVER,PORT))  #ip and port, using gethostname since it's on the same machine

	#print(FILE)
	Lib.writeTextTCP(FILE,sock)
	filesize = Lib.readTextTCP(sock)
	receiveFile(FILE, sock, filesize)

	sock.close()
	sys.exit()


def receiveFile(nm,  conn, size):
	bytesRead = 0
	fileName = Lib.extractFilename(nm)
	file = open(fileName, 'wb')

	while (int(size) > bytesRead):
		buff = conn.recv(BUFSIZE)
		file.write(buff)
		bytesRead = bytesRead+len(buff)

		if(bytesRead == int(size)):
			break

	file.close()
	print("Transfer complete\n")

if __name__ == "__main__":
   main(sys.argv[1:])
