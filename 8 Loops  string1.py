#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

#Calculate the Number of Digits and Letters in a String 
string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)
