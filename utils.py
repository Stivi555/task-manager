def print_task(task):
    status = "Завършена" if task.completed else "Незавършена"
    print(f"{task.task_id}. {task.title} - {status}")


def print_tasks(tasks):
    if not tasks:
        print("Няма намерени задачи.")
        return

    for task in tasks:
        print_task(task)


def print_menu():
    print("\n=== Task Manager ===")
    print("1. Добавяне на задача")
    print("2. Показване на всички задачи")
    print("3. Маркиране на задача като завършена")
    print("4. Изтриване на задача")
    print("5. Търсене на задача")
    print("0. Изход")