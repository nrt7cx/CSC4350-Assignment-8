#Nathaniel Tirado
#Server recieves four different messages from the client and sends the corresponding message back.
#Python; socket, argparse, datetime, logging
#run with command line
from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port", help="Sets port for server: ", type=int)
args = parser.parse_args()
serverPort = args.port

def getCheckSum(sentence):
    chksum = 0
    for i in sentence:
        chksum ^= ord(i)
    return str(hex(chksum))


serverSocket = socket(AF_INET,SOCK_DGRAM) 
serverSocket.bind(('',serverPort))
print ("The server is ready to receieve")

while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(message)
    
        if(message.decode()[0:4] == "0x10"):
            chksum = message.decode()[25:29]
            header = message.decode()[0:25]
            chksumver = getCheckSum(header)
            if chksum == chksumver:
                modifiedMessage = message.decode()
                modifiedMessage = modifiedMessage.replace("0x3","0x4")
                serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            
      
        else: 
            modifiedMessage = message.decode()
            modifiedMessage = modifiedMessage.replace("0x3","0x5")
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            