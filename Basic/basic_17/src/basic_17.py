# Python program to illustrate 
# nested for loops in Python 
from __future__ import print_function 
for i in range(1, 5): 
	for j in range(i): 
		print(i, end=' ') 
	print() 
        
# An empty loop 
for letter in 'geeksforgeeksk': 
    pass

print( 'Current Letter :', letter )


# python code to demonstrate working of enumerate() 

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']): 
	print(key, value) 
        

# initializing list 
questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 

# using zip() to combine two containers 
# and print values 
for question, answer in zip(questions, answers): 
	print('What is your {0}? I am {1}.'.format(question, answer))         

