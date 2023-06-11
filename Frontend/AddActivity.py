import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QTimeEdit, QCheckBox, QMessageBox
from PyQt6.QtCore import QDateTime, Qt,QTime
from PyQt6.QtGui import QPalette, QColor, QIcon
import subprocess


class AddActivityWindow(QMainWindow):
    def __init__(self, previous_window, day=None, activity=None):
        super().__init__()

        self.previous_window = previous_window
        self.day = day
        self.activity = activity

        self.setWindowTitle("Atrakcja")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

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

        self.middle_top_layout = QHBoxLayout()

        self.ticket_label = QLabel("Bilet")
        self.middle_top_layout.addWidget(self.ticket_label)

        self.ticket_checkbox = QCheckBox()
        self.ticket_checkbox.clicked.connect(self.ticket_button_enable)
        self.middle_top_layout.addWidget(self.ticket_checkbox)

        self.spacer = QSpacerItem(40,20,QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.middle_top_layout.addItem(self.spacer)

        self.main_layout.addLayout(self.middle_top_layout)

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

        self.middle_bottom_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")
        self.cancel_button.clicked.connect(self.cancel)
        self.middle_bottom_layout.addWidget(self.cancel_button)

        self.save_button = QPushButton("Zapisz")
        self.save_button.setStyleSheet("background-color: darkgreen; color: black;")
        self.save_button.clicked.connect(self.save)

        self.middle_bottom_layout.addWidget(self.save_button)

        self.main_layout.addLayout(self.middle_bottom_layout)

        self.load()
        self.update_buttons()

    def load(self):
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
        self.enable_open_ticket() if self.file_path_label.text() != "" else self.disable_open_ticket()
        self.ticket_button_enable()

    def cancel(self):
        self.close()
        self.previous_window.show()

    def save(self):
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
            self.day.add_activity(name, start_hour, end_hour, city, street, post, building, apartment, ticket_needed, pdf_ticket)
            self.close()
            self.previous_window.update_items()
            self.previous_window.show()
        elif name and start_hour and end_hour and self.activity:
            self.activity.name = name
            self.activity.ticket_needed = ticket_needed
            self.activity.pdf_ticket = pdf_ticket
            self.activity.localization = city, street, post, building, apartment
            self.close()
            self.previous_window.update_items()
            self.previous_window.disable_edit()
            self.previous_window.show()
        else:
            error_message = "Proszę uzupełnić wszystkie wymagane\npola oznaczone znakiem *"
            QMessageBox.critical(self, "Błąd", error_message)

    def ticket_button_enable(self):
        if self.ticket_checkbox.isChecked():
            self.ticket_button.setEnabled(True)
            self.ticket_button.setStyleSheet("background-color: ; color: black;")
        else:
            self.ticket_button.setEnabled(False)
            self.ticket_button.setStyleSheet("background-color: #181818; color: white;")
            self.delete_ticket()

    def enable_open_ticket(self):
        self.open_button.setEnabled(True)
        self.open_button.setStyleSheet("background-color: ; color: white;")
        self.delete_button.setEnabled(True)
        self.delete_button.setStyleSheet("background-color: darkred; color: black;")

    def disable_open_ticket(self):
        self.open_button.setEnabled(False)
        self.open_button.setStyleSheet("background-color: #181818; color: white;")
        self.delete_button.setEnabled(False)
        self.delete_button.setStyleSheet("background-color: #181818; color: white;")

    def add_ticket(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Dodaj swój bilet", "", "Bilety (*.pdf)")
        if file_name:
            self.file_path_label.setText(file_name)
            self.enable_open_ticket()

    def delete_ticket(self):
        self.file_path_label.setText("")
        self.disable_open_ticket()

    def open_ticket(self):
        subprocess.run(["start", "", self.file_path_label.text()], shell=True)

    def update_from_hour_maximum(self):
        self.from_hour_view.setMaximumTime(self.to_hour_view.time())

    def update_to_hour_minimum(self):
        self.to_hour_view.setMinimumTime(self.from_hour_view.time())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(35, 35, 35))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    app.setPalette(dark_palette)
    viewer = AddActivityWindow(None,None)
    viewer.show()
    sys.exit(app.exec())