import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QMessageBox
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon
from Backend.Localization import Localization


class AddAccommodationWindow(QMainWindow):
    def __init__(self, previous_window, travel):
        super().__init__()

        self.previous_window = previous_window
        self.travel = travel

        self.setWindowTitle("Zakwaterowanie")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.top_layout = QVBoxLayout()

        self.name_label = QLabel("Nazwa *")
        self.top_layout.addWidget(self.name_label)

        self.name_view = QLineEdit()
        self.name_view.setReadOnly(False)
        self.top_layout.addWidget(self.name_view)

        self.city_label = QLabel("Miasto *")
        self.top_layout.addWidget(self.city_label)

        self.city_view = QLineEdit()
        self.city_view.setReadOnly(False)
        self.top_layout.addWidget(self.city_view)

        self.post_label = QLabel("Kod pocztowy *")
        self.top_layout.addWidget(self.post_label)

        self.post_view = QLineEdit()
        self.post_view.setReadOnly(False)
        self.top_layout.addWidget(self.post_view)

        self.street_label = QLabel("Ulica *")
        self.top_layout.addWidget(self.street_label)

        self.street_view = QLineEdit()
        self.street_view.setReadOnly(False)
        self.top_layout.addWidget(self.street_view)

        self.building_label = QLabel("Nr budynku *")
        self.top_layout.addWidget(self.building_label)

        self.building_view = QLineEdit()
        self.building_view.setReadOnly(False)
        self.top_layout.addWidget(self.building_view)

        self.apartment_label = QLabel("Nr mieszkania")
        self.top_layout.addWidget(self.apartment_label)

        self.apartment_view = QLineEdit()
        self.apartment_view.setReadOnly(False)
        self.top_layout.addWidget(self.apartment_view)

        self.bottom_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")
        self.cancel_button.clicked.connect(self.cancel)

        self.bottom_layout.addWidget(self.cancel_button)

        self.save_button = QPushButton("Zapisz")
        self.save_button.setStyleSheet("background-color: darkgreen; color: black;")
        self.save_button.clicked.connect(self.save)

        self.bottom_layout.addWidget(self.save_button)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)

        self.load()

    def load(self):
        if self.travel.accommodation:
            self.name_view.setText(self.travel.accommodation.name)
            self.city_view.setText(self.travel.accommodation.localization.city)
            self.post_view.setText(self.travel.accommodation.localization.post_code)
            self.street_view.setText(self.travel.accommodation.localization.street_name)
            self.building_view.setText(self.travel.accommodation.localization.building_number)
            self.apartment_view.setText(self.travel.accommodation.localization.apartment_number)

    def cancel(self):
        self.close()
        self.previous_window.show()

    def save(self):
        name = self.name_view.text()
        city = self.city_view.text()
        street = self.street_view.text()
        post = self.post_view.text()
        building = self.building_view.text()
        apartment = self.apartment_view.text()
        if name and city and street and post and building:
            self.travel.accommodation = name, city, street, post, building, apartment
            self.close()
            self.previous_window.show()
            self.previous_window.update_details()
        else:
            error_message = "Proszę uzupełnić wszystkie wymagane\npola oznaczone znakiem *"
            QMessageBox.critical(self, "Błąd", error_message)


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
    viewer = AddAccommodationWindow(None, None)
    viewer.show()
    sys.exit(app.exec())