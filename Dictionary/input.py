students = {}

n = int(input("How many Students you want to add : "))

for i in range (n) :
  key = input("Enter Student Key : ")
  name = input("Enter name : ")
  age = int(input("Enter age : "))

  students[key] = {
    "name" : name,
    "age" : age,
  }

  print()
print(students)