from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCalendarWidget, QMessageBox
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon


class AddTravelWindow(QMainWindow):  # Window for adding new travel
    def __init__(self, window, app):
        super().__init__()

        self.app = app  # Store a reference to the main application
        self.previous_window = window  # Store a reference to the previous window

        self.setWindowTitle("Dodaj podróż")  # Set the window title to "Dodaj podróż"
        self.setWindowIcon(QIcon("Logo.jpg"))  # Set the window icon using the provided image file "Logo.jpg"
        self.setMinimumWidth(400)  # Set the minimum width of the window to 400 pixels

        self.central_widget = QWidget()  # Create a central widget to hold the main layout
        self.setCentralWidget(self.central_widget)  # Set the central widget for the main window

        self.main_layout = QVBoxLayout(self.central_widget)  # Create a vertical layout as the main layout

        self.top_layout = QVBoxLayout()  # Create a vertical layout for the top section

        self.name_label = QLabel("Nazwa *")  # Create a label with the text "Nazwa *"
        self.top_layout.addWidget(self.name_label)  # Add the label to the top layout

        self.name_view = QLineEdit()  # Create a line edit widget for entering the name
        self.name_view.setReadOnly(False)  # Set the line edit as editable
        self.top_layout.addWidget(self.name_view)  # Add the line edit to the top layout

        self.destination_label = QLabel("Cel *")  # Create a label with the text "Cel *"
        self.top_layout.addWidget(self.destination_label)  # Add the label to the top layout

        self.destination_view = QLineEdit()  # Create a line edit widget for entering the destination
        self.destination_view.setReadOnly(False)  # Set the line edit as editable
        self.top_layout.addWidget(self.destination_view)  # Add the line edit to the top layout

        self.middle_layout = QHBoxLayout()  # Create a horizontal layout for the middle section

        self.left_middle_layout = QVBoxLayout()  # Create a vertical layout for the left side of the middle layout

        self.date_from_label = QLabel("Data od *")  # Create a label with the text "Data od *"
        self.date_from_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Set the alignment of the label to center
        self.left_middle_layout.addWidget(self.date_from_label)  # Add the label to the left middle layout

        self.from_date = QCalendarWidget()  # Create a calendar widget for selecting the start date
        self.from_date.setMinimumDate(QDate.currentDate())  # Set the minimum date to the current date
        self.from_date.selectionChanged.connect(self.update_to_date)  # Connect the selectionChanged signal to the update_to_date method
        self.left_middle_layout.addWidget(self.from_date)  # Add the calendar widget to the left middle layout

        self.middle_layout.addLayout(self.left_middle_layout)  # Add the left middle layout to the middle layout

        self.right_middle_layout = QVBoxLayout()  # Create a vertical layout for the right side of the middle layout

        self.date_to_label = QLabel("Data do *")  # Create a label with the text "Data do *"
        self.date_to_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Set the alignment of the label to center
        self.right_middle_layout.addWidget(self.date_to_label)  # Add the label to the right middle layout

        self.to_date = QCalendarWidget()  # Create a calendar widget for selecting the end date
        self.to_date.setMinimumDate(QDate.currentDate())  # Set the minimum date to the current date
        self.to_date.selectionChanged.connect(self.update_from_date)  # Connect the selectionChanged signal to the update_from_date method
        self.right_middle_layout.addWidget(self.to_date)  # Add the calendar widget to the right middle layout

        self.middle_layout.addLayout(self.right_middle_layout)  # Add the right middle layout to the middle layout

        self.bottom_layout = QHBoxLayout()  # Create a horizontal layout for the bottom section

        self.create_button = QPushButton("Utwórz")  # Create a button with the text "Utwórz"
        self.create_button.setStyleSheet("background-color: darkgreen; color: black;")  # Apply a dark green background color to the button
        self.create_button.clicked.connect(self.create)  # Connect the button's clicked signal to the create method

        self.cancel_button = QPushButton("Anuluj")  # Create a button with the text "Anuluj"
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")  # Apply a dark red background color to the button
        self.cancel_button.clicked.connect(self.cancel)  # Connect the button's clicked signal to the cancel method

        self.bottom_layout.addWidget(self.cancel_button)  # Add the "Anuluj" button to the bottom layout
        self.bottom_layout.addWidget(self.create_button)  # Add the "Utwórz" button to the bottom layout

        self.main_layout.addLayout(self.top_layout)  # Add the top layout to the main layout
        self.main_layout.addLayout(self.middle_layout)  # Add the middle layout to the main layout
        self.main_layout.addLayout(self.bottom_layout)  # Add the bottom layout to the main layout

    def cancel(self):
        self.previous_window.show()  # Show the previous window
        self.close()  # Close the current window

    def create(self):
        try:
            name = self.name_view.text().strip()  # Get the entered name text and remove leading/trailing whitespace
            destination = self.destination_view.text().strip()  # Get the entered destination text and remove leading/trailing whitespace
            date_from = self.from_date.selectedDate().toPyDate()  # Get the selected start date
            date_to = self.to_date.selectedDate().toPyDate()  # Get the selected end date

            if name and destination and date_from and date_to:
                # If all required fields are not empty, proceed with creating the travel
                self.app.add_travel(name, destination, date_from, date_to)  # Call the app's add_travel method with the provided details
                self.previous_window.show()  # Show the previous window
                self.previous_window.update_travels_list()  # Update the travels list in the previous window
                self.close()  # Close the current window
            else:
                # If any required field is empty, show an error message box
                error_message = "Proszę uzupełnić wszystkie wymagane\npola oznaczone znakiem *"
                QMessageBox.critical(self, "Błąd", error_message)
        except:
            error_message = "Proszę wpisać poprawną nazwę\nmiejsca docelowego"
            QMessageBox.critical(self, "Błąd", error_message)

    def update_to_date(self):
        self.to_date.setMinimumDate(self.from_date.selectedDate())  # Update the minimum date of the "to_date" calendar widget based on the selected "from_date"

    def update_from_date(self):
        self.from_date.setMaximumDate(self.to_date.selectedDate())  # Update the maximum date of the "from_date" calendar widget based on the selected "to_date"
