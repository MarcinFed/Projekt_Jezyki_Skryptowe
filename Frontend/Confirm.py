from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class ConfirmWindow(QMainWindow):  # Confirm decision window
    def __init__(self, window, element):
        super().__init__()

        self.previous_window = window  # Reference to the previous window
        self.element = element  # The element to be confirmed for deletion

        self.setWindowTitle("Edycja")  # Set the window title to "Edycja"
        self.setWindowIcon(QIcon("Logo.jpg"))  # Set the window icon using the provided image file "Logo.jpg"
        self.setMinimumWidth(300)  # Set the minimum width of the window to 300 pixels

        self.central_widget = QWidget()  # Create a central widget to hold the main layout
        self.setCentralWidget(self.central_widget)  # Set the central widget for the main window

        self.main_layout = QVBoxLayout(self.central_widget)  # Create a vertical layout as the main layout

        self.top_layout = QVBoxLayout()  # Create a vertical layout for the top section
        self.question_label = QLabel("Czy na pewno chcesz usunąć " + self.element + " ?")  # Create a label with a confirmation question
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Set the alignment of the label to center
        self.question_label.setStyleSheet("font-weight: bold;")  # Apply a bold font style to the label
        self.top_layout.addWidget(self.question_label)  # Add the label to the top layout

        self.bottom_layout = QHBoxLayout()  # Create a horizontal layout for the bottom section

        self.yes_button = QPushButton("Tak")  # Create a button labeled "Tak"
        self.yes_button.setStyleSheet("background-color: darkgreen; color: black;")  # Apply a dark green background color to the button
        self.yes_button.clicked.connect(self.confirm)  # Connect the button's clicked signal to the confirm method

        self.no_button = QPushButton("Nie")  # Create a button labeled "Nie"
        self.no_button.setStyleSheet("background-color: darkred; color: black;")  # Apply a dark red background color to the button
        self.no_button.clicked.connect(self.decline)  # Connect the button's clicked signal to the decline method

        self.bottom_layout.addWidget(self.no_button)  # Add the "Nie" button to the bottom layout
        self.bottom_layout.addWidget(self.yes_button)  # Add the "Tak" button to the bottom layout

        self.main_layout.addLayout(self.top_layout)  # Add the top layout to the main layout
        self.main_layout.addLayout(self.bottom_layout)  # Add the bottom layout to the main layout

    def confirm(self):
        # Confirm deletion and invoke the delete_selected method in the previous window
        self.previous_window.delete_selected()
        self.previous_window.show()
        self.close()

    def decline(self):
        # Decline deletion and return to the previous window
        self.previous_window.show()
        self.close()
