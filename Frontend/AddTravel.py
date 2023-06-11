import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QCalendarWidget, QMessageBox
from PyQt6.QtCore import QDateTime, Qt, QDate
from PyQt6.QtGui import QPalette, QColor, QIcon


class AddTravelWindow(QMainWindow):
    def __init__(self, window, app):
        super().__init__()

        self.app = app
        self.previous_window = window

        self.setWindowTitle("Dodaj podróż")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()

        self.name_label = QLabel("Nazwa *")
        self.top_layout.addWidget(self.name_label)

        self.name_view = QLineEdit()
        self.name_view.setReadOnly(False)
        self.top_layout.addWidget(self.name_view)

        self.destination_label = QLabel("Cel *")
        self.top_layout.addWidget(self.destination_label)

        self.destination_view = QLineEdit()
        self.destination_view.setReadOnly(False)
        self.top_layout.addWidget(self.destination_view)

        self.middle_layout = QHBoxLayout()

        self.left_middle_layout = QVBoxLayout()

        self.date_from_label = QLabel("Data od *")
        self.date_from_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_middle_layout.addWidget(self.date_from_label)

        self.from_date = QCalendarWidget()
        self.from_date.setMinimumDate(QDate.currentDate())
        self.from_date.selectionChanged.connect(self.update_to_date)
        self.left_middle_layout.addWidget(self.from_date)

        self.middle_layout.addLayout(self.left_middle_layout)

        self.right_middle_layout = QVBoxLayout()

        self.date_to_label = QLabel("Data do *")
        self.date_to_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_middle_layout.addWidget(self.date_to_label)

        self.to_date = QCalendarWidget()
        self.to_date.setMinimumDate(QDate.currentDate())
        self.to_date.selectionChanged.connect(self.update_from_date)
        self.right_middle_layout.addWidget(self.to_date)

        self.middle_layout.addLayout(self.right_middle_layout)

        self.bottom_layout = QHBoxLayout()

        self.create_button = QPushButton("Utwórz")
        self.create_button.setStyleSheet("background-color: darkgreen; color: black;")
        self.create_button.clicked.connect(self.create)

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")
        self.cancel_button.clicked.connect(self.cancel)

        self.bottom_layout.addWidget(self.cancel_button)
        self.bottom_layout.addWidget(self.create_button)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addLayout(self.bottom_layout)

    def cancel(self):
        self.previous_window.show()
        self.close()

    def create(self):
        name = self.name_view.text().strip()
        destination = self.destination_view.text().strip()
        date_from = self.from_date.selectedDate().toPyDate()
        date_to = self.to_date.selectedDate().toPyDate()

        if name and destination and date_from and date_to:
            self.app.add_travel(name, destination, date_from, date_to)
            self.previous_window.show()
            self.previous_window.update_travels_list()
            self.close()
        else:
            error_message = "Proszę uzupełnić wszystkie wymagane\npola oznaczone znakiem *"
            QMessageBox.critical(self, "Błąd", error_message)

    def update_to_date(self):
        self.to_date.setMinimumDate(self.from_date.selectedDate())

    def update_from_date(self):
        self.from_date.setMaximumDate(self.to_date.selectedDate())


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