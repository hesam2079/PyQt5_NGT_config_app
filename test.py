import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QLabel

# Example JSON string
json_str = '''{
  "cn_m": "pin_status",
  "digital_in": {
    "di1": "1",
    "di2": "0"
  },
  "digital_out": {
    "do1": "0",
    "do2": "0"
  },
  "analog_in": {
    "ai_1": "1022"
    }
}'''

class JSONViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON Viewer")

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Parse JSON string into a Python data structure (dictionary)
        data = json.loads(json_str)

        if "digital_in" in data:
            digital_in_data = data["digital_in"]

            group_box = QGroupBox("digital_in")
            group_layout = QVBoxLayout()
            group_box.setLayout(group_layout)

            for key, value in digital_in_data.items():
                label = QLabel(f"{key}: {value}")
                group_layout.addWidget(label)

            layout.addWidget(group_box)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = JSONViewer()
    sys.exit(app.exec_())
