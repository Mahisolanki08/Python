# import math
# x = float(input("Enter Number : "))
# print(math.ceil(x))

# E-commerce Logic

import math
book_price = 12.5
user_type = input("Enter You are a User or Admin : ")

if user_type == "user" or user_type == "User":
  print("Price is : ",math.ceil(book_price))

elif user_type == "admin" or user_type == "Admin":
  print("You are a Admin So you can see actual price : ",book_price)

else :
  print("You are not a user or admin so price not shown....")