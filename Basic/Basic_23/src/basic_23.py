# Python program to illustrate functions 
# Functions can return another function 

def create_adder(x): 
	def adder(y): 
		return x+y 

	return adder 

add_15 = create_adder(15) 

print (add_15(10)) 

# Python program to illustrate 
# nested functions 
def outerFunction(text): 
	text = text 

	def innerFunction(): 
		print(text) 

	innerFunction() 

if __name__ == '__main__': 
	outerFunction('Hey!') 
