#TO-DO Task Manager

def manage_tasks(option):
    if option == "1":
        view_tasks()
    elif option == "2":
        add_task()
    elif option == "3":
        edit_task()
    elif option == "4":
        delete_task()
    elif option == "5":
        exit()
    else:
        print("Enter a valid option number between 1 and 5")

def view_tasks():
    print("You have chosen Option 1 : View Tasks")
    try:
        with open("todo.txt" , "r") as f:
            lines = f.readlines()
            tasks = [t.strip() for t in lines]
            print(f"Your tasks: \n {tasks}")
    except Exception as e:
        print(f"[ERROR]: {e}")

def add_task():
    print("You have chosen Option 2 : Add a Task")
    new_task = input(str("Enter the Task you want to add - "))
    with open("todo.txt" , "a") as f:
        f.write(new_task + "\n")
    print(f"You have added {new_task}")

def edit_task():
    print("You have chosen Option 3 : Edit a Task")
    task_to_edit = input(str("Enter the Task you want to edit - "))

    with open("todo.txt" , "r") as f:
        tasks = f.readlines()

    print("Tasks are:",[t.strip() for t in tasks])
    
    if task_to_edit not in [t.strip() for t in tasks]:
        print(f"{task_to_edit} is not available in your todo list")
        return
    
    tasklist = []
    for t in tasks:
        if (t.strip()) == (task_to_edit):
            update_task = input(str("Enter the Update for the task :- "))
            new_t = t.replace(task_to_edit,update_task)
            tasklist.append(new_t)
        else:
            tasklist.append(t)
    with open("todo.txt" , "w") as out:
        for l in tasklist:
            out.write(l)
    print(f"{task_to_edit} updated successfully!!")

def delete_task():
    print("You have chosen Option 4 : Delete a Task")
    task_to_del = input(str("Enter the Task you want to delete - "))
    with open("todo.txt" , "r") as f:
        current_tasks = f.readlines()
    with open("todo.txt" , "w") as out:
        for t in current_tasks:
            if (t.strip()) != (task_to_del):
                    out.write(t)
            else:
                print(f"{t} is deleted")
            
if __name__ == "__main__":

    while True:
        print("Choose the action you want to perform")
        print("1.View Tasks \n2.Add a Task \n3.Edit a Task \n4.Delete a Task \n5.Exit")

        option = input("Enter the option number: ")
        manage_tasks(option)
