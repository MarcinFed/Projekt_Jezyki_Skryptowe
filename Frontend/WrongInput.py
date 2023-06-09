import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QCalendarWidget, QComboBox, QTimeEdit
from PyQt6.QtCore import QDateTime, Qt, QDate
from PyQt6.QtGui import QPalette, QColor, QIcon


class WrongInputWindow(QMainWindow):
    def __init__(self, previous_window):
        super().__init__()

        self.previous_window = previous_window

        self.setWindowTitle("Błędne dane")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.warning_label = QLabel("Wprowadzono blędne dane,\n popraw je aby kontynuować!")
        self.warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning_label.setStyleSheet("font-weight: bold;")
        self.main_layout.addWidget(self.warning_label)

        self.ok_button = QPushButton("Ok")
        self.ok_button.setStyleSheet("background-color: darkred; color: black;")
        self.ok_button.clicked.connect(self.ok)

        self.main_layout.addWidget(self.ok_button)

    def ok(self):
        self.close()
        self.previous_window.show()