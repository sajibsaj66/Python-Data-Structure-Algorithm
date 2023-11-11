
def pypart(n):
    
    for i in range(0,n):
        
        for j in range(0,i+1):
            print("* ",end="")
        print()
n= 5;
pypart(n)

# Python 3.x code to demonstrate star pattern 
  
# Function to demonstrate printing pattern 
def pypart(n): 
    myList = [] 
    for i in range(1,n+1): 
        myList.append("u"*i) 
    print("\r".join(myList)) 
  
# Driver Code 
n = 5
pypart(n) 

rows = int(input("enter no of rows:"))
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()