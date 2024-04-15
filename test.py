import sys
import time
import serial
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel

# Worker thread for background process
class Worker(QThread):
    resultReady = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, serial_port, connection_mode):
        super().__init__()
        self.serial_port = serial_port
        self.connection_mode = connection_mode
        self.is_running = True

    def run(self):
        while self.is_running:
            # Send the connection mode to the serial port
            self.serial_port.write(self.connection_mode.encode())

            # Wait for some time to receive the pin status
            time.sleep(2)

            # Receive and process the pin status from the serial port
            pin_status = self.serial_port.readline().decode().strip()

            if self.is_running:
                # Emit the pin status
                self.resultReady.emit(pin_status)

        self.finished.emit()

    def cancel(self):
        self.is_running = False

# Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a serial port
        self.serial_port = serial.Serial('COM6', 115200)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Serial Port Example')
        self.setGeometry(300, 300, 250, 150)

        # Button
        self.button = QPushButton('Stop', self)
        self.button.setGeometry(40, 50, 100, 30)
        self.button.clicked.connect(self.stopSending)

        # Label to display the pin status
        self.pinStatusLabel = QLabel(self)
        self.pinStatusLabel.setGeometry(40, 100, 210, 30)
        self.pinStatusLabel.setAlignment(Qt.AlignCenter)

        self.worker = None
        self.is_sending = False

    def startSending(self):
        self.button.setText('Stop')
        self.is_sending = True

        # Connection mode to be sent to the serial port
        connection_mode = 'PIN_STATUS'

        self.worker = Worker(self.serial_port, connection_mode)
        self.worker.resultReady.connect(self.displayPinStatus)
        self.worker.finished.connect(self.processFinished)
        self.worker.start()

    def stopSending(self):
        self.button.setEnabled(False)  # Disable the button during the stopping process

        if self.worker is not None and self.worker.isRunning():
            self.worker.cancel()
            self.worker.finished.connect(self.processStopped)

    def processStopped(self):
        self.button.setEnabled(True)  # Enable the button after the stopping process completes

        # Show a message box to indicate that the process has stopped
        QMessageBox.information(self, 'Process Stopped', 'Sending requests has been stopped.')

    def displayPinStatus(self, pin_status):
        # Display the pin status in the label
        self.pinStatusLabel.setText(f'Pin Status: {pin_status}')

    def processFinished(self):
        # Show a message box to indicate that the process has finished
        QMessageBox.information(self, 'Process Finished', 'Pin status received successfully.')

    def closeEvent(self, event):
        # Close the serial port when the application is closed
        self.serial_port.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
