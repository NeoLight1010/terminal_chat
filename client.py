# /home/neolight1010/anaconda3/bin/python /home/neolight1010/Documents/Coding/Tutorials/socket_tutorial/client.py

import socket
import threading
from term_func import *

PORT = 6166
SERVER = "192.168.0.189"
CLIENT = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT = "DISCONNECT"

connected = True

print("Trying to connect to " + low_prior(str(ADDR)))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg():
    global connected
    while connected:

        msg = input(low_prior("(" + CLIENT + ") "))

        send_msg = msg.encode(FORMAT)
        msg_length = len(send_msg)
        send_msg_length = str(msg_length).encode(FORMAT)
        send_msg_length += b' ' * (HEADER - len(send_msg_length))

        client.send(send_msg_length)
        client.send(send_msg)
        
        if (msg == DISCONNECT): # If message is DISCONNECT
            connected = False

def recv_msg(): # Receive server's message

    global connected
    while connected:
        msg = client.recv(HEADER).decode(FORMAT)

        if msg:
            print(f"[MESSAGE]: {msg}")

def print_local_address():
    local_address = socket.gethostbyname(socket.gethostname())
    print(f"Local address is {local_address}")

def main():
    print_local_address()

    recv_msg_thread = threading.Thread(target=recv_msg)
    recv_msg_thread.start()

    send_msg_thread = threading.Thread(target=send_msg)
    send_msg_thread.start() 

if __name__ == "__main__":
    main()