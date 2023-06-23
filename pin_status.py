import sys
import serial
import json
from PyQt5.QtWidgets import QApplication, QMainWindow

from pin_status_ui import pin_status_ui

class pin_status(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = pin_status_ui()
        self.setCentralWidget(self.widget)

    def show_widget(self):
        self.widget.show()

    def read_json_from_serial(self):
        '''
        ser = serial.Serial(port, 9600)  # Modify the port and baud rate as per your requirement
        while True:
            try:
                data = ser.readline().decode('utf-8').strip()
                json_data = json.loads(data)
                self.widget.update_pins(json_data)
            except KeyboardInterrupt:
                ser.close()
                break
            except Exception as e:
                print(f"Error reading JSON: {e}")
        '''
        sample_data = {
            "pin1": "HIGH",
            "pin2": "LOW",
            "pin3": "HIGH",
            "pin4": "0.1",
            "pin10": "125"
        }
        self.widget.update_pins(sample_data)


def main():
    app = QApplication(sys.argv)

    window = pin_status()
    window.show_widget()
    window.read_json_from_serial()  # Modify the port as per your requirement
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
