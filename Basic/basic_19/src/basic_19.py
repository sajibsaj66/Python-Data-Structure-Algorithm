# Here x is a new reference to same list lst 
def myFun(x): 
 x[0] = None

# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15] 
myFun(lst); 
print(lst) 

def myFun(x): 

# After below line link of x with previous 
# object gets broken. A new object is assigned 
# to x. 
 x = [20, 30, 40] 

# Driver Code (Note that lst is not modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15] 
myFun(lst); 
print(lst) 

def myFun(x): 

# After below line link of x with previous 
# object gets broken. A new object is assigned 
# to x. 
 x = 20

# Driver Code (Note that lst is not modified 
# after function call. 
x = 10
myFun(x); 
print(x) 


def swap(x, y): 
	temp = x; 
	x = y; 
	y = temp; 

# Driver code 
x = 2
y = 3
swap(x, y) 
print(x) 
print(y) 
# Python program to demonstrate 
# default arguments 
def myFun(x, y=50): 
	print("x: ", x) 
	print("y: ", y) 

# Driver code (We call myFun() with only 
# argument) 
myFun(10) 
# Python program to demonstrate Keyword Arguments 
def student(firstname, lastname): 
	print(firstname, lastname) 
	
	
# Keyword arguments				 
student(firstname ='Geeks', lastname ='Practice')	 
student(lastname ='Practice', firstname ='Geeks') 
