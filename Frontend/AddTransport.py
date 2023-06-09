import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QCalendarWidget, QComboBox, QTimeEdit
from PyQt6.QtCore import QDateTime, Qt, QDate
from PyQt6.QtGui import QPalette, QColor, QIcon


class AddTravelWindow(QMainWindow):
    def __init__(self, window, app):
        super().__init__()

        self.app = app
        self.previous_window = window

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

        self.to_transport_type_label = QLabel("Środek transportu")
        self.left_layout.addWidget(self.to_transport_type_label)

        self.to_transport_type = QComboBox()
        self.to_transport_type.addItem("Wybierz środek transportu")
        self.to_transport_type.addItem("Pociąg")
        self.to_transport_type.addItem("Samolot")
        self.to_transport_type.addItem("Samochód")
        self.to_transport_type.addItem("Autobus")

        self.left_layout.addWidget(self.to_transport_type)

        self.to_ticket_label = QLabel("Bilet")
        self.left_layout.addWidget(self.to_ticket_label)

        self.to_middle_layout = QHBoxLayout()

        self.to_ticket_button = QPushButton("Dodaj bilet")
        self.to_middle_layout.addWidget(self.to_ticket_button)

        self.to_file_path_label = QLineEdit()
        self.to_file_path_label.setReadOnly(True)
        self.to_middle_layout.addWidget(self.to_file_path_label)

        self.left_layout.addLayout(self.to_middle_layout)

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")
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

        self.from_transport_type_label = QLabel("Środek transportu")
        self.right_layout.addWidget(self.from_transport_type_label)

        self.from_transport_type = QComboBox()
        self.from_transport_type.addItem("Wybierz środek transportu")
        self.from_transport_type.addItem("Pociąg")
        self.from_transport_type.addItem("Samolot")
        self.from_transport_type.addItem("Samochód")
        self.from_transport_type.addItem("Autobus")

        self.right_layout.addWidget(self.from_transport_type)

        self.from_ticket_label = QLabel("Bilet")
        self.right_layout.addWidget(self.from_ticket_label)

        self.from_middle_layout = QHBoxLayout()

        self.from_ticket_button = QPushButton("Dodaj bilet")
        self.from_middle_layout.addWidget(self.from_ticket_button)

        self.from_file_path_label = QLineEdit()
        self.from_file_path_label.setReadOnly(True)
        self.from_middle_layout.addWidget(self.from_file_path_label)

        self.right_layout.addLayout(self.from_middle_layout)

        self.save_button = QPushButton("Zapisz")
        self.save_button.setStyleSheet("background-color: darkgreen; color: black;")
        self.right_layout.addWidget(self.save_button)

        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)


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
    viewer = AddTravelWindow(None, None)
    viewer.show()
    sys.exit(app.exec())