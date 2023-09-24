my_list=[]

while True:
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Quit")

    option =input("Enter your option (1/2/3/4):")

    if option=="1":
        task=input("Enter a task:")
        my_list.append(task)
        print("Task added to To-Do list")

    elif option=="2":
        if not my_list:
            print("To-Do list is empty")
        else:
            print("\nTo-Do List:")
            print("\nTo-Do List:")
            for index, task in enumerate(my_list, start=1):
                print(f"{index}. {task}")

    elif option == "3":
        if not my_list:
            print("The to-do list is empty.")
        else:
            try:
                task_index = int(input("Enter the task number to mark as done: "))
                if 1 <= task_index <= len(my_list):
                    task_done = my_list.pop(task_index - 1)
                    print(f"Marked '{task_done}' as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Enter a valid task number.")

    elif option == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please enter a valid option (1/2/3/4).")
