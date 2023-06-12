from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,\
    QPushButton, QFileDialog, QSpacerItem, QSizePolicy, QTimeEdit, QCheckBox, QMessageBox
from PyQt6.QtCore import QTime
from PyQt6.QtGui import QIcon
import subprocess

class AddActivityWindow(QMainWindow):  # Window for adding an activity to the day
    def __init__(self, previous_window, day=None, activity=None):
        super().__init__()

        # Store references to the previous window, day, and activity objects
        self.previous_window = previous_window
        self.day = day
        self.activity = activity

        # Set window properties
        self.setWindowTitle("Atrakcja")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(400)

        # Create central widget and set it as the central widget of the window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create main layout for the central widget
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create labels and input fields for activity details
        self.name_label = QLabel("Nazwa *")
        self.main_layout.addWidget(self.name_label)

        self.name_view = QLineEdit()
        self.name_view.setReadOnly(False)
        self.main_layout.addWidget(self.name_view)

        self.from_hour_label = QLabel("Godzina rozpoczęcia *")
        self.main_layout.addWidget(self.from_hour_label)

        self.from_hour_view = QTimeEdit()
        self.from_hour_view.setDisplayFormat("HH:mm")
        self.from_hour_view.timeChanged.connect(self.update_to_hour_minimum)
        self.main_layout.addWidget(self.from_hour_view)

        self.to_hour_label = QLabel("Godzina zakończenia *")
        self.main_layout.addWidget(self.to_hour_label)

        self.to_hour_view = QTimeEdit()
        self.to_hour_view.setDisplayFormat("HH:mm")
        self.to_hour_view.timeChanged.connect(self.update_from_hour_maximum)
        self.main_layout.addWidget(self.to_hour_view)

        self.city_label = QLabel("Miasto")
        self.main_layout.addWidget(self.city_label)

        self.city_view = QLineEdit()
        self.city_view.setReadOnly(False)
        self.main_layout.addWidget(self.city_view)

        self.street_label = QLabel("Ulica")
        self.main_layout.addWidget(self.street_label)

        self.street_view = QLineEdit()
        self.street_view.setReadOnly(False)
        self.main_layout.addWidget(self.street_view)

        self.post_label = QLabel("Kod pocztowy")
        self.main_layout.addWidget(self.post_label)

        self.post_view = QLineEdit()
        self.post_view.setReadOnly(False)
        self.main_layout.addWidget(self.post_view)

        self.building_label = QLabel("Numer budynku")
        self.main_layout.addWidget(self.building_label)

        self.building_view = QLineEdit()
        self.building_view.setReadOnly(False)
        self.main_layout.addWidget(self.building_view)

        self.apartment_label = QLabel("Numer mieszkania")
        self.main_layout.addWidget(self.apartment_label)

        self.apartment_view = QLineEdit()
        self.apartment_view.setReadOnly(False)
        self.main_layout.addWidget(self.apartment_view)

        # Create layout for the ticket checkbox and spacer
        self.middle_top_layout = QHBoxLayout()

        self.ticket_label = QLabel("Bilet")
        self.middle_top_layout.addWidget(self.ticket_label)

        self.ticket_checkbox = QCheckBox()
        self.ticket_checkbox.clicked.connect(self.ticket_button_enable)
        self.middle_top_layout.addWidget(self.ticket_checkbox)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.middle_top_layout.addItem(self.spacer)

        self.main_layout.addLayout(self.middle_top_layout)

        # Create layout for ticket button and file path label
        self.middle_layout = QHBoxLayout()

        self.ticket_button = QPushButton("Dodaj bilet")
        self.ticket_button.setEnabled(False)
        self.ticket_button.setStyleSheet("background-color: #181818; color: white;")
        self.ticket_button.clicked.connect(self.add_ticket)
        self.middle_layout.addWidget(self.ticket_button)

        self.file_path_label = QLineEdit()
        self.file_path_label.setReadOnly(True)
        self.middle_layout.addWidget(self.file_path_label)

        self.main_layout.addLayout(self.middle_layout)

        # Create layout for delete button and open button
        self.ticket_layout = QHBoxLayout()

        self.delete_button = QPushButton("Usuń bilet")
        self.delete_button.setEnabled(False)
        self.delete_button.setStyleSheet("background-color: #181818; color: white;")
        self.delete_button.clicked.connect(self.delete_ticket)
        self.ticket_layout.addWidget(self.delete_button)

        self.open_button = QPushButton("Otwórz bilet")
        self.open_button.setEnabled(False)
        self.open_button.setStyleSheet("background-color: #181818; color: white;")
        self.open_button.clicked.connect(self.open_ticket)
        self.ticket_layout.addWidget(self.open_button)

        self.main_layout.addLayout(self.ticket_layout)

        # Create layout for cancel button and save button
        self.middle_bottom_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")
        self.cancel_button.clicked.connect(self.cancel)
        self.middle_bottom_layout.addWidget(self.cancel_button)

        self.save_button = QPushButton("Zatwierdź")
        self.save_button.setStyleSheet("background-color: darkgreen; color: black;")
        self.save_button.clicked.connect(self.save)
        self.middle_bottom_layout.addWidget(self.save_button)

        self.main_layout.addLayout(self.middle_bottom_layout)

        # Load activity details if provided
        self.load()
        self.update_buttons()

    def load(self):
        # Load activity details into the input fields if an activity object is provided
        if self.activity:
            self.name_view.setText(self.activity.name)
            self.from_hour_view.setTime(QTime.fromString(self.activity.start_hour, "HH:mm"))
            self.to_hour_view.setTime(QTime.fromString(self.activity.end_hour, "HH:mm"))
            self.city_view.setText(self.activity.localization.city)
            self.street_view.setText(self.activity.localization.street_name)
            self.post_view.setText(self.activity.localization.post_code)
            self.building_view.setText(self.activity.localization.building_number)
            self.apartment_view.setText(self.activity.localization.apartment_number)
            self.ticket_checkbox.setChecked(self.activity.ticket_needed)
            self.file_path_label.setText(self.activity.pdf_ticket)

    def update_buttons(self):
        # Enable or disable the open button and delete button based on the presence of a file path
        self.enable_open_ticket() if self.file_path_label.text() != "" else self.disable_open_ticket()
        self.ticket_button_enable()

    def cancel(self):
        # Close the window and show the previous window
        self.close()
        self.previous_window.show()

    def save(self):
        # Get the activity details from the input fields and save the activity to the day object
        name = self.name_view.text()
        start_hour = self.from_hour_view.text()
        end_hour = self.to_hour_view.text()
        city = self.city_view.text()
        street = self.street_view.text()
        post = self.post_view.text()
        building = self.building_view.text()
        apartment = self.apartment_view.text()
        ticket_needed = self.ticket_checkbox.isChecked()
        pdf_ticket = self.file_path_label.text()

        if name and start_hour and end_hour and self.day:
            # Create a new activity and add it to the day
            self.day.add_activity(name, start_hour, end_hour, city, street, post, building, apartment, ticket_needed, pdf_ticket)
            self.close()
            self.previous_window.update_items()
            self.previous_window.show()
        elif name and start_hour and end_hour and self.activity:
            # Update the existing activity
            self.activity.name = name
            self.activity.start_hour = start_hour
            self.activity.end_hour = end_hour
            self.activity.ticket_needed = ticket_needed
            self.activity.pdf_ticket = pdf_ticket
            self.activity.localization = city, street, post, building, apartment
            self.close()
            self.previous_window.update_items()
            self.previous_window.disable_edit()
            self.previous_window.show()
        else:
            # Display an error message if required fields are missing
            error_message = "Proszę uzupełnić wszystkie wymagane\npola oznaczone znakiem *"
            QMessageBox.critical(self, "Błąd", error_message)

    def ticket_button_enable(self):
        # Enable or disable the ticket button based on the checked state of the ticket checkbox
        if self.ticket_checkbox.isChecked():
            self.ticket_button.setEnabled(True)
            self.ticket_button.setStyleSheet("background-color: ; color: black;")
        else:
            self.ticket_button.setEnabled(False)
            self.ticket_button.setStyleSheet("background-color: #181818; color: white;")
            self.delete_ticket()

    def enable_open_ticket(self):
        # Enable the open button and delete button
        self.open_button.setEnabled(True)
        self.open_button.setStyleSheet("background-color: ; color: white;")
        self.delete_button.setEnabled(True)
        self.delete_button.setStyleSheet("background-color: darkred; color: black;")

    def disable_open_ticket(self):
        # Disable the open button and delete button
        self.open_button.setEnabled(False)
        self.open_button.setStyleSheet("background-color: #181818; color: white;")
        self.delete_button.setEnabled(False)
        self.delete_button.setStyleSheet("background-color: #181818; color: white;")

    def add_ticket(self):
        # Open a file dialog to select a PDF ticket file and set the file path label
        file_name, _ = QFileDialog.getOpenFileName(self, "Dodaj swój bilet", "", "Bilety (*.pdf)")
        if file_name:
            self.file_path_label.setText(file_name)
            self.enable_open_ticket()

    def delete_ticket(self):
        # Clear the file path label and disable the open button and delete button
        self.file_path_label.setText("")
        self.disable_open_ticket()

    def open_ticket(self):
        # Open the PDF ticket using the default system application for PDF files
        subprocess.run(["start", "", self.file_path_label.text()], shell=True)

    def update_from_hour_maximum(self):
        # Update the maximum time for the "From Hour" view based on the selected time in the "To Hour" view
        self.from_hour_view.setMaximumTime(self.to_hour_view.time())

    def update_to_hour_minimum(self):
        # Update the minimum time for the "To Hour" view based on the selected time in the "From Hour" view
        self.to_hour_view.setMinimumTime(self.from_hour_view.time())
