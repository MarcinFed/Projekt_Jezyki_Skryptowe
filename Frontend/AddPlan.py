import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QTimeEdit, QCheckBox, QScrollArea, QGridLayout
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon
from Frontend.AddDay import AddDayWindow

class AddPlanWindow(QMainWindow):
    def __init__(self, previous_window, travel):
        super().__init__()

        self.add_day_window = None
        self.previous_window = previous_window
        self.travel = travel

        self.setWindowTitle("Plan")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()

        self.list_label = QLabel("Plany")
        self.list_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.list_label.setStyleSheet("font-weight: bold;")
        self.top_layout.addWidget(self.list_label)

        self.plans_list = QListWidget()
        self.top_layout.addWidget(self.plans_list)
        self.plans_list.itemSelectionChanged.connect(self.enable_edit)
        self.update_plans_list()

        self.edit_button = QPushButton("Edytuj dzień")
        self.edit_button.setStyleSheet("background-color: #181818; color: white;")
        self.edit_button.setEnabled(False)
        self.edit_button.clicked.connect(self.edit)
        self.top_layout.addWidget(self.edit_button)

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

    def enable_edit(self):
        self.edit_button.setEnabled(True)
        self.edit_button.setStyleSheet("background-color: darkblue; color: black;")

    def edit(self):
        self.add_day_window = AddDayWindow(self, self.plans_list.selectedItems()[0].day)
        self.close()
        self.add_day_window.show()

    def update_plans_list(self):
        self.plans_list.clear()
        for day in self.travel.plan.days:
            plan_name = str(day.date.strftime("%Y-%m-%d")) + " " + str(day.day)
            item = QListWidgetItem(plan_name)
            item.day = day
            self.plans_list.addItem(item)



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
    viewer = AddPlanWindow(None, None)
    viewer.show()
    sys.exit(app.exec())