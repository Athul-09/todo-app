# Simple To-Do App (Terminal)

todo_list = []

def show_menu():
    print("\nSimple To-Do App")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

def show_list():
    if not todo_list:
        print("No tasks in your list!")
    else:
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

while True:
    show_menu()
    choice = input("Enter choice: ").strip()
    if choice == "1":
        show_list()
    elif choice == "2":
        task = input("Enter a new task: ").strip()
        if task:
            todo_list.append(task)
            print("Task added.")
    elif choice == "3":
        show_list()
        index = input("Enter task number to remove: ").strip()
        if index.isdigit():
            index = int(index)
            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
