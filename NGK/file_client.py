import sys
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    if len(argv) > 0: #give arguments in the terminal names
        TARGET = argv[0]
        FILE = argv[1]
    else:
        sys.exit()

    client = socket(AF_INET, SOCK_STREAM)   #making the socket
    client.connect((TARGET,PORT))

    Lib.writeTextTCP(FILE, client)  #asking for file
    sizer = Lib.readTextTCP(client) #receives the filesize from server


    receiveFile(FILE, client, sizer) #receive the file

    client.close()
    sys.exit()

def receiveFile(fileName,  conn, size):
	# TO DO Your Code
    bytesToRead = 0
    name = Lib.extractFilename(fileName) #getting the name of the file
    file = open(name, 'wb') #using the file name to make a new file
    while(int(size) > bytesToRead): #building the new file
        data = conn.recv(BUFSIZE)
        file.write(data)
        bytesToRead += len(data)

        if bytesToRead == int(size): # makes sure that the file doesnt get too much data
            break

    file.close()
    print("completed transfering file")

if __name__ == "__main__":
   main(sys.argv[1:])
