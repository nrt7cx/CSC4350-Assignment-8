# CSC4350-Assignment-8
1. This project aims to build a reilable UDP protocol that sends a header and payload packet tfrom the client to the server and back.
2. Use the terminal in your system and cd into the folder location. Use python3 client8.py -i xxx.xx.xx.x -p xxxx -m xxxxxxxx and use python server8.py - xxxx .
3. No error checking with the message length, couldn't figure out how to handle errors with information entered in the command line. There is also no packet corrupter present. Sometimes the length of the header varies becuase of the two byte random number  ex: 0x1 = 1 and 0x1B = 27 need to find a way around this. Not entirely sure if hex() turns values into bytes, if not will need to address with .to_bytes().
