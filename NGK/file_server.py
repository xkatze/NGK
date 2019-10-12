import sys
from socket import *
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
    sock = socket(AF_INET, SOCK_STREAM) #creation of socket
    sock.bind((HOST,PORT))  #bind socket to ip and port
    sock.listen(1)  # waiting for connectiong

    print("Server is Ready")

    while True:
        connected, addr = sock.accept() #reciving clients adress and give them a name
        print("client connected with <" + str(addr) + ">") #printing where the connection is from

        wish = Lib.readTextTCP(connected)   #reading the TCP msg
        if wish != "q": #if not q check if the file exist

            datasize = Lib.check_File_Exists(wish)

            if datasize > 0:
                sendFile(wish, datasize, connected) #if file exist send the file

            else:
                connected.send("file does not exist")

        connected.close() #close client connection (it does not close the server)

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
    Lib.writeTextTCP(str(fileSize), conn) #sending information to client
    file = open(fileName, "rb") #opening file in "read binary" mode
    data = file.read(BUFSIZE) #read the binary and put it in a buffer
    while data:
        conn.send(data) #sending data over to client
        data = file.read(BUFSIZE) #updating data

    file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
