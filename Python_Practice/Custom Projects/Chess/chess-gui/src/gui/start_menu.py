from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class StartMenu(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chess Game")
        self.setFixedSize(400, 300)
        
        # Set window styling
        self.setStyleSheet("""
            QDialog {
                background-color: #2C3E50;
            }
            QLabel {
                color: white;
                font-size: 36px;
                font-weight: bold;
                padding: 20px;
                margin-bottom: 20px;
            }
            QPushButton {
                background-color: #27AE60;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                min-width: 200px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: #2ECC71;
            }
            QPushButton:pressed {
                background-color: #219A52;
            }
        """)

        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Chess Game")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Buttons
        self.vs_ai_button = QPushButton("Player vs AI")
        self.vs_player_button = QPushButton("Player vs Player")
        
        layout.addWidget(self.vs_ai_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.vs_player_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.vs_ai_button.clicked.connect(self.choose_ai_game)
        self.vs_player_button.clicked.connect(self.choose_player_game)
        
        self.setLayout(layout)
        self.game_mode = None
        
    def choose_ai_game(self):
        self.game_mode = "AI"
        self.accept()
        
    def choose_player_game(self):
        self.game_mode = "Player"
        self.accept()
