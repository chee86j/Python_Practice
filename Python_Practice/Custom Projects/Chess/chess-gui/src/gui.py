import sys
import os
import pygame
from pygame.locals import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QMessageBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import chess
from stockfish import Stockfish

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
        
        # Initialize pygame and other attributes
        pygame.init()
        self.SQUARE_SIZE = 80
        self.BOARD_SIZE = self.SQUARE_SIZE * 8
        self.screen = pygame.display.set_mode((self.BOARD_SIZE, self.BOARD_SIZE))
        pygame.display.set_caption("Chess Game") 
        
        # Define the base path for piece images
        self.pieces_path = os.path.join(os.path.dirname(__file__), "assets", "pieces")
        
        # Load piece images
        self.pieces = {}
        for color in ['white', 'black']:
            for piece in ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']:
                image_path = os.path.join(self.pieces_path, f"{color}_{piece}.png")
                try:
                    image = pygame.image.load(image_path)
                    image = pygame.transform.scale(image, (self.SQUARE_SIZE, self.SQUARE_SIZE))
                    self.pieces[f"{color}_{piece}"] = image
                except pygame.error as e:
                    print(f"Error loading image {image_path}: {e}")

        self.setWindowTitle("Chess Game")
        self.setFixedSize(QSize(800, 800))
        self.board = chess.Board()
        stockfish_path = "c:/Users/jeffr/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe"
        self.engine = Stockfish(path=stockfish_path)
        self.initUI()

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

        self.update_board()

    def get_square_color(self, i, j):
        return self.LIGHT_SQUARE if (i + j) % 2 == 0 else self.DARK_SQUARE

    def highlight_possible_moves(self, square):
        """Get all legal moves for the selected piece"""
        self.possible_moves = set()
        if square is not None:
            for move in self.board.legal_moves:
                if move.from_square == square:
                    self.possible_moves.add(move.to_square)

    def show_game_over_message(self):
        """Show game over message with the result"""
        msg = QMessageBox()
        msg.setWindowTitle("Game Over")
        
        if self.board.is_checkmate():
            if self.board.turn:  # Black won (player lost)
                msg.setText("You Lost!")
                msg.setIcon(QMessageBox.Critical)
            else:  # White won (player won)
                msg.setText("You Win!")
                msg.setIcon(QMessageBox.Information)
        elif self.board.is_stalemate():
            msg.setText("Draw - Stalemate!")
            msg.setIcon(QMessageBox.Information)
        elif self.board.is_insufficient_material():
            msg.setText("Draw - Insufficient Material!")
            msg.setIcon(QMessageBox.Information)
        
        msg.exec_()

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

    def get_ai_move(self):
        """Get the best move from Stockfish"""
        self.engine.set_position([move.uci() for move in self.board.move_stack])
        best_move = self.engine.get_best_move()
        return chess.Move.from_uci(best_move)

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
                piece = self.board.piece_at(square)
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
                    
                    piece_image = os.path.join(self.pieces_path, f"{color}_{piece_type}.png")
                    if os.path.exists(piece_image):
                        button.setIcon(QIcon(piece_image))
                        button.setIconSize(QSize(80, 80))
                else:
                    button.setIcon(QIcon())

    def draw_pieces(self, board):
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece != '--':
                    piece_color = 'white' if piece[0] == 'w' else 'black'
                    piece_type = self.get_piece_type(piece[1])
                    piece_key = f"{piece_color}_{piece_type}"
                    if piece_key in self.pieces:
                        piece_rect = self.pieces[piece_key].get_rect()
                        piece_rect.center = (col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2,
                                          row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2)
                        self.screen.blit(self.pieces[piece_key], piece_rect)

    def get_piece_type(self, symbol):
        mapping = {
            'P': 'pawn',
            'R': 'rook',
            'N': 'knight',
            'B': 'bishop',
            'Q': 'queen',
            'K': 'king'
        }
        return mapping.get(symbol, 'pawn')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessGUI()
    window.show()
    sys.exit(app.exec_())