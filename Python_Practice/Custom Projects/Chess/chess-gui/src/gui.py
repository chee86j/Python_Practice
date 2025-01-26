import sys
import os
import pygame
from pygame.locals import *
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGridLayout, QPushButton, 
                            QWidget, QMessageBox, QVBoxLayout, QDialog, QLabel)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
import chess
from stockfish import Stockfish

class GameOverDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Over")
        self.setFixedSize(400, 200)
        
        # Set window style
        self.setStyleSheet("""
            QDialog {
                background-color: #2C3E50;
            }
            QLabel {
                color: white;
                font-size: 24px;
                padding: 20px;
            }
            QPushButton {
                background-color: #27AE60;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #2ECC71;
            }
        """)

        layout = QVBoxLayout()
        
        # Message label
        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(message_label)
        
        # Restart button
        restart_button = QPushButton("Play Again")
        restart_button.clicked.connect(self.accept)
        layout.addWidget(restart_button, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)

class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Define color constants first
        self.LIGHT_SQUARE = "#F0D9B5"  # Light brown
        self.DARK_SQUARE = "#B58863"   # Dark brown
        self.SELECTED_COLOR = "#90EE90"  # Light green for selected piece
        self.POSSIBLE_MOVE_COLOR = "#32CD32"  # Green for possible moves
        
        # Track selected piece and possible moves
        self.selected_square = None
        self.possible_moves = set()
        
        # Remove pygame-related code
        self.SQUARE_SIZE = 80
        
        # Define the base path for piece images
        self.pieces_path = os.path.join(os.path.dirname(__file__), "assets", "pieces")
        
        # Load piece images
        self.pieces = {}
        for color in ['white', 'black']:
            for piece in ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']:
                image_path = os.path.join(self.pieces_path, f"{color}_{piece}.png")
                try:
                    # No need for pygame image loading
                    self.pieces[f"{color}_{piece}"] = image_path
                except Exception as e:
                    print(f"Error loading image {image_path}: {e}")

        self.setWindowTitle("Chess Game")
        self.setFixedSize(QSize(800, 800))
        self.board = chess.Board()
        
        # Initialize Stockfish
        try:
            stockfish_path = "c:/Users/jeffr/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe"
            if not os.path.exists(stockfish_path):
                raise FileNotFoundError(f"Stockfish not found at: {stockfish_path}")
            
            self.engine = Stockfish(path=stockfish_path)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to initialize Stockfish engine: {str(e)}\n"
                               "Please make sure Stockfish is installed in the correct location.")
            sys.exit(1)

        self.initUI()
        self.create_toolbar()

    def get_square_color(self, i, j):  # Fix indentation
        return self.LIGHT_SQUARE if (i + j) % 2 == 0 else self.DARK_SQUARE

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)  

        self.central_widget.setLayout(self.grid_layout)
        self.buttons = {}

        for i in range(8):
            for j in range(8):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                # Use class color constants
                color = self.get_square_color(i, j)
                button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color};
                        border: none;
                    }}
                    QPushButton:hover {{
                        background-color: #DAA520;  /* Golden color on hover */
                    }}
                """)
                button.clicked.connect(lambda _, x=i, y=j: self.on_button_clicked(x, y))
                self.grid_layout.addWidget(button, i, j)
                self.buttons[(i, j)] = button

        self.update_board()  # Move out of the loop

    def highlight_possible_moves(self, square):
        """Get all legal moves for the selected piece"""
        self.possible_moves = set()
        if square is not None:
            for move in self.board.legal_moves:
                if move.from_square == square:
                    self.possible_moves.add(move.to_square)


    def create_toolbar(self):
        toolbar = self.addToolBar("Game Controls")
        toolbar.setMovable(False)
        
        restart_action = QPushButton("Restart Game")
        restart_action.setStyleSheet("""
            QPushButton {
                background-color: #2980B9;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3498DB;
            }
        """)
        restart_action.clicked.connect(self.restart_game)
        toolbar.addWidget(restart_action)

    def restart_game(self):
        self.board = chess.Board()
        self.selected_square = None
        self.possible_moves.clear()  # Add this line
        self.update_board()

    def on_button_clicked(self, x, y):
        square = chess.square(y, 7 - x)
        
        if self.selected_square is None:
            # First click - select piece if it belongs to player
            piece = self.board.piece_at(square)
            if piece is not None and piece.color == self.board.turn:
                self.selected_square = square
                self.highlight_possible_moves(square)
                self.update_board()
        else:
            # Second click - try to make a move
            if square in self.possible_moves:
                move = chess.Move(self.selected_square, square)
                self.board.push(move)
                self.update_board()
                
                if self.board.is_game_over():
                    self.show_game_over_message()
                else:
                    self.ai_move()
                    if self.board.is_game_over():
                        self.show_game_over_message()
            
            # Reset selection and highlights
            self.selected_square = None
            self.possible_moves.clear()
            self.update_board()
    def ai_move(self):
        move = self.get_ai_move()
        if move:
            self.board.push(move)
            self.update_board()
            if self.board.is_game_over():
                self.show_game_over_message()

    def get_ai_move(self):
        """Get the best move from Stockfish"""
        try:
            self.engine.set_position([move.uci() for move in self.board.move_stack])
            best_move = self.engine.get_best_move()
            if best_move is None:
                raise Exception("Stockfish failed to return a move")
            return chess.Move.from_uci(best_move)
        except Exception as e:
            QMessageBox.warning(self, "AI Error", f"Error getting AI move: {str(e)}")
            return None

    def update_board(self):
        # Update the GUI to reflect the current board state
        for i in range(8):
            for j in range(8):
                button = self.buttons[(i, j)]
                square = chess.square(j, 7 - i)
                base_color = self.get_square_color(i, j)
                
                # Determine square color based on state
                if square == self.selected_square:
                    color = self.SELECTED_COLOR
                elif square in self.possible_moves:
                    color = self.POSSIBLE_MOVE_COLOR
                else:
                    color = base_color
                
                # Update button style
                button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color};
                        border: none;
                    }}
                    QPushButton:hover {{
                        background-color: #DAA520;
                    }}
                """)
                
                # Update piece icons
                piece = self.board.piece_at(chess.square(j, 7 - i))
                if piece:
                    # Map chess piece to filename
                    color = 'white' if piece.color else 'black'
                    piece_type = {
                        chess.PAWN: 'pawn',
                        chess.ROOK: 'rook',
                        chess.KNIGHT: 'knight',
                        chess.BISHOP: 'bishop',
                        chess.QUEEN: 'queen',
                        chess.KING: 'king'
                    }[piece.piece_type]
                    
                    piece_image = os.path.join(self.pieces_path, f"{color}_{piece_type}.png")
                    if os.path.exists(piece_image):
                        self.buttons[(i, j)].setIcon(QIcon(piece_image))
                        self.buttons[(i, j)].setIconSize(QSize(80, 80))
                    else:
                        print(f"Missing image: {piece_image}")
                else:
                    self.buttons[(i, j)].setIcon(QIcon())

    def show_game_over_message(self):
        """Show styled game over message with the result"""
        if self.board.is_checkmate():
            if self.board.turn:  # Black won (player lost)
                message = "Checkmate! You Lost!"
            else:  # White won (player won)
                message = "Checkmate! You Win!"
        elif self.board.is_stalemate():
            message = "Draw - Stalemate!"
        elif self.board.is_insufficient_material():
            message = "Draw - Insufficient Material!"
        
        dialog = GameOverDialog(message, self)
        if dialog.exec_() == QDialog.Accepted:
            self.restart_game()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessGUI()
    window.show()
    sys.exit(app.exec_())