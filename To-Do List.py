tasks = []

def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            for line in f:
                tasks.append(line.strip())
    except:
        pass

def save_tasks():
    with open("tasks.txt","w") as f:
        for task in tasks:
            f.write(task+"\n")

def show_tasks():
    print("\nYour Tasks:")
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t}")

def main():
    load_tasks()
    while True:
        print("\n1.Add 2.Delete 3.View 4.Exit")
        choice = input("Choice: ")
        if choice=="1":
            t=input("Enter task: ")
            tasks.append(t)
        elif choice=="2":
            show_tasks()
            index=int(input("Task number to delete: "))
            if 0<index<=len(tasks):
                tasks.pop(index-1)
        elif choice=="3":
            show_tasks()
        elif choice=="4":
            save_tasks()
            break
        else:
            print("Invalid choice!")

if __name__=="__main__":
    main()
