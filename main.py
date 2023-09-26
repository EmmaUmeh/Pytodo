# main.py
from addtodo import add_task
from viewtodo import view_tasks
from deletetodo import mark_done

# Define an empty list to store tasks
tasks = []

# Main loop
while True:
    print('\nOptions:')
    print('1. Add a task')
    print('2. View tasks')
    print('3. Mark a task as done')
    print('4. Quit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        task = input('Enter the task: ')
        add_task(tasks, task)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        view_tasks(tasks)
        task_number = int(input('Enter the task number to mark as done: '))
        mark_done(tasks, task_number)
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please select a valid option.')
