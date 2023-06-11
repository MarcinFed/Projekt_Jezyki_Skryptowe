import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QTimeEdit, QCheckBox, QScrollArea, QGridLayout
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon
from Backend.Day import Day
from AddActivity import AddActivityWindow
from ActivityEditChoice import ActivityEditChoiceWindow


class AddDayWindow(QMainWindow):
    def __init__(self, previous_window, day):
        super().__init__()
        self.previous_window = previous_window
        self.day = day
        self.add_activity_window = None
        self.activity_edit_choice_window = None

        self.setWindowTitle(self.day.day)
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(300)
        self.setMinimumHeight(300)

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

        self.activity_list = QListWidget()
        self.activity_list.itemSelectionChanged.connect(self.enable_edit)
        self.scroll_layout = QVBoxLayout(self.activity_list)

        self.scroll_area.setWidget(self.activity_list)
        self.top_layout.addWidget(self.scroll_area)

        self.main_layout.addLayout(self.top_layout)

        self.edit_button = QPushButton("Edytuj")
        self.edit_button.setStyleSheet("background-color: #181818; color: white;")
        self.edit_button.setEnabled(False)
        self.edit_button.clicked.connect(self.edit_activity)

        self.main_layout.addWidget(self.edit_button)

        self.add_button = QPushButton("+")
        self.add_button.clicked.connect(self.add_activity)

        self.main_layout.addWidget(self.add_button)

        self.bottom_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Zamknij")
        self.cancel_button.setStyleSheet("background-color: ; color: black;")
        self.cancel_button.clicked.connect(self.cancel)

        self.bottom_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(self.bottom_layout)

        self.update_items()

    def cancel(self):
        self.close()
        self.previous_window.show()

    def update_items(self):
        self.activity_list.clear()
        for activity in self.day.activity_list:
            activity_name = activity.name + " " + activity.start_hour + " - " + activity.end_hour
            item = QListWidgetItem(activity_name)
            item.activity = activity
            self.activity_list.addItem(item)

    def add_activity(self):
        self.add_activity_window = AddActivityWindow(self, self.day, )
        self.close()
        self.add_activity_window.show()

    def enable_edit(self):
        self.edit_button.setEnabled(True)
        self.edit_button.setStyleSheet("background-color: darkblue; color: black;")

    def disable_edit(self):
        self.edit_button.setEnabled(False)
        self.edit_button.setStyleSheet("background-color: #181818; color: white;")

    def edit_activity(self):
        self.activity_edit_choice_window = ActivityEditChoiceWindow(self, self.activity_list.selectedItems()[0].activity, self.day.activity_list)
        self.close()
        self.activity_edit_choice_window.show()


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