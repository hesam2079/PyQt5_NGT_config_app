from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

class config_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 300)  # Initial size of the window


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # Create a QHBoxLayout to manage the overall layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Create a QFrame for the additional frame
        self.additional_frame = QtWidgets.QFrame(self.centralwidget)
        self.additional_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.additional_frame.setObjectName("additional_frame")

        # Create a QVBoxLayout for the additional frame
        self.additional_layout = QtWidgets.QVBoxLayout(self.additional_frame)
        self.additional_layout.setObjectName("additional_layout")

        # Logo widget
        self.logo_label = QtWidgets.QLabel(self.additional_frame)
        self.logo_label.setObjectName("logo_label")
        logo_pixmap = QtGui.QPixmap("NgLogo.png")  # Replace "logo.png" with the path to your logo image

        # Resize the logo pixmap to a specific with and height
        logo_pixmap = logo_pixmap.scaled(200, 200, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.additional_layout.addWidget(self.logo_label)



        # Add more widgets to the additional frame as needed

        self.horizontalLayout.addWidget(self.additional_frame)

        # Add your additional widgets to the additional frame
        # Example:
        # Logo widget
        self.logo_label = QtWidgets.QLabel(self.additional_frame)
        self.logo_label.setObjectName("logo_label")
        self.additional_layout.addWidget(self.logo_label)



        # Add more widgets to the additional frame as needed

        self.horizontalLayout.addWidget(self.additional_frame)

        # Create a QGroupBox for Wi-Fi settings
        self.wifi_groupBox = QtWidgets.QGroupBox("Wi-Fi Settings", self.centralwidget)
        self.wifi_groupBox.setObjectName("wifi_groupBox")

        # Create a QFormLayout for Wi-Fi settings
        self.wifi_formLayout = QtWidgets.QFormLayout(self.wifi_groupBox)
        self.wifi_formLayout.setObjectName("wifi_formLayout")

        # SSID text field
        self.ssid_label = QtWidgets.QLabel(self.wifi_groupBox)
        self.ssid_label.setObjectName("ssid_label")
        self.wifi_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ssid_label)

        self.ssid_textfield = QtWidgets.QLineEdit(self.wifi_groupBox)
        self.ssid_textfield.setObjectName("ssid_textfield")
        self.wifi_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ssid_textfield)

        # Password text field
        self.password_label = QtWidgets.QLabel(self.wifi_groupBox)
        self.password_label.setObjectName("password_label")
        self.wifi_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_label)

        self.password_textfield = QtWidgets.QLineEdit(self.wifi_groupBox)
        self.password_textfield.setObjectName("password_textfield")
        self.wifi_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_textfield)

        self.horizontalLayout.addWidget(self.wifi_groupBox)

        # Create a QGroupBox for server settings
        self.server_groupBox = QtWidgets.QGroupBox("Server Settings", self.centralwidget)
        self.server_groupBox.setObjectName("server_groupBox")

        # Create a QFormLayout for server settings
        self.server_formLayout = QtWidgets.QFormLayout(self.server_groupBox)
        self.server_formLayout.setObjectName("server_formLayout")

        # MQTT IP text field
        self.mqtt_ip_label = QtWidgets.QLabel(self.server_groupBox)
        self.mqtt_ip_label.setObjectName("mqtt_ip_label")
        self.server_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.mqtt_ip_label)

        self.mqtt_ip_textfield = QtWidgets.QLineEdit(self.server_groupBox)
        self.mqtt_ip_textfield.setObjectName("mqtt_ip_textfield")
        self.server_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mqtt_ip_textfield)

        # MQTT Username text field
        self.mqtt_username_label = QtWidgets.QLabel(self.server_groupBox)
        self.mqtt_username_label.setObjectName("mqtt_username_label")
        self.server_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mqtt_username_label)

        self.mqtt_username_textfield = QtWidgets.QLineEdit(self.server_groupBox)
        self.mqtt_username_textfield.setObjectName("mqtt_username_textfield")
        self.server_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mqtt_username_textfield)

        # MQTT Password text field
        self.mqtt_password_label = QtWidgets.QLabel(self.server_groupBox)
        self.mqtt_password_label.setObjectName("mqtt_password_label")
        self.server_formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.mqtt_password_label)

        self.mqtt_password_textfield = QtWidgets.QLineEdit(self.server_groupBox)
        self.mqtt_password_textfield.setObjectName("mqtt_password_textfield")
        self.server_formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mqtt_password_textfield)

        self.horizontalLayout.addWidget(self.server_groupBox)

        # Create a QGroupBox for lorawan settings
        self.lorawan_groupBox = QtWidgets.QGroupBox("LoraWan Settings", self.centralwidget)
        self.lorawan_groupBox.setObjectName("lorawan_groupBox")

        # Create a QFormlayout for lorawan settings
        self.lorawan_formLayout = QtWidgets.QFormLayout(self.lorawan_groupBox)
        self.lorawan_formLayout.setObjectName("lorawan_formLayout")

        # LoraWan baud rate
        self.lorawan_baud_rate_label = QtWidgets.QLabel(self.lorawan_groupBox)
        self.lorawan_baud_rate_label.setObjectName("lorawan_baud_rate_label")
        self.lorawan_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lorawan_baud_rate_label)

        self.lorawan_baud_rate_textfield = QtWidgets.QLineEdit(self.lorawan_groupBox)
        self.lorawan_baud_rate_textfield.setObjectName("lorawan_baud_rate_textfield")
        self.lorawan_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lorawan_baud_rate_textfield)

        # LoraWan Signal Bandwidth
        self.lorawan_signal_bandwidth_label = QtWidgets.QLabel(self.lorawan_groupBox)
        self.lorawan_signal_bandwidth_label.setObjectName("lorawan_signal_bandwidth_label")
        self.lorawan_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lorawan_signal_bandwidth_label)

        self.lorawan_signal_bandwidth_textfield = QtWidgets.QLineEdit(self.lorawan_groupBox)
        self.lorawan_signal_bandwidth_textfield.setObjectName("lorawan_signal_bandwidth_textfield")
        self.lorawan_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lorawan_signal_bandwidth_textfield)

        # LoraWan Spreading Factor
        self.lorawan_spreading_factor_label = QtWidgets.QLabel(self.lorawan_groupBox)
        self.lorawan_spreading_factor_label.setObjectName("lorawan_spreading_factor_label")
        self.lorawan_formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lorawan_spreading_factor_label)

        self.lorawan_spreading_factor_textfield = QtWidgets.QLineEdit(self.lorawan_groupBox)
        self.lorawan_spreading_factor_textfield.setObjectName("lorawan_spreading_factor_textfield")
        self.lorawan_formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lorawan_spreading_factor_textfield)

        # LoraWan Sync Word
        self.lorawan_sync_word_label = QtWidgets.QLabel(self.lorawan_groupBox)
        self.lorawan_sync_word_label.setObjectName("lorawan_sync_word_label")
        self.lorawan_formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lorawan_sync_word_label)

        self.lorawan_sync_word_textfield = QtWidgets.QLineEdit(self.lorawan_groupBox)
        self.lorawan_sync_word_textfield.setObjectName("lorawan_sync_word_textfield")
        self.lorawan_formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lorawan_sync_word_textfield)

        # LoraWan Coding Rate4
        self.lorawan_coding_rate4_label = QtWidgets.QLabel(self.lorawan_groupBox)
        self.lorawan_coding_rate4_label.setObjectName("lorawan_coding_rate4_label")
        self.lorawan_formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lorawan_coding_rate4_label)

        self.lorawan_coding_rate4_textfield = QtWidgets.QLineEdit(self.lorawan_groupBox)
        self.lorawan_coding_rate4_textfield.setObjectName("lorawan_coding_rate4_textfield")
        self.lorawan_formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lorawan_coding_rate4_textfield)

        # LoraWan TX Power
        self.lorawan_tx_power_label = QtWidgets.QLabel(self.lorawan_groupBox)
        self.lorawan_tx_power_label.setObjectName("lorawan_tx_power_label")
        self.lorawan_formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lorawan_tx_power_label)

        self.lorawan_tx_power_textfield = QtWidgets.QLineEdit(self.lorawan_groupBox)
        self.lorawan_tx_power_textfield.setObjectName("lorawan_tx_power_textfield")
        self.lorawan_formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lorawan_tx_power_textfield)

        # LoraWan Gain
        self.lorawan_gain_label = QtWidgets.QLabel(self.lorawan_groupBox)
        self.lorawan_gain_label.setObjectName("lorawan_gain_label")
        self.lorawan_formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lorawan_gain_label)

        self.lorawan_gain_textfield = QtWidgets.QLineEdit(self.lorawan_groupBox)
        self.lorawan_gain_textfield.setObjectName("lorawan_gain_textfield")
        self.lorawan_formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lorawan_gain_textfield)

        self.horizontalLayout.addWidget(self.lorawan_groupBox)

        # Create a QGroupBox for COM port settings
        self.com_groupBox = QtWidgets.QGroupBox("COM Port Settings", self.centralwidget)
        self.com_groupBox.setObjectName("com_groupBox")

        # Create a QFormLayout for COM port settings
        self.com_formLayout = QtWidgets.QFormLayout(self.com_groupBox)
        self.com_formLayout.setObjectName("com_formLayout")
        self.com_formLayout.setAlignment(QtCore.Qt.AlignCenter)

        # COM Port list
        self.com_port_label = QtWidgets.QLabel(self.com_groupBox)
        self.com_port_label.setObjectName("com_port_label")
        self.com_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.com_port_label)

        self.com_port_combobox = QtWidgets.QComboBox(self.com_groupBox)
        self.com_port_combobox.setObjectName("com_port_combobox")
        self.com_port_combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.com_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.com_port_combobox)


        # COM Port searching status label
        '''
        self.com_port_status_label = QtWidgets.QLabel(self.com_groupBox)
        self.com_port_status_label.setObjectName("com_port_status_label")
        self.com_port_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.com_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.com_port_status_label)
        self.com_formLayout.widget().setAlignment(QtCore.Qt.AlignCenter)
        '''
        # Refresh button
        self.refresh_button = QtWidgets.QPushButton("Refresh", self.com_groupBox)
        self.refresh_button.setObjectName("refresh_button")

        self.com_formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.refresh_button)

        # Add the COM port group box to the horizontal layout
        self.horizontalLayout.addWidget(self.com_groupBox)

        # Create a QGroupBox for Buttons
        self.buttons_groupBox = QtWidgets.QGroupBox("Save/Submit", self.centralwidget)
        self.buttons_groupBox.setObjectName("buttons_groupBox")

        # Create a QFormLayout for buttons
        self.buttons_formLayout = QtWidgets.QFormLayout(self.buttons_groupBox)
        self.buttons_formLayout.setObjectName("buttons_formLayout")

        # Save button
        self.save_button = QPushButton("Save", self.buttons_groupBox)
        self.save_button.setObjectName("save_button")
        self.buttons_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.save_button)

        # Load button
        self.load_button = QPushButton("Load", self.buttons_groupBox)
        self.save_button.setObjectName("Load_button")
        self.buttons_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.load_button)

        # submit button
        self.submit_button = QPushButton("Submit", self.buttons_groupBox)
        self.submit_button.setObjectName("submit_button")
        self.buttons_formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.submit_button)

        # Add the buttons group box to the horizontal layout
        self.horizontalLayout.addWidget(self.buttons_groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NG config app"))

        # Labels for Wi-Fi settings
        self.ssid_label.setText(_translate("MainWindow", "SSID:"))
        self.password_label.setText(_translate("MainWindow", "Password:"))

        # Labels for server settings
        self.mqtt_ip_label.setText(_translate("MainWindow", "MQTT IP:"))
        self.mqtt_username_label.setText(_translate("MainWindow", "MQTT Username:"))
        self.mqtt_password_label.setText(_translate("MainWindow", "MQTT Password:"))

        # Labels for lorawan settings
        self.lorawan_baud_rate_label.setText(_translate("MainWindow", "Baud Rate:"))
        self.lorawan_signal_bandwidth_label.setText(_translate("MainWindow", "Signal Bandwidth:"))
        self.lorawan_spreading_factor_label.setText(_translate("MainWindow", "Spreading Factor:"))
        self.lorawan_sync_word_label.setText(_translate("MainWindow", "Sync Word:"))
        self.lorawan_coding_rate4_label.setText(_translate("MainWindow", "Coding Rate 4:"))
        self.lorawan_tx_power_label.setText(_translate("MainWindow", "Tx Power:"))
        self.lorawan_gain_label.setText(_translate("MainWindow", "Gain:"))
        #self.com_port_status_label.setText(_translate("MainWindow", "click refresh to find available COM ports"))






