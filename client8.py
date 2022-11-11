#Nathaniel Tirado
#Client sends four different messages to the server and recieves the corresponding message back.
#Python; socket, argparse, datetime, string, random
#run with command line
from socket import *
from scapy.all import *
import argparse
import random


parser = argparse.ArgumentParser()
parser.add_argument("-i","--internet", help="Sets IP Address for client: ", type=str)
parser.add_argument("-p","--port", help="Sets Port for client: ", type=int)
parser.add_argument("-m","--msg", help="Sets the msg for the client: ", type=str)
args = parser.parse_args()

serverIP = args.internet
serverPort = args.port
serverMsg = args.msg
clientSocket = socket(AF_INET, SOCK_DGRAM)

protocolType = "A"
protocolLength = len(message + serverMsg)
protocolPort = serverPort
protocolRand = random.randint(0,9)
protocolField = syn = IP(dst="10.20.232.22")/TCP(dport=8080, sport=45632, flags="S")
syn_ack = sr1(syn)
protocolSeq =
protocolChksum =
message = "a"
