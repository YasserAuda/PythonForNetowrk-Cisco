#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

#Add a Key-Value Pair to the Dictionary 


key=str(input("Enter the Device type to be added:"))
value=int(input("Enter the Device model to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)

#we can change str  to int
