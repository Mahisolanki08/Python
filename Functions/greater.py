n1 = int(input("Enter 1st Number"))
n2 = int(input("Enter 2nd Number"))
def greater(a,b) :
  if (n1>n2) :
    return f"{n1} is greater"
  else :
    return f"{n2} is greater"
  
print(greater(n1,n2))