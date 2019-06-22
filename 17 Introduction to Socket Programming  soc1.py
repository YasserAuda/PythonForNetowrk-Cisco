import socket
hostname, aliases, addresses = socket.gethostbyaddr('192.168.1.1')
print('Hostname :', hostname)
print('Aliases :', aliases)
print('Addresses:', addresses)
