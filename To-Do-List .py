tasks = []
while True:
    print("1. Add task: ")
    print("2. List the tasks:")
    print("3. Delete a task")
    print("4. exit")

    choice = input("choise one of them: ")
    if choice == "1":  #if we choose 1, new task will be added.
        new_task = input("write your new task: ")
        tasks.append(new_task) # the task will be added in the tasks list.
        print("new task added!")

    elif choice == "2":
        if len(tasks) == 0:  # we check if the task list empty or not.
            print("no tasks here. ")
        else:
            print("Task Lists: ")

    elif choice == "3":  #if choose 3 lets delete the task.
        deleting = int(input("Enter the number of the task u want to delete: "))
        if 1 <= deleting <= len(tasks):
            deleted = tasks.pop(deleting -1)
            print(f"deleted task: {deleted}") #prints the name of the deleted atsk and gives info to users.
        else: #if the enetred atsk number is not valid range
            print("invalid task number")









