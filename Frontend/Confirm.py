import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon

class ConfirmWindow(QMainWindow):
    def __init__(self, window, element):
        super().__init__()

        self.previous_window = window
        self.element = element

        self.setWindowTitle("Edycja")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()
        self.question_label = QLabel("Czy na pewno chcesz usunąć " + self.element + " ?")
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.question_label)

        self.bottom_layout = QHBoxLayout()

        self.yes_button = QPushButton("Tak")
        self.yes_button.setStyleSheet("background-color: darkgreen; color: black;")
        self.yes_button.clicked.connect(self.confirm)

        self.no_button = QPushButton("Nie")
        self.no_button.setStyleSheet("background-color: darkred; color: black;")
        self.no_button.clicked.connect(self.decline)

        self.bottom_layout.addWidget(self.no_button)
        self.bottom_layout.addWidget(self.yes_button)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)

    def confirm(self):
        self.previous_window.delete_selected()
        self.previous_window.show()
        self.close()

    def decline(self):
        self.previous_window.show()
        self.close()


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
    viewer = ConfirmWindow(None,"Wyjazd")
    viewer.show()
    sys.exit(app.exec())
