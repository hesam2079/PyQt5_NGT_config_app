import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.pin_status_window = None
        self.config_window = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Welcome Page')

        #welcome_label =

        button1 = QPushButton('Config', self)
        button1.clicked.connect(self.launch_file1)
        button1.setGeometry(50, 50, 200, 50)

        button2 = QPushButton('Pin Status', self)
        button2.clicked.connect(self.launch_file2)
        button2.setGeometry(50, 120, 200, 50)

        self.setGeometry(300, 300, 300, 200)
        self.show()

    def launch_file1(self):
        self.close()
        from config import Config
        self.config_window = Config()
        self.config_window.show()

    def launch_file2(self):
        self.close()
        from pin_status import PinStatus
        self.pin_status_window = PinStatus()
        self.pin_status_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome_page = WelcomePage()
    sys.exit(app.exec_())
