n = int(input("Enter a Number : "))
def palindrome_number(a):
  reverse = 0
  original = a

  while (a > 0) :
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a//10

  if original == reverse :
    return ("Number is Palindrome")
  
  else :
    return ("Not a Palindrome Number ")

print(palindrome_number(n))