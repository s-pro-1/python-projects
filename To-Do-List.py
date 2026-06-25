def add_task():
    task = input("Enter your task: ")
    with open("tasks.txt", "a") as file:
        file.write("TODO - " + task + "\n")
    print("Task added successfully!")

def view_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if not tasks:
        print("No tasks found!")
        return
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task.rstrip()}")

def mark_complete():
    view_task()
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    try:
        task_number = int(input("Enter task number to mark complete: "))
        index = task_number - 1
        if 0 <= index < len(tasks):
            tasks[index] = tasks[index].replace("TODO", "DONE")
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_task()
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    try:
        task_number = int(input("Enter task number to delete: "))
        index = task_number - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

choice = 0

while choice != 5:
    print("\n\t===== To Do List =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_complete()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("Goodbye!")
    else:
        print("Invalid choice! Pick between 1-5.")