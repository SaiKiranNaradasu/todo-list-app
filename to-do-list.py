def display_menu():
    print("\n==== SECRET AGENCY TO-DO LIST ====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. {task['title']} (Priority: {task['priority']}) - {status}")


def add_task(tasks):
    title = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ")
    tasks.append({"title": title, "done": False, "priority": priority})
    print("Task added!")


def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            tasks[task_num - 1]["done"] = True
            print("Task marked as completed!")
        except (ValueError, IndexError):
            print("Invalid task number!")


def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed['title']}")
        except (ValueError, IndexError):
            print("Invalid task number!")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye, Agent!")
            break
        else:
            print("Invalid option, try again!")


if __name__ == "__main__":
    main()
