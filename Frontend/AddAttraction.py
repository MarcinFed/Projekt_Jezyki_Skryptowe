import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,\
                            QLabel, QLineEdit, QPushButton, QDateTimeEdit, QFileDialog, QStyleFactory,  QSpacerItem, QSizePolicy, QTimeEdit, QCheckBox
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtGui import QPalette, QColor, QIcon


class AddAttractionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atrakcja")
        self.setWindowIcon(QIcon("Logo.jpg"))
        self.setMinimumWidth(400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.name_label = QLabel("Nazwa")
        self.main_layout.addWidget(self.name_label)

        self.name_view = QLineEdit()
        self.name_view.setReadOnly(False)
        self.main_layout.addWidget(self.name_view)

        self.from_hour_label = QLabel("Godzina rozpoczęcia")
        self.main_layout.addWidget(self.from_hour_label)

        self.from_hour_view = QTimeEdit()
        self.from_hour_view.setDisplayFormat("HH:mm")
        self.main_layout.addWidget(self.from_hour_view)

        self.to_hour_label = QLabel("Godzina zakończenia")
        self.main_layout.addWidget(self.to_hour_label)

        self.to_hour_view = QTimeEdit()
        self.to_hour_view.setDisplayFormat("HH:mm")
        self.main_layout.addWidget(self.to_hour_view)

        self.city_label = QLabel("Miasto")
        self.main_layout.addWidget(self.city_label)

        self.city_view = QLineEdit()
        self.city_view.setReadOnly(False)
        self.main_layout.addWidget(self.city_view)

        self.street_label = QLabel("Ulica")
        self.main_layout.addWidget(self.street_label)

        self.street_view = QLineEdit()
        self.street_view.setReadOnly(False)
        self.main_layout.addWidget(self.street_view)

        self.post_label = QLabel("Kod pocztowy")
        self.main_layout.addWidget(self.post_label)

        self.post_view = QLineEdit()
        self.post_view.setReadOnly(False)
        self.main_layout.addWidget(self.post_view)

        self.building_label = QLabel("Numer budynku")
        self.main_layout.addWidget(self.building_label)

        self.building_view = QLineEdit()
        self.building_view.setReadOnly(False)
        self.main_layout.addWidget(self.building_view)

        self.apartment_label = QLabel("Numer mieszkania")
        self.main_layout.addWidget(self.apartment_label)

        self.apartment_view = QLineEdit()
        self.apartment_view.setReadOnly(False)
        self.main_layout.addWidget(self.apartment_view)

        self.middle_top_layout = QHBoxLayout()

        self.ticket_label = QLabel("Bilet")
        self.middle_top_layout.addWidget(self.ticket_label)

        self.ticket_checkbox = QCheckBox()
        self.middle_top_layout.addWidget(self.ticket_checkbox)

        self.spacer = QSpacerItem(40,20,QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.middle_top_layout.addItem(self.spacer)

        self.main_layout.addLayout(self.middle_top_layout)

        self.middle_layout = QHBoxLayout()

        self.to_ticket_button = QPushButton("Dodaj bilet")
        self.middle_layout.addWidget(self.to_ticket_button)

        self.to_file_path_label = QLineEdit()
        self.to_file_path_label.setReadOnly(True)
        self.middle_layout.addWidget(self.to_file_path_label)

        self.main_layout.addLayout(self.middle_layout)

        self.middle_bottom_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.setStyleSheet("background-color: darkred; color: black;")
        self.middle_bottom_layout.addWidget(self.cancel_button)

        self.save_button = QPushButton("Zapisz")
        self.save_button.setStyleSheet("background-color: darkgreen; color: black;")

        self.middle_bottom_layout.addWidget(self.save_button)

        self.main_layout.addLayout(self.middle_bottom_layout)


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
    viewer = AddAccommodation()
    viewer.show()
    sys.exit(app.exec())