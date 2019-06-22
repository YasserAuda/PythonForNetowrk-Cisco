#pip install python-nmap
import nmap
nm = nmap.PortScanner()
print(nm.nmap_version())
nm.scan('192.168.1.1', '1-1024', '-v')
# get nmap scan informations
print(nm.scaninfo())
print(nm.csv())
