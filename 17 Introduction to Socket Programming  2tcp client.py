import socket

T_PORT = 60

TCP_IP = '127.0.0.1'

BUF_SIZE = 30

MSG = "Hello karl".encode()

# create a socket object name 'k'

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.connect((TCP_IP, T_PORT))

k.send(MSG)

data = k.recv(BUF_SIZE)

k.close
