from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QDateEdit,
    QTimeEdit
)

from PyQt6.QtCore import QDate, QTime

from task_manager import TaskManager


class TaskManagerGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.manager = TaskManager()

        self.setWindowTitle("Task Manager")
        self.resize(800, 500)

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Task Title")
        layout.addWidget(self.title_input)

        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setDisplayFormat("dd-MM-yyyy")
        layout.addWidget(self.date_edit)

        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QTime.currentTime())
        self.time_edit.setDisplayFormat("HH:mm")
        layout.addWidget(self.time_edit)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.load_tasks()

    def load_tasks(self):

        tasks = self.manager.get_tasks()

        self.table.clearContents()

        self.table.setRowCount(len(tasks))
        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Title",
            "Status",
            "Priority",
            "Date",
            "Time"
        ])

        for row, task in enumerate(tasks):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(task.title)
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    "Done" if task.completed else "Pending"
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(task.priority)
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(task.due_date)
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(task.due_time)
            )

    def add_task(self):

        title = self.title_input.text().strip()

        if not title:
            return

        due_date = self.date_edit.date().toString(
            "dd-MM-yyyy"
        )

        due_time = self.time_edit.time().toString(
            "HH:mm"
        )

        self.manager.add_task(
            title,
            "Low",
            due_date,
            due_time
        )

        self.title_input.clear()

        self.load_tasks()

    def delete_task(self):

        row = self.table.currentRow()

        if row >= 0:
            self.manager.remove_task(row)
            self.load_tasks()