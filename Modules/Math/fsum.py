import math 
# l = [10,20,30,40]
# print(math.fsum(l))

list = []
element = int(input("Length of list : "))
for i in range (element) :
  values = int(input("Enter Value : "))
  list.append(values)

print("The list is : ",list)
print("Sum of give list is : ",math.fsum(list))