#Nathaniel Tirado
#Client sends created protocol over UDP to a server.
#Python, socket, argparse, random
#run with command line
from socket import *
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("-i","--internet", help="Sets IP Address for client: ", type=str)
parser.add_argument("-p","--port", help="Sets Port for client: ", type=int)
parser.add_argument("-m","--msg", help="Sets the msg for the client: ", type=str)
args = parser.parse_args()
pakcor = random.randint(0,9)

def getCheckSum(sentence):
    chksum = 0
    for i in sentence:
        chksum ^= ord(i)
    return chksum

serverIP = args.internet
serverPort = args.port
clientMsg = args.msg
clientSocket = socket(AF_INET, SOCK_DGRAM)
num = 4
num = num.to_bytes(1,'big')
num2 = 5
num2 = num2.to_bytes(1,'big')
multivalue = [num,num2]


ProID = 1
ProID = ProID.to_bytes(1,'big')

PromsgLen = 10 + len(clientMsg)
PromsgLen = PromsgLen.to_bytes(1,'big')

ProPort = serverPort
ProPort = ProPort.to_bytes(2,'big')

ProRand = random.randint(277,65535)
ProRand = ProRand.to_bytes(2,'big')

ProField = 3
ProField = ProField.to_bytes(1,'big')

ProSeq = random.randint(0,255)
ProSeq = ProSeq.to_bytes(1,'big')

header = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq
ProChkSum = getCheckSum(str(header))
ProChkSum = ProChkSum.to_bytes(1,'big')
clientMsg = clientMsg.encode()

message = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq + ProChkSum + clientMsg
print("Original Message:" + ' ' + str(message))
if pakcor == 1:
    print("Packet Corrupt")
    PromsgLen = 22
    PromsgLen = PromsgLen.to_bytes(1,'big')
    message = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq + ProChkSum + clientMsg



clientSocket.sendto(message,(serverIP,serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

if modifiedMessage[6:7] not in multivalue:
    print("Packet Drop")
    clientSocket.sendto(message,(serverIP,serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    


print ("New Message:" + ' ' + str(modifiedMessage))
clientSocket.close
