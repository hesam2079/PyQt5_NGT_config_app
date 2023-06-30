import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction, QFileDialog, QDialog
import sample
import serial
from serial.tools import list_ports
import time



# Function for save data fields to class data attribute
def save_data_json(self):
    self.data = {
        "cn_m": "config",
        "ssid": self.text(),
        "pass": self.ui.password_textfield.text(),
        "mq_ser": self.ui.mqtt_server_textfield.text(),
        "mq_po": self.ui.mqtt_port_textfield.text(),
        "mq_un": self.ui.mqtt_username_textfield.text(),
        "mq_pass": self.ui.mqtt_password_textfield.text(),
        "ci": self.ui.mqtt_client_id_textfield.text(),
        "fre": self.ui.lorawan_frequency_textfield.text(),
        "SiBa": self.ui.lorawan_signal_bandwidth_textfield.text(),
        "SpFa": self.ui.lorawan_spreading_factor_textfield.text(),
        "SyWo": self.ui.lorawan_sync_word_textfield.text(),
        "CoR4": self.ui.lorawan_coding_rate4_textfield.text(),
        "TxP": self.ui.lorawan_tx_power_textfield.text(),
        "Ga": self.ui.lorawan_gain_textfield.text()
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
                self.ui.password_textfield.setText(self.data['pass'])
                self.ui.mqtt_server_textfield.setText(self.data['mq_ser'])
                self.ui.mqtt_port_textfield.setText(self.data['mq_po'])
                self.ui.mqtt_username_textfield.setText(self.data['mq_un'])
                self.ui.mqtt_password_textfield.setText(self.data['mq_pass'])
                self.ui.lorawan_frequency_textfield.setText(self.data['fre'])
                self.ui.lorawan_signal_bandwidth_textfield.setText(self.data['SiBa'])
                self.ui.lorawan_spreading_factor_textfield.setText(self.data['SpFa'])
                self.ui.lorawan_sync_word_textfield.setText(self.data['SyWo'])
                self.ui.lorawan_coding_rate4_textfield.setText(self.data['CoR4'])
                self.ui.lorawan_tx_power_textfield.setText(self.data['TxP'])
                self.ui.lorawan_gain_textfield.setText(self.data['Ga'])
            except Exception as e:
                QMessageBox.information(self, "Loading Error", f"Exeption Error: {str(e)}")

# Function to handle the send button click event
def submit_button_clicked(self):
    try:
        self.save_data_json()
        QMessageBox.information(self, "submitting", "Precess start Successfully!")
        # Convert the data to a JSON string
        json_data = json.dumps(self.data)
        # Configure the serial connection
        port = str(self.ui.com_port_combobox.currentText())
        ser = serial.Serial(port, 115200, timeout=0.1)
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
    app = QApplication([])
    ui = sample.ui
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
