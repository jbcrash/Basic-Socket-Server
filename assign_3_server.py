'''
Author: Josh Bellingham
Version: 05/12/22
Description: A program to send numbers from a counter via a server socket (server side)
'''
import socket
import threading

def counter(client, client_addr):
    '''function to print a string of numbers from 1-50'''
    for i in range(1, 51):
        client.send(f"{i}\n".encode('utf-8'))

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 5490

soc.bind((HOST, PORT))

print("Server started")

soc.listen(10)

try:
    while True:
        client, client_addr = soc.accept()
        print("Connected to ", client_addr)
        thread = threading.Thread(target=counter, args=(client, client_addr))
        thread.start()
except:
    print("Server closed")
    soc.close()
    