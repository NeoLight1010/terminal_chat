# /home/neolight1010/anaconda3/bin/python /home/neolight1010/Documents/Coding/terminal_chat/client.py

import socket
import threading
from term_func import *

PORT = 6166
SERVER = "192.168.0.189"
CLIENT = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 128
FORMAT = "utf-8"
DISCONNECT = "DISCONNECT"

connected = True

def send_msg(): # send message to server
    global connected
    while connected:
        msg = input(low_prior("(" + CLIENT + "): "))

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
            print(low_prior("\n[MESSAGE]:") + f" {msg}") # Print relayed messages from SERVER

def print_local_address():
    local_address = socket.gethostbyname(socket.gethostname())
    print(high_prior("[CONNECTING]: ") + f"Local address is {local_address}")

def main():
    recv_msg_thread = threading.Thread(target=recv_msg) # Initialize receive-message thread
    recv_msg_thread.start()

    send_msg_thread = threading.Thread(target=send_msg) # Initialize send-message thread
    send_msg_thread.start() 

## SOCKET INITIALIZATION ##

print(high_prior("[CONNECTING]: ") + "Trying to connect to " + low_prior(str(ADDR)))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print_local_address()

###########################

if __name__ == "__main__":
    main()