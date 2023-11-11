

def  printInitials(name):
    
    if (len(name)==0):
        return
    
    print(name[0].upper(),end = " ")
    
    for i in range(1,len(name)):
        
        if name[i]== " ":
            print(name[i+1].upper(),end = " "),
           


def main():
    name = "Prabhat Kumar Sing"
    printInitials(name)
if __name__=="__main__":
    main()
