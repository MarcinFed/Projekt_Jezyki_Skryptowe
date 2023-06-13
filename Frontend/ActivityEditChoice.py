from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from Frontend.AddActivity import AddActivityWindow


class ActivityEditChoiceWindow(QMainWindow):  # Window for choosing the edit for activity
    def __init__(self, previous_window, activity, activity_list):
        super().__init__()

        self.previous_window = previous_window
        self.activity = activity
        self.activity_list = activity_list
        self.add_activity_window = None

        self.setWindowTitle("Edycja")  # Set the window title
        self.setWindowIcon(QIcon("Frontend\\Logo.jpg"))  # Set the window icon
        self.setMinimumWidth(200)  # Set the minimum width of the window

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()
        self.question_label = QLabel("Co chcesz zrobić ?")
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.question_label)

        self.middle_layout = QHBoxLayout()

        # Create edit button
        self.edit_button = QPushButton("Edytuj")
        self.edit_button.setStyleSheet("background-color: darkblue; color: black;")
        self.edit_button.clicked.connect(self.edit)

        # Create delete button
        self.delete_button = QPushButton("Usuń")
        self.delete_button.setStyleSheet("background-color: darkred; color: black;")
        self.delete_button.clicked.connect(self.delete)

        self.middle_layout.addWidget(self.delete_button)
        self.middle_layout.addWidget(self.edit_button)

        self.bottom_layout = QVBoxLayout()

        # Create cancel button
        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkorange; color: black;")
        self.cancel_button.clicked.connect(self.cancel)

        self.bottom_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addLayout(self.bottom_layout)

    def cancel(self):
        # Close the window and show the previous window
        self.close()
        self.previous_window.show()

    def delete(self):
        # Remove the activity from the activity list, update the previous window, and show the previous window
        self.activity_list.remove(self.activity)
        self.close()
        self.previous_window.update_items()
        self.previous_window.disable_edit()
        self.previous_window.show()

    def edit(self):
        # Open the AddActivityWindow to edit the activity
        self.add_activity_window = AddActivityWindow(self.previous_window, activity=self.activity, day=None)
        self.close()
        self.add_activity_window.show()
