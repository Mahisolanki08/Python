def add(a,b):
  return a + b

def subtract(a,b) :
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a/b

while True :
  print("\n =======Calculator Menu=======")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Divide")
  print("5. Exit")

  choice = int(input("Enter Choice between (1-5) : "))

  if choice == 5 :
    print("Exiting Calculator......Bye")
    break

  if choice in (1,2,3,4):
    num1 = int(input("Enter 1st Number : "))
    num2 = int(input("Enter 2nd Number : "))

    if choice == 1 :
      print("Addition is : ",add(num1,num2))

    elif choice == 2:
      print("Subtraction is : ",subtract(num1,num2))

    elif choice == 3:
      print("Multiplication is : ",multiply(num1,num2))

    elif choice == 4:
      print("Divide is :",divide(num1,num2))

  else :
    print("Invalid Choice !Please Select (1-5)")

