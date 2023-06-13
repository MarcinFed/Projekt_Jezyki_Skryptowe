from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from Frontend.AddAccomodation import AddAccommodationWindow
from Frontend.AddPlan import AddPlanWindow
from Frontend.AddTransport import AddTransportWindow


class ChooseActionWindow(QMainWindow):  # Window for choosing action to do with travel
    def __init__(self, previous_window, travel):
        super().__init__()

        self.previous_window = previous_window  # Store the reference to the previous window
        self.travel = travel  # Store the travel object to be edited
        self.add_accommodation_window = None  # Initialize the accommodation window reference to None
        self.add_plan_window = None  # Initialize the plan window reference to None
        self.add_transport_window = None  # Initialize the transport window reference to None

        self.setWindowTitle("Edycja")  # Set the window title to "Edycja"
        self.setWindowIcon(QIcon("Frontend\\Logo.jpg"))  # Set the window icon using the provided image file "Logo.jpg"
        self.setMinimumWidth(300)  # Set the minimum width of the window to 300 pixels

        self.central_widget = QWidget()  # Create a central widget to hold the main layout
        self.setCentralWidget(self.central_widget)  # Set the central widget for the main window

        self.main_layout = QVBoxLayout(self.central_widget)  # Create a vertical layout as the main layout

        self.top_layout = QVBoxLayout()  # Create a vertical layout for the top section
        self.question_label = QLabel("Co chcesz edytować ?")  # Create a label with the question
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Set the alignment of the label to center
        self.question_label.setStyleSheet("font-weight: bold;")  # Apply a bold font style to the label
        self.top_layout.addWidget(self.question_label)  # Add the label to the top layout

        self.middle_layout = QHBoxLayout()  # Create a horizontal layout for the middle section

        self.accommodation_button = QPushButton("Zawkaterowanie")  # Create a button labeled "Zawkaterowanie"
        self.accommodation_button.setStyleSheet("background-color: darkorange; color: black;")  # Apply a dark orange background color to the button
        self.accommodation_button.clicked.connect(self.accommodation)  # Connect the button's clicked signal to the accommodation method

        self.plan_button = QPushButton("Plan")  # Create a button labeled "Plan"
        self.plan_button.setStyleSheet("background-color: darkblue; color: black;")  # Apply a dark blue background color to the button
        self.plan_button.clicked.connect(self.plan)  # Connect the button's clicked signal to the plan method

        self.transport_button = QPushButton("Transport")  # Create a button labeled "Transport"
        self.transport_button.setStyleSheet("background-color: darkgreen; color: black;")  # Apply a dark green background color to the button
        self.transport_button.clicked.connect(self.transport)  # Connect the button's clicked signal to the transport method

        self.middle_layout.addWidget(self.accommodation_button)  # Add the "Zawkaterowanie" button to the middle layout
        self.middle_layout.addWidget(self.plan_button)  # Add the "Plan" button to the middle layout
        self.middle_layout.addWidget(self.transport_button)  # Add the "Transport" button to the middle layout

        self.bottom_layout = QVBoxLayout()  # Create a vertical layout for the bottom section

        self.cancel_button = QPushButton("Anuluj")  # Create a button labeled "Anuluj"
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")  # Apply a dark red background color to the button
        self.cancel_button.clicked.connect(self.cancel)  # Connect the button's clicked signal to the cancel method

        self.bottom_layout.addWidget(self.cancel_button)  # Add the "Anuluj" button to the bottom layout

        self.main_layout.addLayout(self.top_layout)  # Add the top layout to the main layout
        self.main_layout.addLayout(self.middle_layout)  # Add the middle layout to the main layout
        self.main_layout.addLayout(self.bottom_layout)  # Add the bottom layout to the main layout

    def cancel(self):
        self.previous_window.show()  # Show the previous window
        self.close()  # Close the current window

    def accommodation(self):
        self.add_accommodation_window = AddAccommodationWindow(self.previous_window, self.travel)  # Create an instance of the AddAccommodationWindow
        self.close()  # Close the current window
        self.add_accommodation_window.show()  # Show the AddAccommodationWindow

    def plan(self):
        self.add_plan_window = AddPlanWindow(self.previous_window, self.travel)  # Create an instance of the AddPlanWindow
        self.close()  # Close the current window
        self.add_plan_window.show()  # Show the AddPlanWindow

    def transport(self):
        self.add_transport_window = AddTransportWindow(self.previous_window, self.travel)  # Create an instance of the AddTransportWindow
        self.close()  # Close the current window
        self.add_transport_window.show()  # Show the AddTransportWindow
