import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import config
import pin_status

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome Page')
        self.resize(400, 300)  # Set the size of the window

        # Create and customize the welcome label
        welcome_label = QLabel('Welcome to My App')
        welcome_label.setStyleSheet('font-size: 24px; font-weight: bold;')

        # Create buttons
        config_button = QPushButton('Config')
        pin_status_button = QPushButton('Pin Status')

        # Create a layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(config_button)
        button_layout.addWidget(pin_status_button)

        # Create a layout for the welcome page
        layout = QVBoxLayout()
        layout.addWidget(welcome_label)
        layout.addStretch(1)  # Add some empty space
        layout.addLayout(button_layout)

        # Set the layout for the welcome page
        self.setLayout(layout)

        # Connect button signals to slots
        config_button.clicked.connect(self.open_config_ui)
        pin_status_button.clicked.connect(self.open_pin_status_ui)

    def open_config_ui(self):
        config

    def open_pin_status_ui(self):
        pin_status


if __name__ == '__main__':
    app = QApplication(sys.argv)

    welcome_page = WelcomePage()
    welcome_page.show()

    sys.exit(app.exec_())
