print('''
  + ADD
  - SUBTRACT
  * MULTIPLY
  / DIVISION    
''')

num1 = int(input("Enter The Value1 : "))
num2 = int(input("Enter The Value2 : "))
opr = input("Enter The Opr....(+,-,*,/)")
if opr == "+" :
  print(num1 + num2)

elif opr == "-" :
  print(num1 - num2)

elif opr == "*" :
  print(num1 * num2)

elif opr == "/" :
  print(num1 / num2)

else :
  print("Invalid opr.....")