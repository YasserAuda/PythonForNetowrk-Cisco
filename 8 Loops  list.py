#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

a=[]
n=int(input("Enter number of ports to create List:"))
for i in range(1,n+1):
    b=input("Enter port number:")
    a.append(b)
a.sort(key=len)
print(a)
