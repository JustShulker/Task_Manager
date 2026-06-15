import sys

from PyQt6.QtWidgets import QApplication

from gui import TaskManagerGUI


app = QApplication(sys.argv)

window = TaskManagerGUI()
window.show()

sys.exit(app.exec())