# CSC4350-Assignment-8
1. This project aims to build a reilable UDP protocol that sends a header and payload packet tfrom the client to the server and back.
2. Use the terminal in your system and cd into the folder location. Use python3 client8.py -i xxx.xx.xx.x -p xxxx -m xxxxxxxx and use python server8.py - xxxx .
3.Program now fucntions somewhat as intended. The client sends a message which has a 1/10 chance to be corrupted on the client side. The server then processes this message accordingly and has a 1/10 chance to drop the packet or send the corresponding ACK or NACK. Although this fucntions as indendended, when faced with a back to back packet drop the program will still forget to append an ACK or a NACK to the final message. The checksum field is also still one byte which is not what the assignment called for.
