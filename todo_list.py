TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n To-Do List")
        print("1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "3":
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print(" Please enter a valid number.")
        elif choice == "4":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
