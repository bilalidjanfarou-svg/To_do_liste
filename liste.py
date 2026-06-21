def to_do_liste():
    task={}
    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. Show task")
        print("4. Exit")
        choose=input("Choose your task")
        if choose == "1":
            task = input("Enter task")
            tasks.append(task)
        elif choose == "2":
            task = input("Remove task")
            if task in tasks:
                tasks.remove(task)
            else:
                    print("Task not found")
        elif choose == "3":
            print("Task: ")
            for task in tasks:
                print("_"+task)
        elif choose == "4":
            break
        else:
            to_do_liste()
to_do_liste()
            



