x=input("Enter the number to count: ")
x=int(x)
y=1
while y<=x:
   print(y)
   y=y+1
   
#while y less than or equal to x , keep printing y
#while statement repeats the loop until a test is not met.
#current y value will be incremnted by 1  



# Prints out 0,1,2,3,4
count = 0

while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# Prints out 0,1,2,3,4
count = 0

while True:
    print(count)
    count += 1
    if count >= 5: 
        break
#another example
print("Welcome!")
guess = 0
while guess != 5:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == 5:
        print("You win!")
    else:
       if guess > 5:
          print("Too high")
       else: print("Too low")
print("Game over!")
