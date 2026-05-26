n = int(input("Enter a Number : "))
def reverse_number(a):
  reverse = 0 

  while a > 0 :
    digits = a%10
    reverse = reverse * 10 + digits
    a = a//10

  return reverse

print(reverse_number(n))