import socket

HOST = socket.gethostname()
PORT = 21505
print(HOST)

sock = socket.socket()
#(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall("It's late at night")

data = s.recv(1024)
sock.close()
print("Received response from server as: " + repr(data))
