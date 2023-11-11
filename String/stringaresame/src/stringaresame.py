
def allcharsame(s):
    for i in range(1,len(s)):
        if s[i] != s[0]:
            return False
    return True

str = "aaa"

if allcharsame(str):
   print("All Same")
else:
   print("Not Same")
    
    