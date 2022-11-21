#Nathaniel Tirado
#Server recieves packet and ensures the checksum is correct and edits the packet to send an ack = 0x4 or a nack = 0x5.
#Python; socket, argparse
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
    return chksum


serverSocket = socket(AF_INET,SOCK_DGRAM) 
serverSocket.bind(('',serverPort))
print ("The server is ready to receieve")

while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(message)
        print(message[9::])
        if(message[0:1] == b'\x01'):
            message
            chksum = message[8:9]
            header = message[0:8]
            print(header)
            chksumver = getCheckSum(str(header))
            chksumver = chksumver.to_bytes(1,'big')
        
            if chksum == chksumver:
                modifiedMessage = message[0:6] + b'\x04' + message[7::]
                serverSocket.sendto(modifiedMessage,clientAddress)
            
      
        else: 
            modifiedMessage = message[0:6] + b'\x05' + message[7::]
            serverSocket.sendto(modifiedMessage,clientAddress)
            