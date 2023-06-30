import json
import sys
import time
from serial.tools import list_ports
import serial
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, \
    QGroupBox, QFrame, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QFileDialog, QMessageBox
from PyQt5 import QtCore

text_font = QFont()  # Get the existing font from the label
text_font.setPointSize(10)  # Set the desired font size

group_box_title_font = QFont()
group_box_title_font.setPointSize(12)

class ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = {
            "cn_m": "config",
            "ssid": "",
            "pass": "",
            "mq_ser": "",
            "mq_po": "",
            "mq_un": "",
            "mq_pass": "",
            "ci": "",
            "fre": "",
            "SiBa": "",
            "SpFa": "",
            "SyWo": "",
            "CoR4": "",
            "TxP": "",
            "Ga": ""
        }
        self.data_pin_status = {
            "cn_m": "pin_status",
            "DI1": "",
            "DI2": "",
            "DO1": "",
            "DO2": "",
            "AL": "",
        }
        self.port_name = []
        self.device_name = []

        # Set window properties
        self.setWindowTitle("NGT App")
        self.setGeometry(100, 100, 900, 400)

        # Create the QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create the first tab
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Config")

        # Create a QHBoxLayout for tab1
        self.layout_config = QHBoxLayout(self.tab1)

        # Create the second tab
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "PIN Status")

        # Create a QHBoxLayout for tab2
        self.layout_pin_status = QHBoxLayout(self.tab2)

        # Config page
        for i in range(1, 6):
            group_box = QGroupBox()
            group_box.setFont(group_box_title_font)
            frame = QFrame()

            if i == 1:
                layout = QVBoxLayout(frame)

                # Add a logo to Group 1
                frame.setFrameShape(QFrame.NoFrame)
                logo_label = QLabel()
                logo_pixmap = QPixmap("NGT_logo.png")  # Replace "logo.png" with the path to your logo image
                # Resize the logo pixmap to a specific with and height
                logo_pixmap = logo_pixmap.scaled(120, 120, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                logo_label.setPixmap(logo_pixmap)
                layout.addWidget(logo_label)

                # Add spacer item below the logo
                spacer_item_logo = QSpacerItem(QSizePolicy.Minimum, 40)
                layout.addItem(spacer_item_logo)

                # Add QComboBox for options
                self.combo_box_config = QComboBox()
                self.combo_box_config.setFixedSize(120,27)
                self.combo_box_config.setFont(text_font)
                layout.addWidget(self.combo_box_config)

                # Add refresh button
                self.refresh_button_config = QPushButton("Refresh")
                self.refresh_button_config.setFixedSize(120, 25)
                self.refresh_button_config.setFont(text_font)
                layout.addWidget(self.refresh_button_config)

                # Add spacer below the buttons
                spacer_item_buttons = QSpacerItem(120, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item_buttons)

                # Customize the group box layout
                group_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
                group_box.setMinimumWidth(frame.sizeHint().width())
                group_box.setStyleSheet("QGroupBox { border: 0; }")  # Remove the frame around Group 1

                group_box.setLayout(layout)

            if i == 2:
                layout = QVBoxLayout(frame)

                ssid_label = QLabel("SSID")
                ssid_label.setFont(text_font)
                layout.addWidget(ssid_label)

                self.ssid_input = QLineEdit()
                self.ssid_input.setObjectName("ssid_input")
                layout.addWidget(self.ssid_input)

                password_label = QLabel("Password")
                password_label.setFont(text_font)
                layout.addWidget(password_label)

                self.password_input = QLineEdit()
                self.password_input.setObjectName("password_input")
                layout.addWidget(self.password_input)

                spacer_item = QSpacerItem(120, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item)

                group_box.setLayout(layout)
                group_box.setTitle("WiFi")

            if i == 3:
                layout = QVBoxLayout(frame)

                mqtt_ip_label = QLabel("MQTT IP")
                mqtt_ip_label.setFont(text_font)
                layout.addWidget(mqtt_ip_label)

                self.mqtt_ip_input = QLineEdit()
                self.mqtt_ip_input.setObjectName("mqtt_ip_input")
                layout.addWidget(self.mqtt_ip_input)

                mqtt_port_label = QLabel("MQTT Port")
                mqtt_port_label.setFont(text_font)
                layout.addWidget(mqtt_port_label)

                self.mqtt_port_input = QLineEdit()
                self.mqtt_port_input.setObjectName("mqtt_port_input")
                layout.addWidget(self.mqtt_port_input)

                mqtt_username_label = QLabel("MQTT Username")
                mqtt_username_label.setFont(text_font)
                layout.addWidget(mqtt_username_label)

                self.mqtt_username_input = QLineEdit()
                self.mqtt_username_input.setObjectName("mqtt_username_input")
                layout.addWidget(self.mqtt_username_input)

                mqtt_password_label = QLabel("MQTT Password")
                mqtt_password_label.setFont(text_font)
                layout.addWidget(mqtt_password_label)

                self.mqtt_password_input = QLineEdit()
                self.mqtt_password_input.setObjectName("mqtt_password_input")
                self.mqtt_password_input.setEchoMode(QLineEdit.Password)
                layout.addWidget(self.mqtt_password_input)

                mqtt_client_id_label = QLabel("MQTT Client ID")
                mqtt_client_id_label.setFont(text_font)
                layout.addWidget(mqtt_client_id_label)

                self.mqtt_client_id_input = QLineEdit()
                self.mqtt_client_id_input.setObjectName("mqtt_client_id_input")
                layout.addWidget(self.mqtt_client_id_input)

                spacer_item = QSpacerItem(120, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item)

                group_box.setLayout(layout)
                group_box.setTitle("MQTT")

            if i == 4:
                layout = QVBoxLayout(frame)

                frequency_label = QLabel("Frequency")
                frequency_label.setFont(text_font)
                layout.addWidget(frequency_label)

                self.frequency_input = QLineEdit()
                self.frequency_input.setObjectName("frequency_input")
                layout.addWidget(self.frequency_input)

                signal_bw_label = QLabel("Signal Bandwidth")
                signal_bw_label.setFont(text_font)
                layout.addWidget(signal_bw_label)

                self.signal_bw_input = QLineEdit()
                self.signal_bw_input.setObjectName("signal_bw_input")
                layout.addWidget(self.signal_bw_input)

                spreading_factor_label = QLabel("Spreading Factor")
                spreading_factor_label.setFont(text_font)
                layout.addWidget(spreading_factor_label)

                self.spreading_factor_input = QLineEdit()
                self.spreading_factor_input.setObjectName("spreading_factor_input")
                layout.addWidget(self.spreading_factor_input)

                sync_word_label = QLabel("Sync Word")
                sync_word_label.setFont(text_font)
                layout.addWidget(sync_word_label)

                self.sync_word_input = QLineEdit()
                self.sync_word_input.setObjectName("sync_word_input")
                layout.addWidget(self.sync_word_input)

                coding_rate_label = QLabel("Coding Rate4")
                coding_rate_label.setFont(text_font)
                layout.addWidget(coding_rate_label)

                self.coding_rate_input = QLineEdit()
                self.coding_rate_input.setObjectName("coding_rate_input")
                layout.addWidget(self.coding_rate_input)

                tx_power_label = QLabel("Tx Power")
                tx_power_label.setFont(text_font)
                layout.addWidget(tx_power_label)

                self.tx_power_input = QLineEdit()
                self.tx_power_input.setObjectName("tx_power_input")
                layout.addWidget(self.tx_power_input)

                gain_label = QLabel("Gain")
                gain_label.setFont(text_font)
                layout.addWidget(gain_label)

                self.gain_input = QLineEdit()
                self.gain_input.setObjectName("gain_input")
                layout.addWidget(self.gain_input)

                spacer_item = QSpacerItem(120, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item)

                group_box.setLayout(layout)
                group_box.setTitle("LoraWan")

            if i == 5:
                layout = QVBoxLayout(frame)

                # Create buttons for Group 6
                self.save_button_config = QPushButton("Save")
                self.save_button_config.setFixedSize(105, 25)
                self.save_button_config.setFont(text_font)
                self.load_button_config = QPushButton("Load")
                self.load_button_config.setFixedSize(105, 25)
                self.load_button_config.setFont(text_font)
                self.submit_button_config = QPushButton("Submit")
                self.submit_button_config.setFixedSize(105, 25)
                self.submit_button_config.setFont(text_font)

                layout.addWidget(self.save_button_config)
                layout.addWidget(self.load_button_config)
                layout.addWidget(self.submit_button_config)

                # Add spacer below the buttons
                spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item)

                group_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
                group_box.setMinimumWidth(frame.sizeHint().width())
                group_box.setTitle("Save / Submit")

                group_box.setLayout(layout)

            self.layout_config.addWidget(group_box)

        # Pin Status Page
        for i in range(1, 6):
            group_box = QGroupBox()
            group_box.setFont(group_box_title_font)
            frame = QFrame()

            if i == 1:
                layout = QVBoxLayout(frame)

                # Add a logo to Group 1
                frame.setFrameShape(QFrame.NoFrame)
                logo_label = QLabel()
                logo_pixmap = QPixmap("NGT_logo.png")  # Replace "logo.png" with the path to your logo image
                # Resize the logo pixmap to a specific with and height
                logo_pixmap = logo_pixmap.scaled(120, 120, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                logo_label.setPixmap(logo_pixmap)
                layout.addWidget(logo_label)

                # Add spacer item below the logo
                spacer_item_logo = QSpacerItem(QSizePolicy.Minimum, 40)
                layout.addItem(spacer_item_logo)

                # Add QComboBox for options
                self.combo_box_pin_status = QComboBox()
                self.combo_box_pin_status.setFixedSize(120, 27)
                self.combo_box_pin_status.setFont(text_font)
                layout.addWidget(self.combo_box_pin_status)

                # Add refresh button
                self.refresh_button_pin_status = QPushButton("Refresh")
                self.refresh_button_pin_status.setFixedSize(120, 25)
                self.refresh_button_pin_status.setFont(text_font)
                layout.addWidget(self.refresh_button_pin_status)

                # Add spacer below the buttons
                spacer_item = QSpacerItem(120, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item)

                group_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
                group_box.setMinimumWidth(frame.sizeHint().width())
                group_box.setStyleSheet("QGroupBox { border: 0; }")  # Remove the frame around Group 1

                group_box.setLayout(layout)

            if i == 2:
                layout = QVBoxLayout(frame)

                spacer_item = QSpacerItem(120, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item)

                group_box.setLayout(layout)
                group_box.setTitle("Digital Input")

            if i == 3:
                layout = QVBoxLayout(frame)

                spacer_item = QSpacerItem(120, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item)

                group_box.setLayout(layout)
                group_box.setTitle("Analog Input")

            if i == 4:
                layout = QVBoxLayout(frame)

                spacer_item = QSpacerItem(120, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item)

                group_box.setLayout(layout)
                group_box.setTitle("Digital Output")

            if i == 5:
                layout = QVBoxLayout(frame)

                # Create buttons for Group 6
                self.save_button_pin = QPushButton("Save")
                self.save_button_pin.setFixedSize(105, 25)
                self.save_button_pin.setFont(text_font)
                self.request_button = QPushButton("Request")
                self.request_button.setFixedSize(105, 25)
                self.request_button.setFont(text_font)
                layout.addWidget(self.save_button_pin)
                layout.addWidget(self.request_button)

                # Add spacer below the buttons
                spacer_item = QSpacerItem(20, 40)
                layout.addItem(spacer_item)

                # Add Auto Request label
                auto_request_label = QLabel("Auto Request")
                layout.addWidget(auto_request_label)

                # Add spacer
                spacer_item_auto_request_time = QSpacerItem(0, 10)
                layout.addItem(spacer_item_auto_request_time)

                # Add label for input time
                auto_request_input_label = QLabel("Time")
                auto_request_input_label.setFont(text_font)
                layout.addWidget(auto_request_input_label)

                # Add input field
                self.auto_request_time = QLineEdit()
                self.auto_request_time.setFont(text_font)
                self.auto_request_time.setPlaceholderText("Min: 5 Sec")
                self.auto_request_time.setFixedSize(105, 25)
                layout.addWidget(self.auto_request_time)

                # Add auto request run button
                self.auto_request_button = QPushButton("Run")
                self.auto_request_button.setFont(text_font)
                layout.addWidget(self.auto_request_button)

                # Add spacer below Auto request
                spacer_item_auto_request = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                layout.addItem(spacer_item_auto_request)

                # Customize group box
                group_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
                group_box.setMinimumWidth(frame.sizeHint().width())
                group_box.setTitle("Save / Request")

                group_box.setLayout(layout)

            self.layout_pin_status.addWidget(group_box)

        # Buttons click handler
        self.save_button_config.clicked.connect(self.save_button_config_clicked)
        self.load_button_config.clicked.connect(self.load_button_config_clicked)
        self.refresh_button_config.clicked.connect(self.refresh_button_clicked)
        self.refresh_button_pin_status.clicked.connect(self.refresh_button_clicked)
        self.submit_button_config.clicked.connect(self.submit_button_config_clicked)
        self.save_button_pin.clicked.connect(self.save_button_pin_clicked)
        self.request_button.clicked.connect(self.request_button_clicked)
        self.auto_request_button.clicked.connect(self.auto_request_button_clicked)
        self.combo_box_pin_status.currentIndexChanged.connect(self.combo_box_current_item)
        self.combo_box_pin_status.currentIndexChanged.connect(self.combo_box_current_item)

    def save_data_json(self):
        self.data = {
            "cn_m": "config",
            "ssid": self.ssid_input.text(),
            "pass": self.password_input.text(),
            "mq_ser": self.mqtt_ip_input.text(),
            "mq_po": self.mqtt_port_input.text(),
            "mq_un": self.mqtt_username_input.text(),
            "mq_pass": self.mqtt_password_input.text(),
            "ci": self.mqtt_client_id_input.text(),
            "fre": self.frequency_input.text(),
            "SiBa": self.signal_bw_input.text(),
            "SpFa": self.spreading_factor_input.text(),
            "SyWo": self.sync_word_input.text(),
            "CoR4": self.coding_rate_input.text(),
            "TxP": self.tx_power_input.text(),
            "Ga": self.gain_input.text()
        }

    def save_button_config_clicked(self):
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

    def load_button_config_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'json files (*.json)')

        if file_path:
            with open(file_path, 'r') as file:
                try:
                    self.data = json.load(file)
                    self.ssid_input.setText(self.data['ssid'])
                    self.password_input.setText(self.data['pass'])
                    self.mqtt_ip_input.setText(self.data['mq_ser'])
                    self.mqtt_port_input.setText(self.data['mq_po'])
                    self.mqtt_username_input.setText(self.data['mq_un'])
                    self.mqtt_password_input.setText(self.data['mq_pass'])
                    self.frequency_input.setText(self.data['fre'])
                    self.signal_bw_input.setText(self.data['SiBa'])
                    self.spreading_factor_input.setText(self.data['SpFa'])
                    self.sync_word_input.setText(self.data['SyWo'])
                    self.coding_rate_input.setText(self.data['CoR4'])
                    self.tx_power_input.setText(self.data['TxP'])
                    self.gain_input.setText(self.data['Ga'])
                except Exception as e:
                    QMessageBox.information(self, "Loading Error", f"Exeption Error: {str(e)}")

    def submit_button_config_clicked(self):
        try:
            self.save_data_json()
            QMessageBox.information(self, "submitting", "Precess start Successfully!")
            # Convert the data to a JSON string
            json_data = json.dumps(self.data)
            # Configure the serial connection
            port = str(self.combo_box_config.currentText())
            ser = serial.Serial(port, 115200, timeout=0.1)
            ser.write(bytes(json_data, 'utf-8'))
            time.sleep(0.05)
            QMessageBox.information(self, "Success", "Config submit successfully!")
        except serial.SerialException as e:
            QMessageBox.information(self, "Serial Error", f"Serial Exception Error: {str(e)}")
        except Exception as e:
            QMessageBox.information(self, "Error", f"Exeption Error: {str(e)}")

    def refresh_button_clicked(self):
        try:
            # Show the refreshing message pop-up
            QMessageBox.information(self, "Refresh COM ports", "Refreshing start successfully!")
            self.refresh_data()
            self.combo_box_config.clear()
            self.combo_box_pin_status.clear()
            for port in self.port_name:
                self.combo_box_config.addItem(f"{port}")
                self.combo_box_pin_status.addItem((f"{port}"))
            QMessageBox.information(self, "Refreshing finished", "Refresh process finished")
        except Exception as e:
            QMessageBox.information(self, "Error", f"Exception Error: {str(e)}")

    def refresh_data(self):
        # Your refreshing logic here
        ports = list(serial.tools.list_ports.comports())
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

    def combo_box_current_item(self):
        if self.combo_box_pin_status.currentIndexChanged:
            self.combo_box_pin_status.setCurrentText(self.combo_box_config.currentText())
        else:
            self.combo_box_config.setCurrentText(self.combo_box_pin_status.currentText())

    def save_pin_status_data_json(self):
        print("pin status data saved!")

    def save_button_pin_clicked(self):
        self.save_pin_status_data_json()
        print("save button clicked!")

    def request_button_clicked(self):
        print("request button clicked!")

    def auto_request_button_clicked(self):
        print("auto request button clicked!")
        current_text = self.auto_request_button.text()
        if current_text == "Run":
            print("sending Request is running!")
            self.auto_request_button.setText("Stop")
        if current_text == "Stop":
            print("sending Request is stop!")
            self.auto_request_button.setText("Run")


if __name__ == "__main__":
    app = QApplication([])
    window = ui()
    window.show()
    app.exec_()