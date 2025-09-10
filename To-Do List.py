# To-Do List App
# By Raje

FILE = "todo.txt"

def add_task():
    task = input("Enter task: ")
    with open(FILE, "a") as f:
        f.write(task + "\n")
    print("✅ Task added!\n")

def view_tasks():
    try:
        with open(FILE, "r") as f:
            tasks = f.readlines()
        if not tasks:
            print("⚠️ No tasks found.\n")
            return
        print("\n--- To-Do List ---")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t.strip()}")
        print()
    except FileNotFoundError:
        print("⚠️ No tasks found.\n")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    with open(FILE, "r") as f:
        tasks = f.readlines()
    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        with open(FILE, "w") as f:
            f.writelines(tasks)
        print("✅ Task deleted!\n")
    else:
        print("❌ Invalid task number!\n")

def main():
    while True:
        print("===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        ch = input("Enter choice: ")
        if ch == "1": add_task()
        elif ch == "2": view_tasks()
        elif ch == "3": delete_task()
        elif ch == "4": break
        else: print("⚠️ Invalid choice!\n")

if __name__ == "__main__":
    main()
