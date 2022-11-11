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

serverSocket = socket(AF_INET,SOCK_DGRAM) 
serverSocket.bind(('',serverPort))
print ("The server is ready to receieve")

while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(message)
    
        if(message.decode() == "Send IP"):
            modifiedMessage = "OK: " + clientAddress[0]
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            
        elif(message.decode() == "Send Port"):
            modifiedMessage = "OK: " + str(clientAddress[1])
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            
        elif(message.decode()[0:9] == "TimeDelay"):
            modifiedMessage = "OK: " 
            print(modifiedMessage)
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
           
        elif(message.decode() == "Quit"):
            modifiedMessage = "OK: Quit Program"
            print(modifiedMessage)
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)

        else: 
            modifiedMessage = "INVALID"
            serverSocket.sendto(modifiedMessage.encode(),clientAddress)
            