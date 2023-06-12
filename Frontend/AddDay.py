from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QPushButton, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from AddActivity import AddActivityWindow
from ActivityEditChoice import ActivityEditChoiceWindow


class AddDayWindow(QMainWindow):  # Window for editing day
    def __init__(self, previous_window, day):
        super().__init__()

        # Store references to the previous window and day object
        self.previous_window = previous_window
        self.day = day
        self.add_activity_window = None
        self.activity_edit_choice_window = None

        # Set window properties
        self.setWindowTitle(self.day.day)
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(300)
        self.setMinimumHeight(300)

        # Create central widget and set it as the central widget of the window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create main layout for the central widget
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create top layout for the day information
        self.top_layout = QVBoxLayout()

        # Create and add labels for the day and temperature
        self.day_label = QLabel(str(self.day.date.strftime("%Y-%m-%d")))
        self.day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.day_label)

        self.temp_label = QLabel("Przewidywana temperatura: " + str(self.day.temperature) + "°C")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.temp_label)

        # Create scroll area for the activity list
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Create QListWidget to display activities
        self.activity_list = QListWidget()

        # Connect itemSelectionChanged signal to enable_edit method
        self.activity_list.itemSelectionChanged.connect(self.enable_edit)

        # Create layout for the activity list within the scroll area
        self.scroll_layout = QVBoxLayout(self.activity_list)

        # Set the activity list as the widget for the scroll area
        self.scroll_area.setWidget(self.activity_list)

        # Add the scroll area to the top layout
        self.top_layout.addWidget(self.scroll_area)

        self.main_layout.addLayout(self.top_layout)

        # Create and add buttons for editing and adding activities
        self.edit_button = QPushButton("Edytuj")
        self.edit_button.setStyleSheet("background-color: #181818; color: white;")
        self.edit_button.setEnabled(False)

        # Connect the clicked signal of the edit_button to the edit_activity method
        self.edit_button.clicked.connect(self.edit_activity)
        self.main_layout.addWidget(self.edit_button)

        self.add_button = QPushButton("+")
        self.add_button.clicked.connect(self.add_activity)
        self.main_layout.addWidget(self.add_button)

        # Create bottom layout for the "Cancel" button
        self.bottom_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Zamknij")
        self.cancel_button.setStyleSheet("background-color: ; color: black;")

        # Connect the clicked signal of the cancel_button to the cancel method
        self.cancel_button.clicked.connect(self.cancel)

        self.bottom_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(self.bottom_layout)

        # Update the activity items in the activity list
        self.update_items()

    def cancel(self):
        # Close the current window and show the previous window
        self.close()
        self.previous_window.show()

    def update_items(self):
        # Clear the activity list and populate it with sorted activity items
        self.activity_list.clear()
        self.day.sort_activities()
        for activity in self.day.activity_list:
            # Create a string representation of the activity name and time range
            activity_name = activity.name + " " + activity.start_hour + " - " + activity.end_hour

            # Create a QListWidgetItem with the activity name and assign the activity object as an attribute
            item = QListWidgetItem(activity_name)
            item.activity = activity

            # Add the item to the activity list
            self.activity_list.addItem(item)

    def add_activity(self):
        # Open the AddActivityWindow to add a new activity for the day
        self.add_activity_window = AddActivityWindow(self, self.day)
        self.close()
        self.add_activity_window.show()

    def enable_edit(self):
        # Enable the edit_button and change its style
        self.edit_button.setEnabled(True)
        self.edit_button.setStyleSheet("background-color: darkblue; color: black;")

    def disable_edit(self):
        # Disable the edit_button and change its style
        self.edit_button.setEnabled(False)
        self.edit_button.setStyleSheet("background-color: #181818; color: white;")

    def edit_activity(self):
        # Open the ActivityEditChoiceWindow to select an activity for editing
        selected_item = self.activity_list.selectedItems()[0]
        selected_activity = selected_item.activity
        self.activity_edit_choice_window = ActivityEditChoiceWindow(self, selected_activity, self.day.activity_list)
        self.close()
        self.activity_edit_choice_window.show()
