#Nathaniel Tirado
#Client sends created protocol over UDP to a server.
#Python; socket, argparse,random
#run with command line
from socket import *
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("-i","--internet", help="Sets IP Address for client: ", type=str)
parser.add_argument("-p","--port", help="Sets Port for client: ", type=int)
parser.add_argument("-m","--msg", help="Sets the msg for the client: ", type=str)
args = parser.parse_args()

def getCheckSum(sentence):
    chksum = 0
    for i in sentence:
        chksum ^= ord(i)
    return str(hex(chksum))

serverIP = args.internet
serverPort = args.port
clientMsg = args.msg
clientSocket = socket(AF_INET, SOCK_DGRAM)


ProID = hex(1)
PromsgLen = hex(10 + len(clientMsg))
ProPort = hex(serverPort)
ProRand = hex(random.randint(0,65535))
ProField = hex(3)
ProSeq = hex(random.randint(0,255))
header = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq
ProChkSum = getCheckSum(header)

message = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq + ProChkSum + clientMsg
clientSocket.sendto(message.encode(),(serverIP,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close
