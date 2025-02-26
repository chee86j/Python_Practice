from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
    QGridLayout, QWidget, QGroupBox, QListWidget
)
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QIcon
import chess
import os
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Style Constants
DIALOG_STYLE = """
    QDialog {
        background-color: #2C3E50;
    }
"""

LABEL_STYLE = """
    QLabel {
        color: white;
        font-size: 16px;
        padding: 10px;
    }
"""

BUTTON_STYLE = """
    QPushButton {
        background-color: #27AE60;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 10px 20px;
        font-size: 14px;
        min-width: 100px;
        margin: 5px;
    }
    QPushButton:hover {
        background-color: #2ECC71;
    }
    QPushButton:disabled {
        background-color: #95A5A6;
    }
"""

GROUPBOX_STYLE = """
    QGroupBox {
        color: white;
        font-size: 14px;
        border: 2px solid #34495E;
        border-radius: 5px;
        margin-top: 10px;
    }
"""

LISTWIDGET_STYLE = """
    QListWidget {
        background-color: #34495E;
        color: white;
        border: none;
        font-size: 14px;
    }
"""

class ReplayDialog(QDialog):
    def __init__(self, moves: List[chess.Move], parent: Optional[QWidget] = None):
        try:
            super().__init__(parent)
            logger.info('🎬 Initializing replay dialog')
            
            self.setWindowTitle("Game Replay")
            self.setFixedSize(1000, 800)
            
            self.moves = moves
            self.current_move = 0
            self.board = chess.Board()
            
            # Define color constants
            self.LIGHT_SQUARE = "#E8EDF9"    # Light blue-gray
            self.DARK_SQUARE = "#B7C0D8"     # Medium blue-gray
            self.SELECTED_COLOR = "#4A90E2"   # Bright blue
            self.SQUARE_SIZE = 65            # Exact ChessGUI square size
            
            # Define the base path for piece images
            self.pieces_path = os.path.join(os.path.dirname(__file__), "..", "assets", "pieces")
            
            # Load piece images
            self.pieces = {}
            for color in ['white', 'black']:
                for piece in ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']:
                    image_path = os.path.join(self.pieces_path, f"{color}_{piece}.png")
                    try:
                        self.pieces[f"{color}_{piece}"] = image_path
                    except Exception as e:
                        print(f"Error loading image {image_path}: {e}")
            
            # Define piece sizes for different piece types
            base_size = 50  # Base size for pieces
            self.PIECE_SIZES = {
                'pawn': base_size,
                'knight': int(base_size * 1.1),
                'bishop': int(base_size * 1.1),
                'rook': int(base_size * 1.05),
                'queen': int(base_size * 1.15),
                'king': int(base_size * 1.15)
            }
            
            # Apply consolidated styles
            self.setStyleSheet(DIALOG_STYLE + LABEL_STYLE + BUTTON_STYLE + GROUPBOX_STYLE + LISTWIDGET_STYLE)
            
            # Main layout
            layout = QHBoxLayout()
            layout.setSpacing(20)
            layout.setContentsMargins(20, 20, 20, 20)
            
            # Left side - Board and controls
            left_layout = QVBoxLayout()
            left_layout.setSpacing(10)
            
            # Empty Toolbar Space
            toolbar_space = QWidget()
            toolbar_space.setFixedHeight(40)
            left_layout.addWidget(toolbar_space)
            
            # Board Container
            board_container = QWidget()
            board_layout = QGridLayout()
            board_layout.setSpacing(0)  
            board_layout.setContentsMargins(0, 0, 0, 0)  
            board_container.setLayout(board_layout)
            board_container.setStyleSheet("""
                QWidget {
                    background-color: #2C3E50;
                    spacing: 0px;
                    padding: 0px;
                    margin: 0px;
                }
            """)
            
            # Create Chess Board Squares
            self.squares = []
            for i in range(8):
                row = []
                for j in range(8):
                    button = QPushButton()
                    button.setFixedSize(QSize(self.SQUARE_SIZE, self.SQUARE_SIZE))
                    button.setStyleSheet(self.get_square_style(i, j))
                    button.setContentsMargins(0, 0, 0, 0)
                    board_layout.addWidget(button, i, j)
                    row.append(button)
                self.squares.append(row)
            
            # Center the Board
            board_container.setFixedSize(self.SQUARE_SIZE * 8, self.SQUARE_SIZE * 8)
            left_layout.addWidget(board_container, alignment=Qt.AlignmentFlag.AlignCenter)
            
            # Control Buttons
            button_container = QWidget()
            button_layout = QHBoxLayout(button_container)
            button_layout.setSpacing(10)
            
            # Move Counter
            self.move_label = QLabel(f"Move: {self.current_move}/{len(self.moves)}")
            self.move_label.setStyleSheet("""
                QLabel {
                    color: white;
                    font-size: 14px;
                    padding: 5px;
                }
            """)
            button_layout.addWidget(self.move_label)
            
            # Control buttons with exact sizing
            self.prev_button = QPushButton("◀")  # Previous
            self.play_button = QPushButton("▶")  # Play
            self.pause_button = QPushButton("⏸")  # Pause
            self.next_button = QPushButton("▶▶")  # Next
            self.menu_button = QPushButton("Back to Menu")  # Menu
            
            # Style the playback control buttons
            for button in [self.prev_button, self.play_button, self.pause_button, self.next_button]:
                button.setFixedSize(40, 30)
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #27AE60;
                        color: white;
                        border: none;
                        border-radius: 4px;
                        font-size: 16px;
                        padding: 0px;
                    }
                    QPushButton:hover {
                        background-color: #2ECC71;
                    }
                    QPushButton:disabled {
                        background-color: #95A5A6;
                    }
                """)
            
            # Style the menu button differently
            self.menu_button.setFixedSize(120, 30)
            self.menu_button.setStyleSheet("""
                QPushButton {
                    background-color: #E74C3C;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    font-size: 14px;
                    padding: 0px;
                }
                QPushButton:hover {
                    background-color: #C0392B;
                }
            """)
            
            button_layout.addStretch()
            button_layout.addWidget(self.prev_button)
            button_layout.addWidget(self.play_button)
            button_layout.addWidget(self.pause_button)
            button_layout.addWidget(self.next_button)
            button_layout.addWidget(self.menu_button)
            button_layout.addStretch()
            
            left_layout.addWidget(button_container)
            
            # Right side - Move History
            right_layout = QVBoxLayout()
            right_layout.setSpacing(10)
            
            # Move History group
            move_history_group = QGroupBox("Move History")
            move_history_layout = QVBoxLayout()
            move_history_layout.setContentsMargins(10, 15, 10, 10)
            
            self.move_list = QListWidget()
            move_history_layout.addWidget(self.move_list)
            
            move_history_group.setLayout(move_history_layout)
            right_layout.addWidget(move_history_group)
            
            # Add Layouts
            layout.addLayout(left_layout, stretch=2)
            layout.addLayout(right_layout, stretch=1)
            
            self.setLayout(layout)
            
            # Setup controls
            self.timer = QTimer()
            self.timer.timeout.connect(self.next_move)
            self.is_playing = False
            
            # Connect buttons
            self.prev_button.clicked.connect(self.previous_move)
            self.play_button.clicked.connect(self.start_play)
            self.pause_button.clicked.connect(self.stop_play)
            self.next_button.clicked.connect(self.next_move)
            self.menu_button.clicked.connect(self.return_to_menu)  
            
            # Initialize
            self.pause_button.hide()  # Start with pause hidden
            self.update_display()
            self.update_move_list()
            logger.info('✅ Replay dialog initialized successfully')
            
        except Exception as e:
            logger.error(f'❌ Error initializing replay dialog: {e}')
            raise
    
    def get_square_style(self, i, j):
        """Get the style for a chess square"""
        is_light = (i + j) % 2 == 0
        bg_color = self.LIGHT_SQUARE if is_light else self.DARK_SQUARE
        return f"""
            QPushButton {{
                background-color: {bg_color};
                border: none;
                text-align: left;
                padding-left: 7px;  /* Add left padding to shift pieces */
                border-radius: 0px; 
            }}
            QPushButton:pressed {{
                background-color: {bg_color};
            }}
        """
    
    def update_display(self):
        """Update the display with current board position"""
        try:
            logger.debug(f'Updating display for move {self.current_move}')
            self.move_label.setText(f"Move: {self.current_move}/{len(self.moves)}")
            
            # Update board squares
            for i in range(8):
                for j in range(8):
                    square = chess.square(j, 7 - i)
                    piece = self.board.piece_at(square)
                    button = self.squares[i][j]
                    
                    if piece:
                        color = 'white' if piece.color else 'black'
                        piece_type = {
                            chess.PAWN: 'pawn',
                            chess.ROOK: 'rook',
                            chess.KNIGHT: 'knight',
                            chess.BISHOP: 'bishop',
                            chess.QUEEN: 'queen',
                            chess.KING: 'king'
                        }[piece.piece_type]
                        
                        image_path = os.path.join(self.pieces_path, f"{color}_{piece_type}.png")
                        if os.path.exists(image_path):
                            button.setIcon(QIcon(image_path))
                            size = self.PIECE_SIZES[piece_type]
                            button.setIconSize(QSize(size, size))
                            button.setStyleSheet(button.styleSheet() + """
                                QPushButton {
                                    text-align: left;
                                    padding-left: 7px;
                                }
                            """)
                        else:
                            print(f"Missing image: {image_path}")
                    else:
                        button.setIcon(QIcon())
                        button.setIconSize(QSize(self.SQUARE_SIZE, self.SQUARE_SIZE))
            
            # Update button states
            self.prev_button.setEnabled(self.current_move > 0)
            self.next_button.setEnabled(self.current_move < len(self.moves))
            
        except Exception as e:
            logger.error(f'❌ Error updating display: {e}')
            self.stop_play()
    
    def update_move_list(self):
        """Update the move list with current move highlighted"""
        try:
            logger.debug('Updating move list')
            self.move_list.clear()
            temp_board = chess.Board()
            
            for i, move in enumerate(self.moves[:self.current_move]):
                move_text = temp_board.san(move)
                if i % 2 == 0:
                    item_text = f"{(i//2)+1}. {move_text}"
                    self.move_list.addItem(item_text)
                else:
                    prev_item = self.move_list.item(self.move_list.count()-1)
                    if prev_item:
                        current_text = prev_item.text()
                        prev_item.setText(f"{current_text} {move_text}")
                temp_board.push(move)
            
            # Scroll to the current move
            if self.move_list.count() > 0:
                self.move_list.scrollToItem(self.move_list.item(self.move_list.count()-1))
                
        except Exception as e:
            logger.error(f'❌ Error updating move list: {e}')
    
    def previous_move(self):
        """Go to previous move"""
        try:
            logger.debug('Moving to previous move')
            if self.current_move > 0:
                self.board.pop()
                self.current_move -= 1
                self.update_display()
                self.update_move_list()
                
                # Re-enable next button if we're not at the end
                if self.current_move < len(self.moves):
                    self.next_button.setEnabled(True)
                
                # Disable prev button if we reach the start
                if self.current_move == 0:
                    self.prev_button.setEnabled(False)
        except Exception as e:
            logger.error(f'❌ Error in previous move: {e}')
            self.stop_play()
    
    def next_move(self):
        """Go to next move"""
        try:
            logger.debug('Moving to next move')
            if self.current_move < len(self.moves):
                move = self.moves[self.current_move]
                if move in self.board.legal_moves:
                    self.board.push(move)
                    self.current_move += 1
                    self.update_display()
                    self.update_move_list()
                    
                    # Stop playing if we reach the end
                    if self.current_move >= len(self.moves):
                        self.stop_play()
                        self.next_button.setEnabled(False)
            else:
                self.stop_play()
                self.next_button.setEnabled(False)
        except Exception as e:
            logger.error(f'❌ Error in next move: {e}')
            self.stop_play()
    
    def start_play(self):
        """Start auto-play"""
        try:
            logger.info('▶️ Starting auto-play')
            self.is_playing = True
            self.play_button.hide()
            self.pause_button.show()
            self.timer.start(1500)  # 1.5 second between moves
            
        except Exception as e:
            logger.error(f'❌ Error starting play: {e}')
    
    def stop_play(self):
        """Stop auto-play"""
        try:
            logger.info('⏸️ Stopping auto-play')
            self.is_playing = False
            self.pause_button.hide()
            self.play_button.show()
            self.timer.stop()
            
        except Exception as e:
            logger.error(f'❌ Error stopping play: {e}')
    
    def return_to_menu(self):
        """Close the replay dialog and return to start menu"""
        try:
            logger.info('🔙 Returning to menu')
            self.stop_play()
            self.accept()
            
        except Exception as e:
            logger.error(f'❌ Error returning to menu: {e}')
            self.close()