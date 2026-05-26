num1 = int(input("Enter The Value1 : "))
num2 = int(input("Enter The Value2 : "))
opr = input("Enter Opr...(+,-,*,/) : ")

if opr == "+" :
  print(num1 + num2)

if opr == "-" :
  print(num1 - num2)

if opr == "*" :
  print(num1 * num2)

if opr == "/" :
  print(num1 / num2)

if (opr != "+" and opr != "-" and opr != "*" and opr != "/") :
  print("Invalid opr.....")