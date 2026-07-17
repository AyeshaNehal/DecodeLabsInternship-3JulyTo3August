my_tasks=[]

while True:
    print("---------My To-Do List---------")
    print("1.Add A Task")
    print("2.View Tasks")
    print("3.Exit The Program")

    choice=input("Enter Your Choice of Action:")
    if choice=="1":
        task=input("Enter a New Task:")
        my_tasks.append(task)
        print("Task Added Successfully!")

    elif choice=="2":
        if len(my_tasks)==0:
            print("There Are No Tasks in The To-Do List!")
        else:
            print("Your Tasks:")
            for x in range(len(my_tasks)):
                print(my_tasks[x])
                
                

    elif choice=="3":
        print("Exiting The To-Do List!")
        break
    else:
        print("Invalid Choice of Option, Please Try Again.")





