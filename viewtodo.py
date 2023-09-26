# viewtodos.py
def view_tasks(task_list):
    if not task_list:
        print('No tasks yet.')
    else:
        print('Tasks:')
        for i, task in enumerate(task_list, start=1):
            print(f'{i}. {task}')
