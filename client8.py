#Nathaniel Tirado
#Client sends created protocol over UDP to a server.
#Python, socket, argparse, random
#run with command line
from socket import *
import argparse
import random

def ACKNACK_tobytes():
    num = 4
    num = num.to_bytes(1,'big')
    num2 = 5
    num2 = num2.to_bytes(1,'big')
    return [num,num2]
def getCheckSum(sentence):
    chksum = 0
    for i in sentence:
        chksum ^= ord(i)
    return chksum

parser = argparse.ArgumentParser()
parser.add_argument("-i","--internet", help="Sets IP Address for client: ", type=str)
parser.add_argument("-p","--port", help="Sets Port for client: ", type=int)
parser.add_argument("-m","--msg", help="Sets the msg for the client: ", type=str)
args = parser.parse_args()

serverIP = args.internet
serverPort = args.port
clientMsg = args.msg
clientSocket = socket(AF_INET, SOCK_DGRAM)
multivalue = ACKNACK_tobytes()
pakcor = random.randint(0,9)

def id_tobytes():
    ProID = 1
    ProID = ProID.to_bytes(1,'big')
    return ProID    
def len_tobytes():
    PromsgLen = 9 + len(clientMsg)
    PromsgLen = PromsgLen.to_bytes(1,'big')
    return PromsgLen
def len_corrupter():
    PromsgLen = random.randint(19,254)
    PromsgLen = PromsgLen.to_bytes(1,'big')
    return PromsgLen
def port_tobytes():
    ProPort = serverPort
    ProPort = ProPort.to_bytes(2,'big')
    return ProPort
def rand_tobytes(): 
    ProRand = random.randint(277,65535)
    ProRand = ProRand.to_bytes(2,'big')
    return ProRand
def field_tobytes():
    ProField = 3
    ProField = ProField.to_bytes(1,'big')
    return ProField
def seq_tobytes():
    ProSeq = random.randint(0,255)
    ProSeq = ProSeq.to_bytes(1,'big')
    return ProSeq
def chksum_tobytes(var):
    ProChkSum = getCheckSum(str(var))
    ProChkSum = ProChkSum.to_bytes(1,'big')
    return ProChkSum

ProID = id_tobytes()
PromsgLen = len_tobytes()
ProPort = port_tobytes()
ProRand = rand_tobytes()
ProField = field_tobytes()
ProSeq = seq_tobytes()
header = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq
ProChkSum = chksum_tobytes(header)
clientMsg = clientMsg.encode()

message = header + ProChkSum + clientMsg

print("Original Message:" + ' ' + str(message))
if pakcor == 1:
    print("Packet Corrupt")
    PromsgLen = len_corrupter()
    header = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq
    message = header + ProChkSum + clientMsg
clientSocket.sendto(message,(serverIP,serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
if modifiedMessage[6:7] not in multivalue:
    print("Packet Drop")
    clientSocket.sendto(message,(serverIP,serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print ("New Message:" + ' ' + str(modifiedMessage))

clientSocket.close
