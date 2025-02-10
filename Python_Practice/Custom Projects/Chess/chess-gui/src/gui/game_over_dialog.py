from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class GameOverDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Over")
        self.setFixedSize(400, 250)
        
        # Set window style
        self.setStyleSheet("""
            QDialog {
                background-color: #2C3E50;
            }
            QLabel {
                color: white;
                font-size: 28px;
                font-weight: bold;
                padding: 25px;
                margin: 10px;
            }
            QPushButton {
                background-color: #27AE60;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                min-width: 150px;
                margin: 20px;
            }
            QPushButton:hover {
                background-color: #2ECC71;
            }
            QPushButton:pressed {
                background-color: #219A52;
            }
        """)

        layout = QVBoxLayout()
        
        # Message label
        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message_label)
        
        # Restart button
        restart_button = QPushButton("Play Again")
        restart_button.clicked.connect(self.accept)
        layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)
