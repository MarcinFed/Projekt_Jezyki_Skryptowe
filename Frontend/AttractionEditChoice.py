import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QCalendarWidget
from PyQt6.QtCore import QDateTime, Qt, QDate
from PyQt6.QtGui import QPalette, QColor, QIcon


class AttractionEditChoice(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Edycja")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()
        self.question_label = QLabel("Co chcesz zrobić ?")
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.question_label)

        self.middle_layout = QHBoxLayout()

        self.edit_button = QPushButton("Edytuj")
        self.edit_button.setStyleSheet("background-color: darkblue; color: black;")

        self.delete_button = QPushButton("Usuń")
        self.delete_button.setStyleSheet("background-color: darkred; color: black;")

        self.middle_layout.addWidget(self.delete_button)
        self.middle_layout.addWidget(self.edit_button)

        self.bottom_layout = QVBoxLayout()

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkorange; color: black;")

        self.bottom_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addLayout(self.bottom_layout)


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
    viewer = AttractionEditChoice()
    viewer.show()
    sys.exit(app.exec())