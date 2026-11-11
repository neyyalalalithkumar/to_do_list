tasks = []

#print("/n ------- TO - DO LIST ------")
#print("1. Add Task: ")
#print("2. view Task: ")
#print("3. Marked as Done: ")
#print("4. Delete the Task: ")
#print("5. Exit: ")
def show_menu():
    print("\n------- TO-DO LIST -------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Delete a Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task":task , "done":False})
    print(f"task '{task}' added! ")
    
def view_task():
    if not tasks:
        print("No tasks yet!")
        return
    
    print("\nyour Tasks:")
    
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['task']} [{status}]")
        
def mark_done():
    view_task()
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to mark done: ")) -1
        
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done!")
            
        else:
            print("Invalid number!")
            
    except ValueError:
        print("please enter a valid number. ")
        
def delete_task():
    view_task()
    if not tasks:
        return
    try :
        index = int(input("Enter Task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Delete task: {removed['task']}")
        else:
            print("Invalid number!")
            
    except ValueError:
        print("please enter a valid number !")
        
        
while True:
        show_menu()
        choice = input("choice on option (1-5): ")
        
        if choice == '1':
            add_task()
            
        elif choice == '2':
            view_task()
            
        elif choice == '3':
            mark_done()
            
        elif choice == '4':
            delete_task ()
            
        elif choice == '5':
            print("Good bye!")
            break
        else:
            print("Invalid choice try again.")