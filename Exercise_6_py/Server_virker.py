import sys
from socket import *
from lib import Lib

HOST = '10.0.0.1' #Local host
PORT = 9000
BUFSIZE = 1000 # Chunk of data/bytes that can be sent at a time.

def main(argv):
	servSock = socket(AF_INET, SOCK_STREAM) # INET = family socket type (IPV4), _STREAM = socket type (TCP).
	servSock.bind((HOST, PORT)) # ip and port, here localhost and port

# socket is the end point that recieves data. Send and recieves data.
# The socket itself is not the communication, it's the destination. Endpoint sits at a ip and port.
	servSock.listen(1)  # Leave a queue of 1, only one connection allowed
	print("The server is ready to recieve\n")

#listen forever for connections and if we get one, do the following:
	while True:
		conSock, addr = servSock.accept()
        #anybody connects, we're happy to see you.
    # client socket object stored in variabel clientsocket. Addr = IP adress,where are the client comming from.

		print("client connected\n")  # send information to the client socket, (what do we want to send to the client?),type-of-bytes
		msg = Lib.readTextTCP(conSock)
		if(msg != "exit"):
			print("Command received: %s\n" % msg)

			fileSize = Lib.check_File_Exists(msg)

			if fileSize > 0:

				sendFile(msg, fileSize, conSock)

		print("Connection closed")
		conSock.close()
	# Saa laenge beskeden ikke er EXIT, saa tjekker vi om fileSize > 0, hvis den er det sender den beskeden.
    # hvis den ikke er det, saa lukker vi socket (doeren/endestation)


def sendFile(fileName,  fileSize,  conn): # Sendfile funktion med parameterne (fil navn, fil size, conn/addr )
	Lib.writeTextTCP(str(fileSize), conn)
	file = open(fileName, 'rb')   # rb = read og binary
	data = file.read(BUFSIZE) # vi kan laese 1000 bytes
	while data:
		conn.send(data) # sender bytes
		data = file.read(BUFSIZE)

if __name__ == "__main__":
   main(sys.argv[1:])
  # Naar funktionen sendFile kaldes bruges (fileName, fileSize, conSock); e.g. sendFile(Hello, 30, conSock)
