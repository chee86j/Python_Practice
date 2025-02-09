import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QPushButton, 
                            QWidget, QMessageBox, QVBoxLayout, QDialog, QLabel,
                            QToolBar, QHBoxLayout, QGroupBox, QListWidget, QFileDialog)
from PyQt6.QtCore import QSize, Qt, QTimer, QTime
from PyQt6.QtGui import QIcon
import chess
from stockfish import Stockfish

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
                transform: scale(1.05);
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
                transform: scale(1.05);
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

class ChessGUI(QMainWindow):
    def __init__(self, game_mode):
        super().__init__()
        self.game_mode = game_mode  # "AI" or "Player"
        
        # Define color constants first
        self.LIGHT_SQUARE = "#E8EDF9"    # Light blue-gray
        self.DARK_SQUARE = "#B7C0D8"     # Medium blue-gray
        self.SELECTED_COLOR = "#4A90E2"   # Bright blue
        self.POSSIBLE_MOVE_COLOR = "#81A1C1"  # Muted blue
        self.HOVER_COLOR = "#5E81AC"      # Dark blue
        
        # Add style constants
        self.BUTTON_STYLE = """
            QPushButton {
                background-color: #4C566A;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 5px 10px;
                font-size: 11px;
                font-weight: bold;
                min-width: 80px;
                margin: 2px;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #5E81AC;
            }
            QPushButton:pressed {
                background-color: #81A1C1;
            }
        """
        
        self.LABEL_STYLE = """
            QLabel {
                color: #2C3E50;
                font-size: 11px;
                font-weight: bold;
                padding: 4px 8px;
                background-color: #ECF0F1;
                border-radius: 3px;
                min-width: 100px;
                qproperty-alignment: AlignCenter;
            }
        """
        
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
        self.setFixedSize(QSize(800, 600))
        self.board = chess.Board()
        
        # Initialize Stockfish with multiple possible paths
        stockfish_paths = [
            "C:/Users/jeffr/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe",  # Windows
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
        self.status_label.setMinimumWidth(120)
        self.status_label.setMaximumWidth(120)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time = QTime(0, 0)
        self.timer_label = QLabel("Game Time: 00:00")
        self.timer_label.setMinimumWidth(100)
        self.timer_label.setMaximumWidth(100)
        
        self.move_stack = []  # Stack to keep track of moves for undo functionality

        # Add new features initialization
        self.difficulty_levels = {
            'Easy': 2,
            'Medium': 10,
            'Hard': 15
        }
        self.current_difficulty = 'Medium'
        self.move_history = []
        self.captured_pieces = {'white': [], 'black': []}
        
        self.initUI()
        self.create_toolbar()
        self.create_side_panel()
        self.update_turn_indicator()  # Initial update
        self.start_timer()  # Start the timer

    def start_timer(self):
        self.timer.start(1000)  # Update every second

    def update_timer(self):
        self.time = self.time.addSecs(1)
        self.timer_label.setText(f"Time: {self.time.toString('mm:ss')}")

    def stop_timer(self):
        self.timer.stop()

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
                button.setFixedSize(70, 70)
                color = self.get_square_color(i, j)
                button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color};
                        border: none;
                    }}
                    QPushButton:hover {{
                        background-color: {self.HOVER_COLOR};
                        border: 2px solid #FFF3;
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
        toolbar.setStyleSheet("""
            QToolBar {
                spacing: 5px;
                padding: 2px;
                background-color: #F5F5F5;
                border-bottom: 1px solid #DDD;
            }
        """)

        # Create widget to hold buttons and status
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(5)
        layout.setContentsMargins(5, 2, 5, 2)
        
        # Add Buttons with smaller spacing
        buttons = [
            ("New", self.new_game),
            ("Restart", self.restart_game),
            ("Menu", self.return_to_menu),
            ("Undo", self.undo_move)
        ]
        
        # Create button group
        button_widget = QWidget()
        button_layout = QHBoxLayout(button_widget)
        button_layout.setSpacing(2)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        for text, callback in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(self.BUTTON_STYLE)
            btn.clicked.connect(callback)
            button_layout.addWidget(btn)
        
        layout.addWidget(button_widget)
        
        # Add spacer
        layout.addSpacing(10)
        
        # Add status labels with fixed width
        status_widget = QWidget()
        status_layout = QHBoxLayout(status_widget)
        status_layout.setSpacing(5)
        status_layout.setContentsMargins(0, 0, 0, 0)
        
        self.status_label.setStyleSheet(self.LABEL_STYLE)
        self.timer_label.setStyleSheet(self.LABEL_STYLE)
        
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.timer_label)
        
        layout.addWidget(status_widget)
        layout.addStretch()
        
        widget.setLayout(layout)
        toolbar.addWidget(widget)

    def create_side_panel(self):
        """Create side panel for move history and captured pieces"""
        side_panel = QWidget()
        side_layout = QVBoxLayout()
        
        if self.game_mode == "AI":
            difficulty_group = QGroupBox("AI Difficulty")
            difficulty_layout = QHBoxLayout()
            for level in self.difficulty_levels.keys():
                btn = QPushButton(level)
                btn.setCheckable(True)
                btn.setChecked(level == self.current_difficulty)
                btn.clicked.connect(lambda checked, l=level: self.set_difficulty(l))
                difficulty_layout.addWidget(btn)
            difficulty_group.setLayout(difficulty_layout)
            side_layout.addWidget(difficulty_group)
        
        # Add captured pieces display
        captured_group = QGroupBox("Captured Pieces")
        captured_layout = QVBoxLayout()
        self.white_captured = QLabel("White: ")
        self.black_captured = QLabel("Black: ")
        captured_layout.addWidget(self.white_captured)
        captured_layout.addWidget(self.black_captured)
        captured_group.setLayout(captured_layout)
        side_layout.addWidget(captured_group)
        
        # Add move history
        history_group = QGroupBox("Move History")
        history_layout = QVBoxLayout()
        self.move_list = QListWidget()
        history_layout.addWidget(self.move_list)
        history_group.setLayout(history_layout)
        side_layout.addWidget(history_group)
        
        # Add save/load buttons
        save_load_layout = QHBoxLayout()
        save_btn = QPushButton("Save Game")
        load_btn = QPushButton("Load Game")
        save_btn.clicked.connect(self.save_game)
        load_btn.clicked.connect(self.load_game)
        save_load_layout.addWidget(save_btn)
        save_load_layout.addWidget(load_btn)
        side_layout.addLayout(save_load_layout)
        
        side_panel.setLayout(side_layout)
        side_panel.setFixedWidth(200)
        
        # Create main layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.central_widget)
        main_layout.addWidget(side_panel)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def set_difficulty(self, level):
        """Set AI difficulty level"""
        self.current_difficulty = level
        self.engine.set_skill_level(self.difficulty_levels[level])

    def update_move_history(self, move):
        """Update move history display"""
        move_text = self.board.san(move)
        turn = len(self.move_history) // 2 + 1
        if len(self.move_history) % 2 == 0:
            item_text = f"{turn}. {move_text}"
        else:
            item_text = f"    {move_text}"
        self.move_list.addItem(item_text)
        self.move_history.append(move_text)
        self.move_list.scrollToBottom()

    def update_captured_pieces(self, move):
        """Update captured pieces display"""
        captured_piece = self.board.piece_at(move.to_square)
        if captured_piece:
            color = 'white' if captured_piece.color == chess.WHITE else 'black'
            self.captured_pieces[color].append(captured_piece)
            self.update_captured_display()

    def on_button_clicked(self, i, j):
        square = chess.square(j, 7 - i)
        if self.selected_square is None:
            # First click - select a piece
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected_square = square
                self.highlight_possible_moves(square)
        else:
            # Second click - try to make a move
            if square in self.possible_moves:
                move = chess.Move(self.selected_square, square)
                self.board.push(move)
                self.move_stack.append(move)  # Track the move
                self.update_board()
                self.update_turn_indicator()
                
                if self.board.is_game_over():
                    self.show_game_over_message()
                elif self.game_mode == "AI":  # Only make AI move in AI mode
                    self.ai_move()
                    self.move_stack.append(move)  # Track the AI move
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
            self.move_stack.append(move)  # Track the AI move
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
                        self.buttons[(i, j)].setIconSize(QSize(60, 60))
                    else:
                        print(f"Missing image: {piece_image}")
                else:
                    self.buttons[(i, j)].setIcon(QIcon())

    def show_game_over_message(self):
        self.stop_timer()  # Stop the timer when the game is over
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