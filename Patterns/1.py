'''
*
* *
* * *
* * * *
'''

# for i in range (1,5) :
#   for j in range (i) :
#     print("*",end=" ")
#   print()

n = int(input("Enter Number Rows : "))

for i in range (1,n):
  for j in range(i):
    print("*",end=" ")
  print()