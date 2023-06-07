import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon

class ChooseActionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Edycja")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()
        self.question_label = QLabel("Co chcesz edytować ?")
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.question_label)

        self.middle_layout = QHBoxLayout()

        self.accommodation_button = QPushButton("Zawkaterowanie")
        self.accommodation_button.setStyleSheet("background-color: darkorange; color: black;")

        self.plan_button = QPushButton("Plan")
        self.plan_button.setStyleSheet("background-color: darkblue; color: black;")

        self.transport_button = QPushButton("Transport")
        self.transport_button.setStyleSheet("background-color: darkgreen; color: black;")

        self.middle_layout.addWidget(self.accommodation_button)
        self.middle_layout.addWidget(self.plan_button)
        self.middle_layout.addWidget(self.transport_button)

        self.bottom_layout = QVBoxLayout()

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")

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
    viewer = ChooseActionWindow()
    viewer.show()
    sys.exit(app.exec())