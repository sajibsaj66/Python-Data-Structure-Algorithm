

def leftRotate(arr,d,n):
    for i in range(d):
        leftRotateOne(arr,n)

def leftRotateOne(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr,n):
    for i in range(n):
        print("%d "%arr[i],end =" ")
            
arr = [1,2,3,4,5,6,7]
leftRotate(arr,2,7)
printArray(arr,7)
