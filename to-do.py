tasks = []

while True :
  print("\n____To-Do____")
  print("1. Add Task")
  print("2. View Task")
  print("3. Delete Task")
  print("4. Exit")

  choice = int(input("Enter Choice between (1-4) : "))

  if choice == 1 :
    task = input("Enter Task : ")
    tasks.append(task)
    print("Task added successfully.....")

  elif choice == 2 :
    if len(tasks) == 0:
      print("No tasks available.")

    else :
      print("\nYour Tasks:")
      for i in range (len(tasks)) :
        print(f"{i+1}.{tasks[i]}")

  elif choice == 3:
    if len(tasks) == 0:
      print("No tasks available.")

    else :
      print("\nYour Tasks:")
      for i in range (len(tasks)) :
        print(f"{i+1}.{tasks[i]}")

      index = int(input("Enter task number to delete : "))
      tasks.pop(index-1)
      print("Task delete Successfully!")

  elif choice == 4 :
    print("Thank you for using To-Do List")
    break

  else :
    print("Invalid Choice!")