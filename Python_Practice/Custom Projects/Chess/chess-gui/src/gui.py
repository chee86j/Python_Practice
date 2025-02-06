import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QPushButton, 
                            QWidget, QMessageBox, QVBoxLayout, QDialog, QLabel,
                            QToolBar, QHBoxLayout)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
import chess
from stockfish import Stockfish

class StartMenu(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chess Game")
        self.setFixedSize(400, 300)
        
        # Set window style
        self.setStyleSheet("""
            QDialog {
                background-color: #2C3E50;
            }
            QLabel {
                color: white;
                font-size: 32px;
                padding: 20px;
            }
            QPushButton {
                background-color: #27AE60;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 18px;
                min-width: 200px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: #2ECC71;
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
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message_label)
        
        # Restart button
        restart_button = QPushButton("Play Again")
        restart_button.clicked.connect(self.accept)
        layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)

class ChessGUI(QMainWindow):
    def __init__(self, game_mode):
        super().__init__()
        self.game_mode = game_mode  # "AI" or "Player"
        
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
        
        # Initialize Stockfish with multiple possible paths
        stockfish_paths = [
            "C:/Users/JChee/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe",  # Windows
            "/usr/local/bin/stockfish",  # macOS Homebrew
            "/usr/bin/stockfish",        # Linux
            "stockfish"  # System PATH
        ]

        self.engine = None
        for path in stockfish_paths:
            try:
                self.engine = Stockfish(path=path)
                break
            except Exception:
                continue

        if self.engine is None:
            QMessageBox.critical(
                self, 
                "Stockfish Not Found",
                "Could not find Stockfish chess engine. Please:\n\n"
                "1. Install Stockfish:\n"
                "   - Windows: Download from https://stockfishchess.org/\n"
                "   - macOS: brew install stockfish\n"
                "   - Linux: sudo apt install stockfish\n\n"
                "2. Ensure it's in one of these locations:\n"
                f"{chr(10).join(stockfish_paths)}"
            )
            sys.exit(1)

        # Add status label for turn indicator with dynamic styling
        self.status_label = QLabel("Current Turn: White")
        self.status_label.setMinimumWidth(200)  # Ensure consistent width
        # Initial styling will be set by update_turn_indicator
        
        self.initUI()
        self.create_toolbar()
        self.update_turn_indicator()  # Initial update

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
        toolbar = QToolBar("Game Controls", self)
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        # Create widget to hold buttons and status
        widget = QWidget()
        layout = QHBoxLayout(widget)
        
        # Add buttons
        restart_action = QPushButton("Restart Game")
        new_game_action = QPushButton("New Game")
        menu_action = QPushButton("Return to Menu")  # New button
        
        button_style = """
            QPushButton {
                background-color: #2980B9;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 14px;
                margin-right: 10px;
            }
            QPushButton:hover {
                background-color: #3498DB;
            }
        """
        
        restart_action.setStyleSheet(button_style)
        new_game_action.setStyleSheet(button_style)
        menu_action.setStyleSheet(button_style)
        
        restart_action.clicked.connect(self.restart_game)
        new_game_action.clicked.connect(self.new_game)
        menu_action.clicked.connect(self.return_to_menu)  # New connection
        
        layout.addWidget(new_game_action)
        layout.addWidget(restart_action)
        layout.addWidget(menu_action)  # Add new button
        layout.addWidget(self.status_label)
        layout.addStretch()
        
        widget.setLayout(layout)
        toolbar.addWidget(widget)

    def return_to_menu(self):
        """Return to the start menu"""
        self.close()  # Close current window
        self.show_start_menu()  # Show new menu

    def show_start_menu(self):
        """Show the start menu and create new game based on selection"""
        start_menu = StartMenu()
        if start_menu.exec() == QDialog.DialogCode.Accepted:
            new_window = ChessGUI(start_menu.game_mode)
            new_window.show()

    def new_game(self):
        """Start a completely new game with user choice of color"""
        msg = QMessageBox()
        msg.setWindowTitle("New Game")
        msg.setText("Choose your color:")
        white_button = msg.addButton("White", QMessageBox.ButtonRole.AcceptRole)
        black_button = msg.addButton("Black", QMessageBox.ButtonRole.RejectRole)
        
        msg.exec()
        
        self.board = chess.Board()
        self.selected_square = None
        self.possible_moves.clear()
        
        # If player chose black, make AI play first move as white
        if msg.clickedButton() == black_button:
            # Make AI play as white immediately
            self.ai_move()
        
        self.update_board()
        self.update_turn_indicator()

    def update_turn_indicator(self):
        """Update the status label to show current turn with dynamic styling"""
        current_turn = "White" if self.board.turn else "Black"
        self.status_label.setText(f"Current Turn: {current_turn}")
        
        # Set background and text color based on current turn
        if self.board.turn:  # White's turn
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #2C3E50;
                    color: white;
                    font-size: 16px;
                    font-weight: bold;
                    padding: 5px 15px;
                    border-radius: 5px;
                }
            """)
        else:  # Black's turn
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #ECF0F1;
                    color: #2C3E50;
                    font-size: 16px;
                    font-weight: bold;
                    padding: 5px 15px;
                    border-radius: 5px;
                }
            """)

    def restart_game(self):
        self.board = chess.Board()
        self.selected_square = None
        self.possible_moves.clear()  # Add this line
        self.update_board()
        self.update_turn_indicator()  # Add this line

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
                self.update_turn_indicator()
                
                if self.board.is_game_over():
                    self.show_game_over_message()
                elif self.game_mode == "AI":  # Only make AI move in AI mode
                    self.ai_move()
                    self.update_turn_indicator()
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
            self.update_turn_indicator()  # Add this line
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
        if dialog.exec() == QDialog.Accepted:
            self.restart_game()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    def show_start_menu():
        start_menu = StartMenu()
        if start_menu.exec() == QDialog.DialogCode.Accepted:
            window = ChessGUI(start_menu.game_mode)
            window.show()
    
    show_start_menu()
    sys.exit(app.exec())