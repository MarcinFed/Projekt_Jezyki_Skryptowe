import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QTimeEdit, QCheckBox, QScrollArea, QGridLayout
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon
from Backend.Day import Day


class AddDayWindow(QMainWindow):
    def __init__(self, previous_window, day):
        super().__init__()

        self.previous_window = previous_window
        self.day = day

        self.setWindowTitle("Dzień ")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()

        self.day_label = QLabel(str(self.day.date.strftime("%Y-%m-%d")))
        self.day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.day_label)

        self.temp_label = QLabel(str(self.day.temperature))
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.temp_label)

        self.bottom_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")
        self.cancel_button.clicked.connect(self.cancel)

        self.bottom_layout.addWidget(self.cancel_button)

        self.save_button = QPushButton("Zapisz")
        self.save_button.setStyleSheet("background-color: darkgreen; color: black;")

        self.bottom_layout.addWidget(self.save_button)

        self.main_layout.addLayout(self.bottom_layout)

    def cancel(self):
        self.close()
        self.previous_window.show()


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
    viewer = AddDayWindow(None, None)
    viewer.show()
    sys.exit(app.exec())