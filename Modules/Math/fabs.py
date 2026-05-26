# import math 
# x = float(input("Enter a Number : "))
# print(math.fabs(x))

# # Exapmle 

import math
payment = int(input("Enter How much to pay : "))

if payment < 0 :
  print("I think you want to pay : ",math.fabs(payment))
  answer = input("Enter yes or no : ")
  if answer == "yes" :
    print("Payment Successful........")
  elif answer == "no" :
    print("So Please give value again")
    again = int(input("Re-enter Payment Value : "))
    print("Payment successful",math.fabs(payment))
  else:
    print("You are not choice yess or no.....Payment Exit")

elif payment > 0 :
  print("You want to pay : ",payment)
  sure = input("You are Sure ?? ")
  if sure == "yes" :
    print("Payment Successful......")

else :
  print("you give 0rupees so payment is failed.......")