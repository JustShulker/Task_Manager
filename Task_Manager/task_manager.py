import json
from task import Task

FILE_NAME = "tasks.json"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            self.tasks = [Task.from_dict(task) for task in data]

        except:
            self.tasks = []

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(
                [task.to_dict() for task in self.tasks],
                file,
                indent=4
            )

    def add_task(self, title, priority, due_date, due_time):
        task = Task(title, priority, due_date, due_time)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            return removed

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def get_tasks(self):
        return self.tasks