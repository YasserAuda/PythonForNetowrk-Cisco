#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

portList = [21,22,25,80,110]
for x in range(1,255):
    for port in portList:
        print ("[+] Checking 192.168.95."\
            +str(x)+": "+str(port))   
