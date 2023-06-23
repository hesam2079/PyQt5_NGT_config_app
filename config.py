import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction, QFileDialog
from config_ui import config_ui
import serial
from serial.tools import list_ports
import time


class config(QMainWindow):
    def __init__(self):
        super().__init__()

        # Class Atributes
        self.data = None

        # Set ui the UI
        self.ui = config_ui()
        self.ui.setupUi(self)

        self.port_name = []
        self.device_name = []


        # Connect buttons clicked signal to the buttonClicked method
        self.ui.save_button.clicked.connect(self.save_button_clicked)
        self.ui.load_button.clicked.connect(self.load_button_clicked)
        self.ui.submit_button.clicked.connect(self.submit_button_clicked)
        self.ui.refresh_button.clicked.connect(self.refresh_button_clicked)

    # Function for save data fields to class data attribute
    def save_data_json(self):
        self.data = {
            "ssid": self.ui.ssid_textfield.text(),
            "password": self.ui.password_textfield.text(),
            "mqtt_server": self.ui.mqtt_ip_textfield.text(),
            "mqtt_username": self.ui.mqtt_username_textfield.text(),
            "mqtt_password": self.ui.mqtt_password_textfield.text(),
            "LB": self.ui.lorawan_baud_rate_textfield.text(),
            "SignalBandwidth": self.ui.lorawan_signal_bandwidth_textfield.text(),
            "SpreadingFactor": self.ui.lorawan_spreading_factor_textfield.text(),
            "SyncWord": self.ui.lorawan_sync_word_textfield.text(),
            "CodingRate4": self.ui.lorawan_coding_rate4_textfield.text(),
            "TxPower": self.ui.lorawan_tx_power_textfield.text(),
            "Gain": self.ui.lorawan_gain_textfield.text()
        }

    # Save button clicked handler
    def save_button_clicked(self):
        self.save_data_json()
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'json files (*.json)')

        if file_path:
            # Save the data to a JSON file
            try:
                with open(file_path, "w") as file:
                    json.dump(self.data, file)
                QMessageBox.information(self, "Success", "Data saved successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save data: {str(e)}")

    # Load button clicked handler
    def load_button_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'json files (*.json)')

        if file_path:
            with open(file_path, 'r') as file:
                try:
                    self.data = json.load(file)
                    self.ui.ssid_textfield.setText(self.data['ssid'])
                    self.ui.password_textfield.setText(self.data['password'])
                    self.ui.mqtt_ip_textfield.setText(self.data['mqtt_server'])
                    self.ui.mqtt_username_textfield.setText(self.data['mqtt_username'])
                    self.ui.mqtt_password_textfield.setText(self.data['mqtt_password'])
                    self.ui.lorawan_baud_rate_textfield.setText(self.data['LB'])
                    self.ui.lorawan_signal_bandwidth_textfield.setText(self.data['SignalBandwidth'])
                    self.ui.lorawan_spreading_factor_textfield.setText(self.data['SpreadingFactor'])
                    self.ui.lorawan_sync_word_textfield.setText(self.data['SyncWord'])
                    self.ui.lorawan_coding_rate4_textfield.setText(self.data['CodingRate4'])
                    self.ui.lorawan_tx_power_textfield.setText(self.data['TxPower'])
                    self.ui.lorawan_gain_textfield.setText(self.data['Gain'])
                except Exception as e:
                    QMessageBox.information(self, "Loading Error", f"Exeption Error: {str(e)}")

    # Function to handle the send button click event
    def submit_button_clicked(self):
        try:
            self.save_data_json()
            QMessageBox.information(self, "submitting", "Precess start Successfully!")
            # Convert the data to a JSON string
            json_data = json.dumps(self.data)
            connection_mode = {"connection_mode": "pin_status"}
            json_connection_mode = json.dumps(connection_mode)
            # Configure the serial connection
            port = str(self.ui.com_port_combobox.currentText())
            ser = serial.Serial(port, 9600, timeout=11)
            ser.write(bytes(json_connection_mode, 'utf-8'))
            time.sleep(10)
            ser.write(bytes(json_data, 'utf-8'))
            time.sleep(0.05)
            QMessageBox.information(self, "Success", "Config submit successfully!")
        except serial.SerialException as e:
            QMessageBox.information(self, "Serial Error", f"Serial Exception Error: {str(e)}")
        except Exception as e:
            QMessageBox.information(self, "Error", f"Exeption Error: {str(e)}")

    # Refresh button clicked handler
    def refresh_button_clicked(self):
        try:
            # Show the refreshing message pop-up
            QMessageBox.information(self, "Refresh COM ports", "Refreshing start successfully!")
            self.refresh_data()
            QMessageBox.information(self, "Refreshing finished", "Refresh process finished")
        except Exception as e:
            QMessageBox.information(self, "Error", f"Exception Error: {str(e)}")

    # Function for refreshing data
    def refresh_data(self):
        # Your refreshing logic here
        ports = list(serial.tools.list_ports.comports())
        self.ui.com_port_combobox.clear()
        external_ports = []
        for port in ports:
            try:
                external_ports.append(port)
            except (OSError, serial.SerialException):
                # If opening the port fails, it means there is no device connected to it
                pass
        if external_ports:
            for port in external_ports:
                self.port_name.append(port.device)
                self.device_name.append(port.description)
                port_info = f"{port.device}"
                self.ui.com_port_combobox.addItem(port_info)


def main():
    app = QApplication(sys.argv)
    window = config()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()