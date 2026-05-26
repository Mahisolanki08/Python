n = int(input("Enter a Number : "))

def factorail_number(a):
  fact = 1
  for i in range(1,n+1):
    fact = fact * i
  return fact
  
print(f"Factorail of {n} :",factorail_number(n))