#C:\Users\yasser>pip install Exscript

from Exscript.util.interact import read_login
from Exscript.protocols import SSH2
account = read_login()
conn = SSH2()
conn.connect('192.168.1.50')
conn.login(account)
conn.execute('show ip route')
print (conn.response)
conn.send('exit\r')
conn.close()
