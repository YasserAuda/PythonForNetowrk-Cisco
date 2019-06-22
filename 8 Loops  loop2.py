#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

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
