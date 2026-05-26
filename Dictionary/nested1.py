students = {
  "student1" : {
    "name" : "Mahi",
    "age" : 21,
    "marks" : 98
  },
  "student2" : {
    "name" : "Anjali",
    "age" : 21,
    "marks" : 78
  },
  "student3" : {
    "name" : "Palak",
    "age" : 21,
    "marks" : 38
  }
}


for key,value in students.items():
  print(key)
  for k , v in value.items():
    print(k ,":", v)

  print()


