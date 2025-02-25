from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
import json
import chess
from .replay_dialog import ReplayDialog

class StartMenu(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chess Game")
        self.setFixedSize(400, 400)  # Increased height for new button
        
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
        self.replay_button = QPushButton("Watch Replay")  # New button
        
        layout.addWidget(self.vs_ai_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.vs_player_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.replay_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.vs_ai_button.clicked.connect(self.choose_ai_game)
        self.vs_player_button.clicked.connect(self.choose_player_game)
        self.replay_button.clicked.connect(self.load_replay)  # New connection
        
        self.setLayout(layout)
        self.game_mode = None
        
    def choose_ai_game(self):
        self.game_mode = "AI"
        self.accept()
        
    def choose_player_game(self):
        self.game_mode = "Player"
        self.accept()
    
    def load_replay(self):
        """Load and watch a saved game replay"""
        try:
            # Get the file path using QFileDialog
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Load Game Replay",
                "",  # Default directory
                "Chess Files (*.chess)",  # File type filter
                options=QFileDialog.Option.DontUseNativeDialog
            )
            
            if file_path:
                # Read the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    game_data = json.load(file)
                
                # Create replay dialog with the moves
                moves = [chess.Move.from_uci(move) for move in game_data['moves']]
                if moves:
                    self.game_mode = "Replay"
                    replay_dialog = ReplayDialog(moves, self)
                    replay_dialog.exec()
                else:
                    QMessageBox.warning(
                        self,
                        "Empty Game",
                        "No moves found in the saved game file.",
                        QMessageBox.StandardButton.Ok
                    )
                    
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to load replay: {str(e)}",
                QMessageBox.StandardButton.Ok
            )
