course = {
  'php' : {
    "duration" : "3months",
    "fees" : 10000,
  },
  'java' : {
    "duration" : "2months",
    "fees" : 15000,
  },
  'python' : {
    "duration" : "2months",
    "fees" : 12000,
  },
}

print(course)
print(course["java"]["fees"])

for k, v in course.items():
  print(k,v["duration"],v["fees"])

del course["python"]["fees"]
print(course)

course["java"]["fees"] = 25000
print(course)