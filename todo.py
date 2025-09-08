# Simple To-Do App (Terminal) with Title and User Name

def title_card(user_name):
    print("="*34)
    print(f"     {user_name}'s TO-DO LIST APP".center(34))
    print("="*34)

def show_menu():
    print("\nMenu:")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

def show_list(todo_list):
    if not todo_list:
        print("No tasks in your list!")
    else:
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def main():
    user_name = input("Enter your name: ").strip()
    if not user_name:
        user_name = "User"
    todo_list = []

    while True:
        title_card(user_name)
        show_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            show_list(todo_list)
        elif choice == "2":
            task = input("Enter a new task: ").strip()
            if task:
                todo_list.append(task)
                print("Task added.")
        elif choice == "3":
            show_list(todo_list)
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

if __name__ == "__main__":
    main()
print("ive supposedly added a delete feature")
print("AYoo nothing again")