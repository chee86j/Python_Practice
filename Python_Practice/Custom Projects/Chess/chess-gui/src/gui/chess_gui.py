import os
import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QToolBar, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QListWidget, QMessageBox, QDialog, QFileDialog
from PyQt6.QtCore import QSize, Qt, QTimer, QTime
from PyQt6.QtGui import QIcon
import chess
from stockfish import Stockfish
from .game_over_dialog import GameOverDialog
from .start_menu import StartMenu  # Add this import
from collections import Counter

class ChessGUI(QMainWindow):
    def __init__(self, game_mode):
        super().__init__()
        self.game_mode = game_mode  # "AI" or "Player"
        
        # Define color constants first
        self.LIGHT_SQUARE = "#E8EDF9"    # Light blue-gray
        self.DARK_SQUARE = "#B7C0D8"     # Medium blue-gray
        self.SELECTED_COLOR = "#4A90E2"   # Bright blue
        self.POSSIBLE_MOVE_COLOR = "#32CD32"  # Green for possible moves
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
        self.pieces_path = os.path.join(os.path.dirname(__file__), "..", "assets", "pieces")
        
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
            "C:/Users/Admin/Downloads/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe",  # Windows
            "C:/Users/jeffr/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe",  # Windows
            "C:/Users/JChee/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe",  # Windows
            "/usr/local/bin/stockfish",  # macOS Homebrew
            "/usr/bin/stockfish",        # Linux
            "stockfish"  # System PATH
        ]

        self.engine = None
        for path in stockfish_paths:
            try:
                self.engine = Stockfish(path=path, depth=10)  # Add depth parameter
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

        # Remove AI difficulty feature
        self.move_history = []
        self.current_move_number = 1
        self.captured_pieces = {'white': Counter(), 'black': Counter()}
        self.white_captured = None
        self.black_captured = None
        
        # Initialize captured pieces tracking with all possible pieces
        piece_symbols = ['♟', '♞', '♝', '♜', '♛', '♚']
        self.captured_pieces = {
            'white': {symbol: 0 for symbol in piece_symbols},
            'black': {symbol: 0 for symbol in piece_symbols}
        }
        
        # Add piece symbols mapping
        self.piece_symbols = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',  # White pieces
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'   # Black pieces
        }
        
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
                        border: 2px solid #DAA520;
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
        self.update_board()  # Update the board to show possible moves


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
        
        # Add captured pieces display with styling
        captured_group = QGroupBox("Captured Pieces")
        captured_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin-top: 10px;
                padding: 5px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
            }
            QLabel {
                font-size: 16px;
                padding: 8px;
                margin: 4px;
                background-color: #f0f0f0;
                border-radius: 3px;
                min-height: 20px;
            }
        """)
        
        captured_layout = QVBoxLayout()
        self.white_captured = QLabel("White: ")
        self.black_captured = QLabel("Black: ")
        self.white_captured.setMinimumWidth(180)
        self.black_captured.setMinimumWidth(180)
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
        
        # Update move history styling to support Unicode symbols
        self.move_list.setStyleSheet("""
            QListWidget {
                font-size: 14px;
                font-family: Arial;
                padding: 5px;
            }
            QListWidget::item {
                padding: 3px;
            }
        """)

    def update_move_history(self, move):
        """Update move history display with conventional chess notation and Unicode symbols"""
        try:
            move_text = self.board.san(move)  # Get standard algebraic notation
            
            # Piece letters with Unicode symbols
            for piece_letter, symbol in self.piece_symbols.items():
                if piece_letter.isupper():  # Only replace uppercase pieces (white)
                    move_text = move_text.replace(piece_letter, symbol)
            
            # For white's move (even number of moves in history)
            if len(self.move_history) % 2 == 0:
                item_text = f"{self.current_move_number}. {move_text}"
                self.move_list.addItem(item_text)
            else:
                # For black's move, append to the current line
                current_item = self.move_list.item(self.move_list.count() - 1)
                current_text = current_item.text()
                current_item.setText(f"{current_text}  {move_text}")
                self.current_move_number += 1
            
            self.move_history.append(move_text)
            self.move_list.scrollToBottom()
        except Exception as e:
            print(f"Error updating move history: {e}")

    def update_captured_pieces(self, captured_piece):
        """Update captured pieces display"""
        if captured_piece:
            # Determine which side captured the piece
            capturing_color = 'white' if not captured_piece.color else 'black'
            
            # Map piece type to symbol
            piece_symbols = {
                chess.PAWN: '♟',
                chess.KNIGHT: '♞',
                chess.BISHOP: '♝',
                chess.ROOK: '♜',
                chess.QUEEN: '♛',
                chess.KING: '♚'
            }
            symbol = piece_symbols[captured_piece.piece_type]
            
            # Update counter
            self.captured_pieces[capturing_color][symbol] += 1
            
            # Update display for both sides
            for side in ['white', 'black']:
                # Sort pieces by value
                pieces_display = []
                for piece_symbol in ['♚', '♛', '♜', '♝', '♞', '♟']:
                    count = self.captured_pieces[side][piece_symbol]
                    if count > 0:
                        pieces_display.append(f"{piece_symbol}×{count}")
                
                # Join all pieces with spaces and update label
                pieces_str = " ".join(pieces_display)
                label = self.white_captured if side == 'white' else self.black_captured
                label.setText(f"{side.capitalize()}: {pieces_str}")

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
                
                # First update history (before making the move)
                self.update_move_history(move)
                
                # Check for capture before making move
                captured_piece = self.board.piece_at(square)
                
                # Make the move
                self.board.push(move)
                
                if captured_piece:
                    self.update_captured_pieces(captured_piece)
                
                self.move_stack.append(move)
                self.update_board()
                self.update_turn_indicator()
                
                # Handle game over and AI moves
                if self.board.is_game_over():
                    self.show_game_over_message()
                elif self.game_mode == "AI":
                    ai_move = self.get_ai_move()
                    if ai_move:
                        # Check for AI capture before making move
                        ai_captured = self.board.piece_at(ai_move.to_square)
                        self.board.push(ai_move)
                        self.move_stack.append(ai_move)
                        if ai_captured:
                            self.update_captured_pieces(ai_captured)
                
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

    def restart_game(self):
        """Restart the current game"""
        self.board = chess.Board()
        self.selected_square = None
        self.possible_moves.clear()
        self.captured_pieces = {'white': Counter(), 'black': Counter()}
        self.white_captured.setText("White: ")
        self.black_captured.setText("Black: ")
        self.move_history = []
        self.current_move_number = 1
        self.move_list.clear()
        self.update_board()
        self.update_turn_indicator()
        self.time = QTime(0, 0)  # Reset the timer
        self.start_timer()  # Restart the timer

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
        self.captured_pieces = {'white': Counter(), 'black': Counter()}
        self.white_captured.setText("White: ")
        self.black_captured.setText("Black: ")
        self.move_history = []
        self.current_move_number = 1
        self.move_list.clear()
        
        # If player chose black, make AI play first move as white
        if msg.clickedButton() == black_button:
            # Make AI play as white immediately
            self.ai_move()
        
        self.update_board()
        self.update_turn_indicator()
        self.time = QTime(0, 0)  # Reset the timer
        self.start_timer()  # Restart the timer

    def undo_move(self):
        """Undo the last move"""
        if len(self.board.move_stack) > 0:
            self.board.pop()
            if self.move_history:
                self.move_history.pop()
                # Remove or update the last move in the display
                if len(self.move_history) % 2 == 0:
                    self.move_list.takeItem(self.move_list.count() - 1)
                    self.current_move_number -= 1
                else:
                    # Update the last item to remove black's move
                    current_item = self.move_list.item(self.move_list.count() - 1)
                    move_num = len(self.move_history) // 2 + 1
                    white_move = self.move_history[-1]
                    current_item.setText(f"{move_num}. {white_move}")
            
            self.update_board()
            self.update_turn_indicator()

        if self.game_mode == "AI" and len(self.board.move_stack) > 0:
            # Undo AI's move as well
            self.board.pop()
            if self.move_history:
                self.move_history.pop()
                if len(self.move_history) % 2 == 0:
                    self.move_list.takeItem(self.move_list.count() - 1)
                    self.current_move_number -= 1
                else:
                    current_item = self.move_list.item(self.move_list.count() - 1)
                    move_num = len(self.move_history) // 2 + 1
                    white_move = self.move_history[-1]
                    current_item.setText(f"{move_num}. {white_move}")
            
            self.update_board()
            self.update_turn_indicator()

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

    def save_game(self):
        """Save the current game state to a file"""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Game", "", "Chess Files (*.chess);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.board.fen())

    def load_game(self):
        """Load a game state from a file"""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Game", "", "Chess Files (*.chess);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'r') as file:
                fen = file.read()
                self.board.set_fen(fen)
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

    def __del__(self):
        """Clean up Stockfish engine properly"""
        if hasattr(self, 'engine') and self.engine:
            try:
                self.engine.quit()
            except:
                pass
        super().__del__()  # Call parent's __del__ if it exists
