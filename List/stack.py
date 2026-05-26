list = []

while True :
  c = int(input('''
            1 Push Elements
            2 Pop Elements
            3 Peek Elements
            4 Display Elements
            5 Exit
          '''))
  
  if c == 1 :
    n = int(input("Enter The Value : "))
    list.append(n)
    print(list)

  elif c == 2 :
    if len(list) == 0 :
      print("Empty Stack")

    else :
      p = list.pop()
      print(p)
      print(list)

  elif c == 3 :
    if len(list) == 0:
      print("Empty Stack")

    else :
      print("Last Value of Stack : ",list[-1])

  elif c == 4 :
    print("Display Stack : ",list)

  elif c == 5 :
    break

  else :
    print("Invalid Operation")