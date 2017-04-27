"""Gathumbi Collins Githiari
A program to show implementation of Server client Architecture using sockets."""
import socket
import sys

host = '169.254.155.149'
port = 21505
print("Stating up on Address "+host+" and on Port "+str(port))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

while True:
    print("Waiting for a connection like...")
    conn, client_addr = sock.accept()
    try:
        print ("\nConnection from " + repr(client_addr)+ " started")
        while True:
            data = conn.recv(256)
            print("Here's what we received from the client: " +str(data))
            if data:
                resp = "Message received, will do :D"
                print("Sending data back to client as: "+resp)
                conn.sendall(bytes(resp, 'UTF-8'))
            else:
                print("That's all the data we have for now! :-}\n")
                break
    
    finally:
        conn.close()

