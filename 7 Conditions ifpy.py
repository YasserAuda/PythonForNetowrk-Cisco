rtr = input('Enter the hostname:')
vendor = input('Enter the type of device:')
if ('Hawaii' in vendor) or ('hawaii' in vendor):
    print ('display current')
elif ('Juniper' in vendor) or ('juniper' in vendor):
    print ('sh configuration')
else:
    print ('sh run')
    
print ('\nExiting program...')


rtr = input('Enter Neighbor Device Type:')
Interface = input('Enter Local Interface Name:')
Speed = input('Enter Interface Speed Required:')
if ('hub' in rtr):
    print ('Remeber speed should be always auto')
elif ('10' in Speed) or ('100' in Speed):
    print ('you should set speed to auto')
else:
    print ('your setting is acceptable')

print ('\nExiting program...')






# Example file for working with conditional statements

def main():
  x, y = 10, 100

  # conditional flow uses if, elif, else  
  if(x < y):
    st= "x is less than y"
  elif (x == y):
    st= "x is same as y"
  else:
    st= "x is greater than y"
  print (st)
  
  # conditional statements let you use "a if C else b"
  st = "x is less than y" if (x < y) else "x is greater than or equal to y"
  print (st)
  
  # Python does not have support for higher-order conditionals
  # like "switch-case" in other languages
  
if __name__ == "__main__":
  main()



print("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess == 5:
	print("You win!")
else:
	print("You lose!")
	print("Game over!")
