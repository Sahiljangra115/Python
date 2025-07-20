import os
TASK_FILE = "tasks.txt"  # all caps here means that we are saying that it should not be changed

def load_task():
    tasks = []
    # if(os.path.exists(TASK_FILE))
    if(os.path.exists("tasks.txt")):
        with open("tasks.txt", "r") as f:
        # with open(TASK_FILE, "r") as f:
            for line in f:
                text, status = line.strip().rspilt("||", 1)
                tasks.append({"task": text, "done": status == "done"})
        return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding = "utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task["text"]}||{status}\n")

def display(tasks):
    if not tasks:
        print("No task to display")
    else:
        for i, task in enumerate(1, tasks):
            checkbox = "&" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()  # prints new line

def task_manger():
    tasks = load_task()

    while True:
        print("\n---------------- Task Manager ----------------")
        print("1. Add a new Task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()
        match choice:
            case "1":
                text = input("Enter your task").strip()
                if text:
                    tasks.append({"text": text, "done":False})
                    save_tasks(tasks)
                else:
                    print("Task cannot be empty")
            case "2":
                display(tasks)
            case "3":
                display(tasks)
                try:
                    num = int(input("Enter task number"))
                    if 1<= num <=len(tasks):
                        tasks[num-1]["done"] = True   # this is done because the array behaviour doesnot change enumerate changes the display style only
                        save_tasks(tasks)
                        print("task marked as done")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "4":
                display(tasks)
                try:
                    num = int(input("Enter task number"))
                    if 1<= num <=len(tasks):
                        removed = tasks.pop(num-1)
                       
                        save_tasks(tasks)
                        print("task removed")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "5":
                print("Exiting task manager")
                break
            case _:
                print("Please choose a valid option")

task_manger()