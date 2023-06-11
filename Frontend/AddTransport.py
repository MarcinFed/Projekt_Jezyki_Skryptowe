import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QCalendarWidget, QComboBox, QTimeEdit, QMessageBox
from PyQt6.QtCore import QDateTime, Qt, QDate, QTime
from PyQt6.QtGui import QPalette, QColor, QIcon, QDoubleValidator
import subprocess


class AddTransportWindow(QMainWindow):
    def __init__(self, previous_window, travel):
        super().__init__()

        self.previous_window = previous_window
        self.travel = travel
        self.wrong_input_window = None

        self.setWindowTitle("Transport")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout(self.central_widget)

        self.left_layout = QVBoxLayout()

        self.to_label = QLabel("Dojazd")
        self.to_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.to_label.setStyleSheet("font-weight: bold;")
        self.left_layout.addWidget(self.to_label)

        self.to_hour_label = QLabel("Godzina wyjazdu")
        self.left_layout.addWidget(self.to_hour_label)

        self.to_hour_view = QTimeEdit()
        self.to_hour_view.setDisplayFormat("HH:mm")
        self.left_layout.addWidget(self.to_hour_view)

        self.to_time_label = QLabel("Czas podróży")
        self.left_layout.addWidget(self.to_time_label)

        self.to_time_view = QLineEdit()
        self.to_time_view.setReadOnly(False)
        self.left_layout.addWidget(self.to_time_view)

        self.time_validator = QDoubleValidator()
        self.to_time_view.setValidator(self.time_validator)

        self.to_transport_type_label = QLabel("Środek transportu *")
        self.left_layout.addWidget(self.to_transport_type_label)

        self.to_transport_type = QComboBox()
        self.to_transport_type.addItem("Wybierz środek transportu")
        self.to_transport_type.addItem("Samochód")
        self.to_transport_type.addItem("Samolot")
        self.to_transport_type.addItem("Pociąg")
        self.to_transport_type.addItem("Autobus")
        self.to_transport_type.currentIndexChanged.connect(self.to_transport_button)

        self.left_layout.addWidget(self.to_transport_type)

        self.to_ticket_label = QLabel("Bilet")
        self.left_layout.addWidget(self.to_ticket_label)

        self.to_middle_layout = QHBoxLayout()

        self.to_ticket_button = QPushButton("Dodaj bilet")
        self.to_ticket_button.setEnabled(False)
        self.to_ticket_button.setStyleSheet("background-color: #181818; color: white;")
        self.to_ticket_button.clicked.connect(self.add_ticket_to)
        self.to_middle_layout.addWidget(self.to_ticket_button)

        self.to_file_path_label = QLineEdit()
        self.to_file_path_label.setReadOnly(True)
        self.to_middle_layout.addWidget(self.to_file_path_label)

        self.left_layout.addLayout(self.to_middle_layout)

        self.left_bottom_layout = QHBoxLayout()

        self.delete_ticket_to_button = QPushButton("Usuń bilet")
        self.delete_ticket_to_button.setEnabled(False)
        self.delete_ticket_to_button.setStyleSheet("background-color: #181818; color: white;")
        self.delete_ticket_to_button.clicked.connect(self.delete_ticket_to)
        self.left_bottom_layout.addWidget(self.delete_ticket_to_button)

        self.to_open_button = QPushButton("Otwórz bilet")
        self.to_open_button.setEnabled(False)
        self.to_open_button.setStyleSheet("background-color: #181818; color: white;")
        self.to_open_button.clicked.connect(self.to_open_ticket)
        self.left_bottom_layout.addWidget(self.to_open_button)

        self.left_layout.addLayout(self.left_bottom_layout)

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")
        self.cancel_button.clicked.connect(self.cancel)
        self.left_layout.addWidget(self.cancel_button)

        self.right_layout = QVBoxLayout()

        self.from_label = QLabel("Powrót")
        self.from_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.from_label.setStyleSheet("font-weight: bold;")
        self.right_layout.addWidget(self.from_label)

        self.from_hour_label = QLabel("Godzina wyjazdu")
        self.right_layout.addWidget(self.from_hour_label)

        self.from_hour_view = QTimeEdit()
        self.from_hour_view.setDisplayFormat("HH:mm")
        self.right_layout.addWidget(self.from_hour_view)

        self.from_time_label = QLabel("Czas podróży")
        self.right_layout.addWidget(self.from_time_label)


        self.from_time_view = QLineEdit()
        self.from_time_view.setReadOnly(False)
        self.right_layout.addWidget(self.from_time_view)

        self.time_validator = QDoubleValidator()
        self.from_time_view.setValidator(self.time_validator)

        self.from_transport_type_label = QLabel("Środek transportu *")
        self.right_layout.addWidget(self.from_transport_type_label)

        self.from_transport_type = QComboBox()
        self.from_transport_type.addItem("Wybierz środek transportu")
        self.from_transport_type.addItem("Samochód")
        self.from_transport_type.addItem("Samolot")
        self.from_transport_type.addItem("Pociąg")
        self.from_transport_type.addItem("Autobus")
        self.from_transport_type.currentIndexChanged.connect(self.from_transport_button)

        self.right_layout.addWidget(self.from_transport_type)

        self.from_ticket_label = QLabel("Bilet")
        self.right_layout.addWidget(self.from_ticket_label)

        self.from_middle_layout = QHBoxLayout()

        self.from_ticket_button = QPushButton("Dodaj bilet")
        self.from_ticket_button.setEnabled(False)
        self.from_ticket_button.setStyleSheet("background-color: #181818; color: white;")
        self.from_ticket_button.clicked.connect(self.add_ticket_from)
        self.from_middle_layout.addWidget(self.from_ticket_button)

        self.from_file_path_label = QLineEdit()
        self.from_file_path_label.setReadOnly(True)
        self.from_middle_layout.addWidget(self.from_file_path_label)

        self.right_layout.addLayout(self.from_middle_layout)

        self.right_bottom_layout = QHBoxLayout()

        self.delete_ticket_from_button = QPushButton("Usuń bilet")
        self.delete_ticket_from_button.setEnabled(False)
        self.delete_ticket_from_button.setStyleSheet("background-color: #181818; color: white;")
        self.delete_ticket_from_button.clicked.connect(self.delete_ticket_from)
        self.right_bottom_layout.addWidget(self.delete_ticket_from_button)

        self.from_open_button = QPushButton("Otwórz bilet")
        self.from_open_button.setEnabled(False)
        self.from_open_button.setStyleSheet("background-color: #181818; color: white;")
        self.from_open_button.clicked.connect(self.from_open_ticket)
        self.right_bottom_layout.addWidget(self.from_open_button)

        self.right_layout.addLayout(self.right_bottom_layout)

        self.save_button = QPushButton("Zapisz")
        self.save_button.setStyleSheet("background-color: darkgreen; color: black;")
        self.save_button.clicked.connect(self.save)
        self.right_layout.addWidget(self.save_button)

        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)

        self.load()
        self.update_buttons()

    def load(self):
        if self.travel.transport_to:
            self.to_hour_view.setTime(QTime.fromString(self.travel.transport_to.departure_hour, "HH:mm"))
            self.to_time_view.setText(self.travel.transport_to.time)
            self.to_transport_type.setCurrentText(self.travel.transport_to.transport_type)
            self.to_file_path_label.setText(self.travel.transport_to.pdf_ticket)
            self.from_hour_view.setTime(QTime.fromString(self.travel.transport_from.departure_hour, "HH:mm"))
            self.from_time_view.setText(self.travel.transport_from.time)
            self.from_transport_type.setCurrentText(self.travel.transport_from.transport_type)
            self.from_file_path_label.setText(self.travel.transport_from.pdf_ticket)

    def cancel(self):
        self.close()
        self.previous_window.show()

    def save(self):
        if self.to_transport_type.currentIndex() != 0 and self.from_transport_type.currentIndex() != 0:
            self.travel.transport_to = self.to_transport_type.currentText(), self.to_hour_view.text(), self.to_time_view.text(), self.to_file_path_label.text()
            self.travel.transport_from = self.from_transport_type.currentText(), self.from_hour_view.text(), self.from_time_view.text(), self.from_file_path_label.text()
            self.close()
            self.previous_window.show()
            self.previous_window.update_details()
        else:
            error_message = "Proszę uzupełnić wszystkie wymagane\npola oznaczone znakiem *"
            QMessageBox.critical(self, "Błąd", error_message)

    def to_transport_button(self):
        if self.to_transport_type.currentIndex() > 1:
            self.to_ticket_button.setEnabled(True)
            self.to_ticket_button.setStyleSheet("background-color: ; color: white;")
        else:
            self.to_ticket_button.setEnabled(False)
            self.to_ticket_button.setStyleSheet("background-color: #181818; color: white;")

    def from_transport_button(self):
        if self.from_transport_type.currentIndex() > 1:
            self.from_ticket_button.setEnabled(True)
            self.from_ticket_button.setStyleSheet("background-color: ; color: white;")
        else:
            self.from_ticket_button.setEnabled(False)
            self.from_ticket_button.setStyleSheet("background-color: #181818; color: white;")

    def add_ticket_to(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Dodaj swój bilet", "", "Bilety (*.pdf)")
        if file_name:
            self.to_file_path_label.setText(file_name)
            self.enable_ticket_to()

    def add_ticket_from(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Dodaj swój bilet", "", "Bilety (*.pdf)")
        if file_name:
            self.from_file_path_label.setText(file_name)
            self.enable_ticket_from()

    def enable_ticket_to(self):
        self.to_open_button.setEnabled(True)
        self.to_open_button.setStyleSheet("background-color: ; color: white;")
        self.delete_ticket_to_button.setEnabled(True)
        self.delete_ticket_to_button.setStyleSheet("background-color: darkred; color: black;")

    def enable_ticket_from(self):
        self.from_open_button.setEnabled(True)
        self.from_open_button.setStyleSheet("background-color: ; color: white;")
        self.delete_ticket_from_button.setEnabled(True)
        self.delete_ticket_from_button.setStyleSheet("background-color: darkred; color: black;")

    def disable_ticket_to(self):
        self.to_open_button.setEnabled(False)
        self.to_open_button.setStyleSheet("background-color: #181818; color: white;")
        self.delete_ticket_to_button.setEnabled(False)
        self.delete_ticket_to_button.setStyleSheet("background-color: #181818; color: white;")

    def disable_ticket_from(self):
        self.from_open_button.setEnabled(False)
        self.from_open_button.setStyleSheet("background-color: #181818; color: white;")
        self.delete_ticket_from_button.setEnabled(False)
        self.delete_ticket_from_button.setStyleSheet("background-color: #181818; color: white;")

    def to_open_ticket(self):
        subprocess.run(["start", "", self.to_file_path_label.text()], shell=True)

    def from_open_ticket(self):
        subprocess.run(["start", "", self.from_file_path_label.text()], shell=True)

    def delete_ticket_to(self):
        self.to_file_path_label.setText("")
        self.disable_ticket_to()

    def delete_ticket_from(self):
        self.from_file_path_label.setText("")
        self.disable_ticket_from()

    def update_buttons(self):
        self.enable_ticket_to() if self.to_file_path_label.text() != "" else self.disable_ticket_to()
        self.enable_ticket_from() if self.from_file_path_label.text() != "" else self.disable_ticket_from()


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
    viewer = AddTransportWindow(None, None)
    viewer.show()
    sys.exit(app.exec())