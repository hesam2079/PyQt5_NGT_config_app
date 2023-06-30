import sys
import json
import time

import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget

class PinStatus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON Reader App")
        self.setStyleSheet("background-color: #F0F0F0;")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        self.label = QLabel()
        self.label.setStyleSheet("color: #333333; font-size: 14px;")
        self.layout.addWidget(self.label)

    def load_json(self, filename):
        with open(filename) as f:
            data = json.load(f)
        return data

    def display_json(self, data):
        content = ""
        for item, value in data.items():
            content += f"<span style='color: #007BFF;'>{item}</span>: <span style='color: #28A745;'>{value}</span><br>"
        self.label.setText(f"<html><body>{content}</body></html>")

def get_pin_status(port="COM9", baudrate=9600):
    ser = serial.Serial(port, baudrate, timeout=0.1)
    request = {"cn_m": "pin_status"}
    ser.write(bytes(request, 'utf-8'))
    time.sleep(0.05)
    data = ser.readline()
    return data

def test_pin_status():
    data = {"pin1": "HIGH",
            "pin2": "LOW",
            "pin3": "1.25",
            "pin4": "HIGH"}
    return data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PinStatus()
    window.show()

    # Replace 'data.json' with the path to your .json file
    test_json_data = test_pin_status()
    #json_data = get_pin_status()
    window.display_json(test_json_data)

    sys.exit(app.exec_())
