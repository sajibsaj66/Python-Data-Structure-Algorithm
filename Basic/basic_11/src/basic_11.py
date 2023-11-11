# Python 2.x program to show Vulnerabilities 
# in input() function using a variable 

import random 
secret_number = random.randint(1,500) 
print ("Pick a number between 1 to 500")
while True: 
	res = input("Guess the number: ") 
	if res==secret_number: 
		print ("You win")
		break
	else: 
		print ("You lose")
		continue
