from Backend.App import App
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QMessageBox
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon
from AddTravel import AddTravelWindow
from Confirm import ConfirmWindow
from ChooseAction import ChooseActionWindow


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.app = app

        self.add_travel_window = None
        self.confirm_decision = None
        self.choose_action_window = None

        self.setWindowTitle("TripSet")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(700)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        # Top widget
        self.top_layout = QHBoxLayout()

        self.left_top_layout = QVBoxLayout()

        self.list_label = QLabel("Wyjazdy")
        self.list_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.list_label.setStyleSheet("font-weight: bold;")
        self.left_top_layout.addWidget(self.list_label)

        self.travels_list = QListWidget()
        self.travels_list.itemSelectionChanged.connect(self.update_details)
        self.left_top_layout.addWidget(self.travels_list)
        self.travels_list.clicked.connect(self.enable_buttons)

        self.save_button = QPushButton("Zapisz")
        self.save_button.setStyleSheet("background-color: #8B93D8; color: black;")
        self.save_button.setEnabled(True)
        self.save_button.clicked.connect(self.save)
        self.left_top_layout.addWidget(self.save_button)

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

        self.transport_to_label = QLabel("Transport do")
        self.right_top_layout.addWidget(self.transport_to_label)
        self.transport_to_view = QLineEdit()
        self.transport_to_view.setReadOnly(True)
        self.right_top_layout.addWidget(self.transport_to_view)

        self.transport_from_label = QLabel("Transport od")
        self.right_top_layout.addWidget(self.transport_from_label)
        self.transport_from_view = QLineEdit()
        self.transport_from_view.setReadOnly(True)
        self.right_top_layout.addWidget(self.transport_from_view)

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

        self.days_label = QLabel("Liczba nocy")
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
        self.new_button.clicked.connect(self.open_add_travel_window)

        self.delete_button = QPushButton("Usuń")
        self.delete_button.setStyleSheet("background-color: darkred; color: black;")
        self.delete_button.setEnabled(False)
        self.delete_button.clicked.connect(self.open_confirm_decision)

        self.edit_button = QPushButton("Edytuj")
        self.edit_button.setStyleSheet("background-color: darkblue; color: black;")
        self.edit_button.setEnabled(False)
        self.edit_button.clicked.connect(self.open_edit_window)

        self.calendar_button = QPushButton("Dodaj do kolendarza")
        self.calendar_button.setStyleSheet("background-color: darkorange; color: black;")
        self.calendar_button.setEnabled(False)
        self.calendar_button.clicked.connect(self.add_to_calendar)

        self.update_button_colors()

        self.bottom_layout.addWidget(self.new_button)
        self.bottom_layout.addWidget(self.delete_button)
        self.bottom_layout.addWidget(self.edit_button)
        self.bottom_layout.addWidget(self.calendar_button)

        self.main_layout.addLayout(self.bottom_layout)

        self.load()

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

    def open_add_travel_window(self):
        self.add_travel_window = AddTravelWindow(self, self.app)
        self.close()
        self.add_travel_window.show()

    def update_travels_list(self):
        self.travels_list.clear()
        for travel in self.app.travels:
            travel_name = travel.name
            item = QListWidgetItem(travel_name)
            item.travel = travel
            self.travels_list.addItem(item)

    def enable_buttons(self):
        self.delete_button.setEnabled(True)
        self.edit_button.setEnabled(True)
        self.calendar_button.setEnabled(True)
        self.update_button_colors()

    def disable_buttons(self):
        self.delete_button.setEnabled(False)
        self.edit_button.setEnabled(False)
        self.calendar_button.setEnabled(False)
        self.update_button_colors()

    def delete_selected(self):
        selected_travels = self.travels_list.selectedItems()
        if selected_travels:
            selected_travel = selected_travels[0].travel
            self.app.travels.remove(selected_travel)
        self.update_travels_list()
        self.clear_detail()
        self.disable_buttons()

    def open_confirm_decision(self):
        travel_name = self.travels_list.selectedItems()[0].travel.name
        self.confirm_decision = ConfirmWindow(self, "wyjazd " + travel_name)
        self.close()
        self.confirm_decision.show()

    def open_edit_window(self):
        self.choose_action_window = ChooseActionWindow(self, self.travels_list.selectedItems()[0].travel)
        self.close()
        self.choose_action_window.show()

    def update_details(self):
        selected_travels = self.travels_list.selectedItems()
        if selected_travels:
            travel = selected_travels[0].travel
            self.destination_view.setText(travel.destination if travel.destination is not None else "")
            self.transport_to_view.setText(travel.transport_to.transport_type if travel.transport_to is not None else "")
            self.transport_from_view.setText(travel.transport_from.transport_type if travel.transport_from is not None else "")
            self.accommodation_view.setText(travel.accommodation.name if travel.accommodation is not None else "")
            self.date_view.setText(str(travel.start_date) + " - " + str(travel.end_date))
            self.temperature_view.setText(str(travel.medium_temp))
            self.days_view.setText(str(travel.days))

    def clear_detail(self):
        self.destination_view.clear()
        self.transport_to_view.clear()
        self.transport_from_view.clear()
        self.accommodation_view.clear()
        self.date_view.clear()
        self.days_view.clear()

    def save(self):
        self.app.save_to_file()

    def load(self):
        self.app.load_from_file()
        self.update_travels_list()

    def add_to_calendar(self):
        selected_travels = self.travels_list.selectedItems()
        if selected_travels:
            travel = selected_travels[0].travel
            travel.add_to_calendar()


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
    viewer = MainWindow(App())
    viewer.show()
    sys.exit(app.exec())
