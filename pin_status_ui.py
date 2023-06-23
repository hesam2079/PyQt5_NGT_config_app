from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor

class pin_status_ui(QWidget):
    def __init__(self):
        super().__init__()

        self.pin_labels = {}
        self.pin_status_labels = {}

        layout = QVBoxLayout()
        self.setLayout(layout)

    def update_pins(self, pin_data):
        layout = self.layout()
        if layout is not None:
            # Clear the existing layout
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                layout.removeItem(item)

        # Create new labels based on pin data
        for pin, status in pin_data.items():
            pin_label = QLabel(f"{pin}")
            pin_status_label = QLabel(status)

            # Apply custom styles to status labels
            color = None
            if status == "HIGH":
                color = "green"
            elif status == "LOW":
                color = "red"
            else:
                # Customize the color for float status
                color = "orange"

            pin_status_label.setStyleSheet("QLabel { background-color: %s; color: white; padding: 5px; }" % color)

            # Store the labels for later access
            self.pin_labels[pin] = pin_label
            self.pin_status_labels[pin] = pin_status_label

            # Add the labels to the layout
            pin_layout = QHBoxLayout()
            pin_layout.addWidget(pin_label)
            pin_layout.addWidget(pin_status_label)
            layout.addLayout(pin_layout)

        layout.addStretch()
