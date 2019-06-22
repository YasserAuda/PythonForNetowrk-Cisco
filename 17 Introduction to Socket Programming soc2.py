import socket
from urllib.parse import urlparse
URLS = [
'http://www.python.org',
'https://www.mybank.com',
'ftp://prep.ai.mit.edu',
'gopher://gopher.micro.umn.edu',
'smtp://mail.example.com',
'imap://mail.example.com',
'imaps://mail.example.com',
'pop3://pop.example.com',
'pop3s://pop.example.com',
]
for url in URLS:
	parsed_url = urlparse(url)
	port = socket.getservbyname(parsed_url.scheme)
	print('{:>6} : {}'.format(parsed_url.scheme, port))
