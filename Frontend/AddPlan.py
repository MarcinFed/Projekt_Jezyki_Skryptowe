from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from Frontend.AddDay import AddDayWindow


class AddPlanWindow(QMainWindow):  # Window for editing plan
    def __init__(self, previous_window, travel):
        super().__init__()

        # Store references to the previous window and travel object
        self.add_day_window = None
        self.previous_window = previous_window
        self.travel = travel

        # Set window properties
        self.setWindowTitle("Plan")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(400)

        # Create central widget and set it as the central widget of the window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create main layout for the central widget
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create top layout for the "Plans" section
        self.top_layout = QVBoxLayout()

        # Create and add labels and widgets for the "Plans" section
        self.list_label = QLabel("Plany")
        self.list_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.list_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.list_label)

        self.plans_list = QListWidget()
        self.top_layout.addWidget(self.plans_list)

        # Connect itemSelectionChanged signal to enable_edit method
        self.plans_list.itemSelectionChanged.connect(self.enable_edit)

        # Update the plans list
        self.update_plans_list()

        self.edit_button = QPushButton("Edytuj dzień")
        self.edit_button.setStyleSheet("background-color: #181818; color: white;")
        self.edit_button.setEnabled(False)

        # Connect the clicked signal of the edit_button to the edit method
        self.edit_button.clicked.connect(self.edit)
        self.top_layout.addWidget(self.edit_button)

        self.main_layout.addLayout(self.top_layout)

        # Create bottom layout for the "Cancel" button
        self.bottom_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Zamknij")
        self.cancel_button.setStyleSheet("background-color: ; color: black;")

        # Connect the clicked signal of the cancel_button to the cancel method
        self.cancel_button.clicked.connect(self.cancel)

        self.bottom_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(self.bottom_layout)

    def cancel(self):
        # Close the current window and show the previous window
        self.close()
        self.previous_window.show()

    def enable_edit(self):
        # Enable the edit_button and change its style
        self.edit_button.setEnabled(True)
        self.edit_button.setStyleSheet("background-color: darkblue; color: black;")

    def edit(self):
        # Get the selected day from the plans_list and pass it to the AddDayWindow
        selected_item = self.plans_list.selectedItems()[0]
        selected_day = selected_item.day
        self.add_day_window = AddDayWindow(self, selected_day)

        # Close the current window and show the AddDayWindow
        self.close()
        self.add_day_window.show()

    def update_plans_list(self):
        # Clear the plans_list and populate it with plan items
        self.plans_list.clear()
        for day in self.travel.plan.days:
            # Create a string representation of the plan name (date + day)
            plan_name = str(day.date.strftime("%Y-%m-%d")) + " " + str(day.day)

            # Create a QListWidgetItem with the plan name and assign the day object as an attribute
            item = QListWidgetItem(plan_name)
            item.day = day

            # Add the item to the plans_list
            self.plans_list.addItem(item)
