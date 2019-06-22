#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco


#print out numbers 2,3,,5,7
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):   
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)


# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
# Check if x is even
    if x % 2 == 0:   
        continue
    print(x)
    
    
    
for x in range(1,255):
    print ("192.168.95."+str(x))
    

portList = [21,22,25,80,110]
for port in portList:
    print (port)
    
portList = [21,22,25,80,110]
for x in range(1,255):
    for port in portList:
        print ("[+] Checking 192.168.95."\
            +str(x)+": "+str(port)) 
            
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break


a=[]
n=int(input("Enter number of ports to create List:"))
for i in range(1,n+1):
    b=input("Enter port number:")
    a.append(b)
a.sort(key=len)
print(a)


Devcie_List=["R1 2911","R2 2811","R3 900","Catalyst 9200","Catalyst 2650"]
print(Devcie_List)
for item in Devcie_List:
    print(item)
for item in Devcie_List:
	if "Catalyst" in item: print(item)
	
Catalyst_Switch_List=[]
for item in Devcie_List:
	if "Catalyst" in item: Catalyst_Switch_List.append(item)
	print(Catalyst_Switch_List)
	
	
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


def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end='')

if __name__ == "__main__": main()


def main():
    s = 'this is a string'
    for c in s:
        print(c, end='')

if __name__ == "__main__": main()


def main():
    s = 'this is a string'
    for c in s:
        if c == 's': break
        print(c, end='')

if __name__ == "__main__": main()



from random import randint
secret = randint(1, 10)
print('Welcome')

guess = 0
while guess != secret:
	g = input('Guess the number: ')
	guess = int(g)
	if guess == secret:
		print('You win!')
    
	elif guess > secret:
		print('Too high')
	else:
		if guess < secret:	print('Too low')
	
print('Game over!')



# Example file for working with loops

def main():
  x = 0
  
  # define a while loop
  while (x < 5):
     print (x)
     x = x + 1

  # define a for loop
  for x in range(5,10):
    print (x)
    
  # use a for loop over a collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)
  
  # use the break and continue statements
  for x in range(5,10):
    #if (x == 7): break
    #if (x % 2 == 0): continue
    print (x)
  
  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print (i, d)
  
if __name__ == "__main__":
  main()



