import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QTimeEdit, QCheckBox, QScrollArea, QGridLayout
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon
from Backend.Day import Day
from AddAttraction import AddAttractionWindow


class AddDayWindow(QMainWindow):
    def __init__(self, previous_window, day):
        super().__init__()

        self.previous_window = previous_window
        self.day = day
        self.add_attraction_window = None

        self.setWindowTitle(self.day.day)
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(300)
        self.setMinimumHeight(500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()

        self.day_label = QLabel(str(self.day.date.strftime("%Y-%m-%d")))
        self.day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.day_label)

        self.temp_label = QLabel("Przewidywana temperatura: " + str(self.day.temperature) + "°C")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.temp_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        self.add_button = QPushButton("+")
        self.add_button.clicked.connect(self.add_attraction)

        self.scroll_layout.addWidget(self.add_button)

        self.scroll_area.setWidget(self.scroll_content)
        self.top_layout.addWidget(self.scroll_area)

        self.main_layout.addLayout(self.top_layout)

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

    def add_tile(self):
        new_tile = QPushButton("Nowy element")
        self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, new_tile)

    def add_attraction(self):
        self.add_attraction_window = AddAttractionWindow(self, self.day)
        self.close()
        self.add_attraction_window.show()


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