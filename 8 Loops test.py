portList = [21,22,25,80,110]
for x in range(1,255):
    for port in portList:
        print ("[+] Checking 192.168.95."\
            +str(x)+": "+str(port)) 
