def show_menu():
    print("\n--- TO-DO MENU ---")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Edit a task")
    print("4. Remove a task")
    print("5. Exit")

def show_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks yet.")
    else:
        print("\nTasks:")
        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i]}")

def add_task(task_list):
    new_task = input("Enter a task: ")
    if new_task.strip() != "":
        task_list.append(new_task.strip())
        print("Task added.")
    else:
        print("Task cannot be empty.")

def edit_task(task_list):
    show_tasks(task_list)
    if len(task_list) > 0:
        try:
            num = int(input("Task number to edit: "))
            if num > 0 and num <= len(task_list):
                updated = input("New task text: ").strip()
                if updated:
                    task_list[num-1] = updated
                    print("Task updated.")
                else:
                    print("Empty update ignored.")
            else:
                print("Invalid number.")
        except:
            print("Please enter a valid number.")

def delete_task(task_list):
    show_tasks(task_list)
    if len(task_list) > 0:
        try:
            d = int(input("Task number to delete: "))
            if d > 0 and d <= len(task_list):
                removed = task_list.pop(d-1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except:
            print("Enter a valid number.")

# Main
tasks = []

while True:
    show_menu()
    choice = input("Choose (1-5): ")

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        edit_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid input.")

