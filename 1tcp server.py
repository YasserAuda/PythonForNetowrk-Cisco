import socket
T_PORT = 60
TCP_IP = '127.0.0.1'
BUF_SIZE = 30
# create a socket object name 'k'
k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
k.bind((TCP_IP, T_PORT))
k.listen(1)
con, addr = k.accept()
print ('Connection Address is: ' , addr)
while True :
    data = con.recv(BUF_SIZE)
if not data:
    sys.exit()
print ("Received data", data)
con.send(data)
con.close()
