list = []

while True :
  c = int(input('''
            1 Push Elements
            2 Pop Elements
            3 First Elements
            4 Last Elements
            5 Display Elements
            6 Exit
          '''))
  
  if c == 1 :
    n = int(input("Enter The Value : "))
    list.append(n)
    print(list)

  elif c == 2 :
    if len(list) == 0 :
      print("Empty Queue")

    else :
      p = list.pop()
      print(p)
      print(list)

  elif c == 3 :
    if len(list) == 0:
      print("Empty Queue")

    else :
      print("First Value of Queue: ",list[0])

  elif c == 4 :
    if len(list) == 0 :
      print("Empty Queue")
    
    else :
      print("Last Value of Queue : ",list[-1])
  
  elif c == 5 :
    print("Display Stack : ",list)

  elif c == 6 :
    break

  else :
    print("Invalid Operation")