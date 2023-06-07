import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TripSet")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(700)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        # Top widget
        self.top_layout = QHBoxLayout()

        self.left_top_layout = QHBoxLayout()

        self.travels_list = QListWidget()
        self.left_top_layout.addWidget(self.travels_list)

        self.right_top_layout = QVBoxLayout()

        self.details_label = QLabel("Szczegóły wyjazdu")
        self.details_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.details_label.setStyleSheet("font-weight: bold;")
        self.right_top_layout.addWidget(self.details_label)

        spacer_item = QSpacerItem(20, 20)
        self.right_top_layout.addItem(spacer_item)

        self.destination_label = QLabel("Cel")
        self.right_top_layout.addWidget(self.destination_label)
        self.destination_view = QLineEdit()
        self.destination_view.setReadOnly(True)
        self.right_top_layout.addWidget(self.destination_view)

        self.transport_label = QLabel("Transport")
        self.right_top_layout.addWidget(self.transport_label)
        self.transport_view = QLineEdit()
        self.transport_view.setReadOnly(True)
        self.right_top_layout.addWidget(self.transport_view)

        self.accommodation_label = QLabel("Zakwaterowanie")
        self.right_top_layout.addWidget(self.accommodation_label)
        self.accommodation_view = QLineEdit()
        self.accommodation_view.setReadOnly(True)
        self.right_top_layout.addWidget(self.accommodation_view)

        self.date_label = QLabel("Daty")
        self.right_top_layout.addWidget(self.date_label)
        self.date_view = QLineEdit()
        self.date_view.setReadOnly(True)
        self.right_top_layout.addWidget(self.date_view)

        self.days_label = QLabel("Liczba dni")
        self.right_top_layout.addWidget(self.days_label)
        self.days_view = QLineEdit()
        self.days_view.setReadOnly(True)
        self.right_top_layout.addWidget(self.days_view)

        self.temperature_label = QLabel("Średnia temperatura")
        self.right_top_layout.addWidget(self.temperature_label)
        self.temperature_view = QLineEdit()
        self.temperature_view.setReadOnly(True)
        self.right_top_layout.addWidget(self.temperature_view)

        self.top_layout.addLayout(self.left_top_layout)
        self.top_layout.addLayout(self.right_top_layout)

        self.main_layout.addLayout(self.top_layout)

        # Bottom buttons
        self.bottom_layout = QHBoxLayout()

        self.new_button = QPushButton("Dodaj")
        self.new_button.setStyleSheet("background-color: darkgreen; color: black;")

        self.delete_button = QPushButton("Usuń")
        self.delete_button.setStyleSheet("background-color: darkred; color: black;")
        self.delete_button.setEnabled(False)

        self.edit_button = QPushButton("Edytuj")
        self.edit_button.setStyleSheet("background-color: darkblue; color: black;")
        self.edit_button.setEnabled(False)

        self.calendar_button = QPushButton("Dodaj do kolendarza")
        self.calendar_button.setStyleSheet("background-color: darkorange; color: black;")
        self.calendar_button.setEnabled(False)

        self.update_button_colors()

        self.bottom_layout.addWidget(self.new_button)
        self.bottom_layout.addWidget(self.delete_button)
        self.bottom_layout.addWidget(self.edit_button)
        self.bottom_layout.addWidget(self.calendar_button)

        self.main_layout.addLayout(self.bottom_layout)

    def update_button_colors(self):
        # Update the color of the delete_button
        if self.delete_button.isEnabled():
            self.delete_button.setStyleSheet("background-color: red; color: black;")
        else:
            self.delete_button.setStyleSheet("background-color: grey; color: black;")

        # Update the color of the edit_button
        if self.edit_button.isEnabled():
            self.edit_button.setStyleSheet("background-color: blue; color: black;")
        else:
            self.edit_button.setStyleSheet("background-color: grey; color: black;")

        # Update the color of the calendar_button
        if self.calendar_button.isEnabled():
            self.calendar_button.setStyleSheet("background-color: orange; color: black;")
        else:
            self.calendar_button.setStyleSheet("background-color: grey; color: black;")


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
    viewer = MainWindow()
    viewer.show()
    sys.exit(app.exec())
