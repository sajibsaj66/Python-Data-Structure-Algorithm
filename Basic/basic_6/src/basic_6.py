
a = 10

def read(): 
	print (a) 

def mod1(): 
      global a 
      a = 5
      print (a) 

def mod2(): 
    a=3
    def inner(): 
        nonlocal a
        a = 132
        print (a) 
    inner() 
    print (a)  

read() 

mod1() 

read() 

mod2() 
# demonstrating without non local  
# inner loop not changing the value of outer a 
# prints 5 
print ("Value of a without using nonlocal is : ",end="") 
def outer(): 
    a = 5
    def inner(): 
        a = 10
    inner() 
    print (a) 
  
outer() 