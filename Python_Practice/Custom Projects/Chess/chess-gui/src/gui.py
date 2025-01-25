import sys
import os
import pygame
from pygame.locals import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import chess
from stockfish import Stockfish

class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
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
        stockfish_path = "c:/Users/jeffr/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish chess engine/stockfish-windows-x86-64-avx2.exe"
        self.engine = Stockfish(path=stockfish_path)
        self.initUI()
        self.selected_square = None

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        self.buttons = {}

        for i in range(8):
            for j in range(8):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda _, x=i, y=j: self.on_button_clicked(x, y))
                self.grid_layout.addWidget(button, i, j)
                self.buttons[(i, j)] = button

        self.update_board()

    def on_button_clicked(self, x, y):
        square = chess.square(y, 7 - x)
        if self.selected_square is None:
            self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.update_board()
                if not self.board.is_game_over():
                    self.ai_move()
            self.selected_square = None

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