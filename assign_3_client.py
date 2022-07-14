'''
Author: Josh Bellingham        
Version: 05/12/22
Description: A program to send numbers from a counter via a server socket (client side)
'''

import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 5490

soc.connect((HOST, PORT))

while True:
    print(soc.recv(2048).decode('utf-8'))
    