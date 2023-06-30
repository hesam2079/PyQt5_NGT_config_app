import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTabWidget

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create the main layout (Horizontal layout)
        self.layout_main = QHBoxLayout()
        self.setLayout(self.layout_main)

        # Add your logo
        logo_label = QLabel("Your Logo Here")
        self.layout_main.addWidget(logo_label)

        # Create a QTabWidget to hold your layouts
        tab_widget = QTabWidget()

        # Create tab 1 and add self.layout_config to it
        tab1 = QWidget()
        layout_tab1 = QVBoxLayout(tab1)
        layout_tab1.addLayout(self.layout_config)
        tab_widget.addTab(tab1, "Tab 1")

        # Create tab 2 and add self.layout_pin_status to it
        tab2 = QWidget()
        layout_tab2 = QVBoxLayout(tab2)
        layout_tab2.addLayout(self.layout_pin_status)
        tab_widget.addTab(tab2, "Tab 2")

        # Add the QTabWidget to the main layout
        self.layout_main.addWidget(tab_widget)

# Replace `self.layout_config` and `self.layout_pin_status` with your actual layouts
# self.layout_config = QVBoxLayout()  # Your layout 1
# self.layout_pin_status = QVBoxLayout()  # Your layout 2

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_widget = MainWidget()
    main_widget.show()

    sys.exit(app.exec_())
