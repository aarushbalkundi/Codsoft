toDoList = []

def menu():
    while 1:
        print('''List of options:
              1. Add task to list
              2. Mark a particular task as done
              3. Change details of a particular task
              4. Display all tasks
              5. Exit''')
        a = input("Enter your choice(1/2/3):\t")
        if a=='1':
            b = input('Enter task name:')
            toDoList.append(b)
            print('Task added to list')
        elif a=='2':
            for i in range(len(toDoList)):
                print(i+1, toDoList[i])
            b = int(input('\nWhat is the number of the completed task: '))
            toDoList.remove(toDoList[b-1])
            print('Task marked as complete')
        elif a=='3':
            for i in range(len(toDoList)):
                print(i+1, toDoList[i])
            b = int(input('\nWhat is the number of the task you want to edit: '))
            c = input('edited task details:\n')
            toDoList[b-1] = c
            print('Task edited successfully')
        elif a=='4':
            for i in range(len(toDoList)):
                print(i+1, toDoList[i])
        else:
            exit()
menu()
