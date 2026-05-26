d = {
  "name" : "Python",
  "fees" : 8000,
  "duration" : "2Months",
}

del d["fees"]
print(d)

a = d.pop("name")
print(d)