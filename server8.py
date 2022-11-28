#Nathaniel Tirado
#Server recieves packet and ensures the checksum is correct and edits the packet to send an ack = 0x4 or a nack = 0x5.
#Python, socket, argparse, random
#run with command line
from socket import *
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port", help="Sets port for server: ", type=int)
args = parser.parse_args()
serverPort = args.port

def getCheckSum(sentence):
    chksum = 0
    for i in sentence:
        chksum ^= ord(i)
    return chksum
def chksum_tobytes(var):
    ProChkSum = getCheckSum(str(var))
    ProChkSum = ProChkSum.to_bytes(1,'big')
    return ProChkSum

serverSocket = socket(AF_INET,SOCK_DGRAM) 
serverSocket.bind(('',serverPort))
print ("The server is ready to receieve")

while True:
        pakdrop = random.randint(0,9)
        print(pakdrop)
        message, clientAddress = serverSocket.recvfrom(2048)
        print(message)
        print(message[8:9])
        print(message[9::])
        if(message[0:1] == b'\x01'):
            message
            chksum = message[8:9]
            header = message[0:8]
            print(header)
            chksumver = chksum_tobytes(header)
            
            if pakdrop == 2 :
                    modifiedMessage = message[0:6] + message[7::] 
                    print(modifiedMessage)
                    serverSocket.sendto(modifiedMessage,clientAddress)
            
            elif chksum == chksumver:
                modifiedMessage = message[0:6] + b'\x04' + message[7::]
                serverSocket.sendto(modifiedMessage,clientAddress)
            
            else: 
                modifiedMessage = message[0:6] + b'\x05' + message[7::]
                serverSocket.sendto(modifiedMessage,clientAddress)
            