
    # deletetodo.py
def mark_done(task_list, task_number):
    if 1 <= task_number <= len(task_list):
        task = task_list.pop(task_number - 1)
        print(f'Task "{task}" marked as done.')
    else:
        print('Invalid task number.')
