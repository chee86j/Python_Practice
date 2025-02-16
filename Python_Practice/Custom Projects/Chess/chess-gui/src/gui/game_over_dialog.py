from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor

class GameOverDialog(QDialog):
    def __init__(self, title, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Over")
        self.setFixedSize(500, 300)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)  # Keep dialog on top
        
        # Set window style
        self.setStyleSheet("""
            QDialog {
                background-color: #1a1a1a;
            }
            QLabel#title {
                color: #ff3b30;
                font-size: 48px;
                font-weight: bold;
                padding: 25px;
                margin: 10px;
            }
            QLabel#message {
                color: #ffffff;
                font-size: 28px;
                padding: 15px;
                margin: 10px;
            }
            QPushButton {
                background-color: #34c759;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 15px 30px;
                font-size: 20px;
                font-weight: bold;
                min-width: 200px;
                margin: 20px;
            }
            QPushButton:hover {
                background-color: #30d158;
                transform: scale(1.05);
            }
            QPushButton:pressed {
                background-color: #248a3d;
            }
        """)

        layout = QVBoxLayout()
        
        # Title label
        title_label = QLabel(title)
        title_label.setObjectName("title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Message label
        message_label = QLabel(message)
        message_label.setObjectName("message")
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(title_label)
        layout.addWidget(message_label)
        layout.addStretch()
        
        # Button container for centering
        button_container = QWidget()
        button_layout = QVBoxLayout()
        
        # Play Again button
        restart_button = QPushButton("Play Again")
        restart_button.setCursor(Qt.CursorShape.PointingHandCursor)
        restart_button.clicked.connect(self.accept)
        
        button_layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)
        button_container.setLayout(button_layout)
        layout.addWidget(button_container)
        
        self.setLayout(layout)
