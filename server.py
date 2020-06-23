import socket
import threading
from term_func import * # VARIABLE 'T' IS USED TO REFERENCE THE TERMINAL.

PORT = 6166
SERVER = "192.168.0.189" # socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 128
FORMAT = "utf-8"
DISCONNECT = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients_connected = []
hist = [] # message history (all clients)

def send_all_clients(msg, sender): # send data to ALL clients connected. msg: message to be sent; sender: sender of the relayed message
    for client in clients_connected:
        if client != sender and clients_connected != []: # not relay message to original sender
            client.send(msg)

def handle_client(conn, addr):
    print(medium_prior("[CLIENT CONNECTED]:") + f" {addr}") # new connection alert
    clients_connected.append(conn)
    connected = True

    discon_alert = medium_prior("[CLIENT DISCONNECTED]:") + f" {addr} has disconnected. "

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg != DISCONNECT:
                print(low_prior("(" + str(addr) + "):") + f" {msg}") # output CLIENT's message

                hist.append(msg) # add msg to client's message history
                send_all_clients(hist[-1].encode(FORMAT), conn)

            else: # if client disconnects
                clients_connected.remove(conn)
                print(discon_alert)
                send_all_clients(discon_alert.encode(FORMAT), conn)
                connected = False

    conn.close()

def start():
    print(high_prior("[STARTING]:") + " Server is starting...")
    print(high_prior("[LISTENING]:") + f" Server listening on {ADDR}")

    server.listen()

    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(medium_prior("[ACTIVE CONNECTIONS]:") + f" {threading.activeCount() - 1}")
    
start()