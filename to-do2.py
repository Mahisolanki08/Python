tasks = []

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

while True:
    print("\n____To-Do____")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter Choice between (1-4) : "))

    if choice == 1:
        task = input("Enter Task : ")
        tasks.append(task)
        print("Task added successfully!")
        view_tasks(tasks)

    elif choice == 2:
        view_tasks(tasks)

    elif choice == 3:
        view_tasks(tasks)

        if len(tasks) > 0:
            index = int(input("Enter task number to delete : "))

            if 1 <= index <= len(tasks):
                tasks.pop(index - 1)
                print("Task deleted successfully!")
                view_tasks(tasks)
            else:
                print("Invalid task number!")

    elif choice == 4:
        print("Thank you for using To-Do List")
        break

    else:
        print("Invalid Choice!")