from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor

class GameOverDialog(QDialog):
    def __init__(self, title, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Over")
        self.setFixedSize(500, 300)
        self.setModal(True)  # Make dialog modal
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint)
        
        # Enhanced styling for different game over scenarios
        base_style = """
            QDialog {
                background-color: #1a1a1a;
            }
            QLabel {
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
        """
        
        # Add specific styling based on game outcome
        if "Checkmate" in title:
            title_color = "#ff3b30"  # Red for checkmate
        elif "Draw" in title or "Stalemate" in title:
            title_color = "#ffcc00"  # Yellow for draws
        else:
            title_color = "#34c759"  # Green for other cases
        
        self.setStyleSheet(base_style)
        
        layout = QVBoxLayout()
        
        # Title with specific styling
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            font-size: 48px;
            font-weight: bold;
            color: {title_color};
            padding: 25px;
            margin: 10px;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Message
        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(title_label)
        layout.addWidget(message_label)
        layout.addStretch()
        
        # Button container
        button_container = QWidget()
        button_layout = QVBoxLayout()
        
        # New Game button
        new_game_btn = QPushButton("New Game")
        new_game_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        new_game_btn.clicked.connect(lambda: self.make_choice("new_game"))
        
        # Return to Main Menu button
        menu_btn = QPushButton("Return to Main Menu")
        menu_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        menu_btn.clicked.connect(lambda: self.make_choice("menu"))
        
        button_layout.addWidget(new_game_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(menu_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        button_container.setLayout(button_layout)
        layout.addWidget(button_container)
        
        self.setLayout(layout)
    
    def make_choice(self, choice):
        """Store the user's choice and close dialog"""
        self.choice = choice
        self.accept()

    def closeEvent(self, event):
        """Prevent dialog from being closed except through buttons"""
        event.ignore()
