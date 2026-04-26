from task_manager import TaskManager
from utils import print_menu, print_tasks


def main():
    manager = TaskManager()

    while True:
        print_menu()
        choice = input("Изберете опция: ")

        if choice == "1":
            title = input("Въведете заглавие на задачата: ")
            manager.add_task(title)
            print("Задачата е добавена успешно.")

        elif choice == "2":
            tasks = manager.list_tasks()
            print_tasks(tasks)

        elif choice == "3":
            task_id = int(input("Въведете ID на задачата: "))
            if manager.complete_task(task_id):
                print("Задачата е маркирана като завършена.")
            else:
                print("Задача с такова ID не е намерена.")

        elif choice == "4":
            task_id = int(input("Въведете ID на задачата: "))
            if manager.delete_task(task_id):
                print("Задачата е изтрита.")
            else:
                print("Задача с такова ID не е намерена.")

        elif choice == "5":
            keyword = input("Въведете дума за търсене: ")
            results = manager.search_tasks(keyword)
            print_tasks(results)

        elif choice == "0":
            print("Изход от програмата.")
            break

        else:
            print("Невалидна опция.")


if __name__ == "__main__":
    main()