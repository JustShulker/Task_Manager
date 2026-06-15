class Task:
    def __init__(self, title, priority, due_date, due_time):
        self.title = title
        self.completed = False
        self.priority = priority
        self.due_date = due_date
        self.due_time = due_time

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed,
            "priority": self.priority,
            "due_date": self.due_date,
            "due_time": self.due_time
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["priority"],
            data["due_date"],
            data["due_time"]
        )
        task.completed = data["completed"]
        return task