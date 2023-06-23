import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main widget and layout
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        # Create the tab widget
        self.tab_widget = QTabWidget(self.central_widget)
        self.layout.addWidget(self.tab_widget)

        # Add design files as tabs
        self.add_design_tab("Design 1", "pin_status_ui.py")
        self.add_design_tab("Design 2", "config_ui.py")

        # Set the central widget
        self.setCentralWidget(self.central_widget)

    def add_design_tab(self, title, file_path):
        # Execute the code from the generated design file
        with open(file_path, 'r') as file:
            code = file.read()
            exec(code, globals())

        # Extract the desired widget instance
        widget = globals().get("MainWidget")()

        # Add the widget to the tab
        self.tab_widget.addTab(widget, title)

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = MainWindow()
window.show()

# Run the event loop
sys.exit(app.exec_())
