# Logic improvements v2
from storage import load_tasks, save_tasks
from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title):
        task_id = self._generate_task_id()
        task = Task(task_id, title)
        self.tasks.append(task)
        save_tasks(self.tasks)

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                save_tasks(self.tasks)
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                save_tasks(self.tasks)
                return True
        return False

    def search_tasks(self, keyword):
        return [
            task for task in self.tasks
            if keyword.lower() in task.title.lower()
        ]

    def _generate_task_id(self):
        if not self.tasks:
            return 1
        return max(task.task_id for task in self.tasks) + 1