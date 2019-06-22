#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

#	Python Program to Map Two Lists into a Dictionary 
keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is:")
print(d)

#Enter number of elements for dictionary:4
#For keys:
#Enter element1:1
#Enter element2:2
#Enter element3:3
#Enter element4:4
#For values:
#Enter element1:5
#Enter element2:6
#Enter element3:7
#Enter element4:8
#The dictionary is:
#{1: 5, 2: 6, 3: 7, 4: 8}
