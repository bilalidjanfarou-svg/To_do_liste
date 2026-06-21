def to_do_liste():
    tasks = []

    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")

        choose = input("Choose an option: ")

        if choose == "1":
            task = input("Enter a task: ")
            tasks.append(task)

        elif choose == "2":
            task = input("Task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")

        elif choose == "3":
            print("\nTasks:")
            if len(tasks) == 0:
                print("No tasks.")
            else:
                for task in tasks:
                    print("- " + task)

        elif choose == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

to_do_liste()