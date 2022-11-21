from socket import *
import argparse
import random

def getCheckSum(sentence):
    chksum = 0
    for i in sentence:
        chksum ^= ord(i)
    return hex(chksum)

ProID = hex(1)


PromsgLen = hex(10) 


ProPort = hex(8000)


ProRand = hex(random.randint(0,65535))

ProField = hex(3)

ProSeq = hex(random.randint(0,255))


header = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq
ProChkSum = getCheckSum(header)
clientMsg = 'hello'
#clientMsg = clientMsg.encode('utf-8')

message = ProID + PromsgLen + ProPort + ProRand + ProField + ProSeq + ProChkSum + clientMsg
message = message.encode('utf-16')
print(message)