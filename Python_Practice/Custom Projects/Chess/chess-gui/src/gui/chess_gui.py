import os
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QGridLayout, QPushButton, QToolBar, 
    QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QListWidget, 
    QMessageBox, QDialog, QFileDialog
)
from PyQt6.QtCore import QSize, Qt, QTimer, QTime
from PyQt6.QtGui import QIcon
import chess
from stockfish import Stockfish
from .game_over_dialog import GameOverDialog
from .start_menu import StartMenu  # Add this import
from collections import Counter
import logging
import platform
from pathlib import Path
import json
from .replay_dialog import ReplayDialog

# Enhance logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('chess_gui.log')
    ]
)
logger = logging.getLogger(__name__)

class ChessError(Exception):
    """Base exception class for chess-related errors"""
    pass

class StockfishError(ChessError):
    """Exception for Stockfish engine errors"""
    pass

class GameStateError(ChessError):
    """Exception for invalid game state errors"""
    pass

class ChessGUI(QMainWindow):
    def __init__(self, game_mode):
        try:
            super().__init__()
            logger.info(f"🎮 Initializing ChessGUI with game mode: {game_mode}")
            
            # Validate game mode
            if game_mode not in ["Player", "AI"]:
                raise ValueError(f"❌ Invalid game mode: {game_mode}")
            
            self.game_mode = game_mode
            
            # Initialize board first
            self.board = chess.Board()
            
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
            self.setFixedSize(QSize(1000, 600)) 
            
            # Initialize Stockfish with multiple possible paths
            stockfish_paths = [
                "C:/Users/Admin/Downloads/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe",  # Windows
                "C:/Users/jeffr/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe",  # Windows
                "C:/Users/JChee/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/stockfish/stockfish-windows-x86-64-avx2.exe",  # Windows
                "/usr/local/bin/stockfish",  # macOS Homebrew
                "/usr/bin/stockfish",        # Linux
                "stockfish"  # System PATH
            ]

            try:
                if hasattr(self, 'engine') and self.engine:
                    self.engine.quit()
            except:
                pass
            
            self.engine = None
            for path in stockfish_paths:
                try:
                    self.engine = Stockfish(path=path)
                    # Test if engine is working
                    self.engine.get_board_visual()
                    print(f"✅ SUCCESSFULLY Initialized Stockfish at: {path} ✅")
                    break
                except:
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
            
            # Add piece size constants based on classical Staunton Design proportions
            base_size = 35  # Base size for pawn
            self.PIECE_SIZES = {
                'pawn': base_size,
                'rook': int(base_size * 1.05),
                'knight': int(base_size * 1.3),
                'bishop': int(base_size * 1.55),
                'queen': int(base_size * 1.8),
                'king': int(base_size * 2.05)
            }
            
            self.initUI()
            self.create_toolbar()
            self.create_side_panel()
            self.update_turn_indicator()  # Initial update
            self.start_timer()  # Start the timer

            logger.info('✅ Chess GUI initialized successfully')

        except Exception as e:
            logger.error(f'❌ Error initializing ChessGUI: {e}', exc_info=True)
            QMessageBox.critical(self, "Initialization Error", 
                               f"Failed to start the game: {str(e)}\n\nPlease check the logs for details.")
            raise

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
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        
        self.central_widget.setLayout(self.grid_layout)
        self.buttons = {}

        for i in range(8):
            for j in range(8):
                button = QPushButton("")
                button.setFixedSize(72, 72)
                color = self.get_square_color(i, j)
                button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color};
                        border: none;
                        margin: 0;
                        padding: 0;
                        border-radius: 0;
                    }}
                    QPushButton:hover {{
                        background-color: {self.HOVER_COLOR};
                    }}
                """)
                button.clicked.connect(lambda _, x=i, y=j: self.on_button_clicked(x, y))
                self.grid_layout.addWidget(button, i, j)
                self.buttons[(i, j)] = button

        self.update_board()  # Move out of the loop

    def highlight_possible_moves(self, square):
        """Get all legal moves for the selected piece with validation"""
        self.possible_moves = set()
        if square is not None:
            for move in self.board.legal_moves:
                if move.from_square == square:
                    self.possible_moves.add(move.to_square)
        self.update_board()

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
        
        # Captured pieces styling
        captured_group = QGroupBox("Captured Pieces")
        captured_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #34495e;
                border-radius: 8px;
                margin-top: 12px;
                padding: 15px;
                background-color: #f8f9fa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 10px;
                color: #2C3E50;
                font-size: 14px;
                background-color: #f8f9fa;
            }
            QLabel {
                font-size: 16px;
                padding: 12px 15px;
                margin: 6px;
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                min-height: 30px;
                color: #2C3E50;
                font-weight: bold;
            }
        """)
        
        captured_layout = QVBoxLayout()
        self.white_captured = QLabel("White: ")
        self.black_captured = QLabel("Black: ")
        self.white_captured.setMinimumWidth(400)  
        self.black_captured.setMinimumWidth(400) 
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
        side_panel.setFixedWidth(425)  
        
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
                font-size: 16px;
                font-family: Arial;
                padding: 8px;
            }
            QListWidget::item {
                padding: 5px;
                margin: 2px;
            }
        """)

    def update_move_history(self, move):
        """Update move history display with proper error handling"""
        try:
            if move in self.board.legal_moves:
                move_text = self.board.san(move)  # Get standard algebraic notation
                
                # Replace piece letters with Unicode symbols
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
                    if current_item:
                        current_text = current_item.text()
                        current_item.setText(f"{current_text}  {move_text}")
                        self.current_move_number += 1
                
                self.move_history.append(move_text)
                self.move_list.scrollToBottom()
        except Exception as e:
            logger.error(f"Error updating move history: {e}")
            raise

    def update_captured_pieces(self, captured_piece):
        """Update captured pieces display"""
        if captured_piece:
            # Get the color of the captured piece and update the opposite side's captures
            if captured_piece.color:  # If the captured piece is white
                capturing_side = 'black'
            else:  # If the captured piece is black
                capturing_side = 'white'
            
            # Get the symbol for the captured piece
            piece_symbols = {
                chess.PAWN: '♟',
                chess.KNIGHT: '♞',
                chess.BISHOP: '♝',
                chess.ROOK: '♜',
                chess.QUEEN: '♛',
                chess.KING: '♚'
            }
            captured_symbol = piece_symbols[captured_piece.piece_type]
            
            # Update the capturing side's counter
            self.captured_pieces[capturing_side][captured_symbol] += 1
            
            # Format and display white's captures
            white_captures = []
            for symbol in ['♚', '♛', '♜', '♝', '♞', '♟']:
                count = self.captured_pieces['white'][symbol]
                if count > 0:
                    white_captures.append(f"{symbol}×{count}")
            self.white_captured.setText(f"⚪ White Captures: {' '.join(white_captures)}")
            
            # Format and display black's captures
            black_captures = []
            for symbol in ['♚', '♛', '♜', '♝', '♞', '♟']:
                count = self.captured_pieces['black'][symbol]
                if count > 0:
                    black_captures.append(f"{symbol}×{count}")
            self.black_captured.setText(f"⚫ Black Captures: {' '.join(black_captures)}")

    def on_button_clicked(self, i, j):
        """Handle chess piece movement with proper validation"""
        try:
            square = chess.square(j, 7 - i)
            
            if self.selected_square is None:
                # First click - select a piece
                piece = self.board.piece_at(square)
                if piece and piece.color == self.board.turn:
                    self.selected_square = square
                    self.highlight_possible_moves(square)
            else:
                # Second click - try to make a move
                move = chess.Move(self.selected_square, square)
                
                # Validate move before attempting to make it
                if move in self.board.legal_moves:
                    # Get capture info before making move
                    captured_piece = self.board.piece_at(square)
                    
                    # Update move history before making the move
                    try:
                        self.update_move_history(move)
                    except Exception as e:
                        logger.error(f"Error updating move history: {e}")
                    
                    # Make the move
                    self.board.push(move)
                    self.move_stack.append(move)
                    
                    # Update captured pieces if any
                    if captured_piece:
                        self.update_captured_pieces(captured_piece)
                    
                    self.update_board()
                    self.update_turn_indicator()
                    
                    # Handle game over and AI moves
                    if self.board.is_game_over():
                        self.show_game_over_message()
                    elif self.game_mode == "AI" and not self.board.is_game_over():
                        # AI's turn
                        self.make_ai_move()
                
                # Reset selection and highlights
                self.selected_square = None
                self.possible_moves.clear()
                self.update_board()
            
        except Exception as e:
            logger.error(f"Error in on_button_clicked: {e}")
            self.selected_square = None
            self.possible_moves.clear()
            self.update_board()

    def make_ai_move(self):
        """Handle AI move with enhanced error handling"""
        try:
            if not self.engine:
                raise StockfishError("❌ Stockfish engine not initialized")
                
            logger.debug("🤖 Starting AI move calculation")
            ai_move = self.get_ai_move()
            
            if not ai_move:
                raise GameStateError("⚠️ AI failed to produce a valid move")
            
            if ai_move not in self.board.legal_moves:
                raise GameStateError(f"❌ AI produced illegal move: {ai_move}")
            
            self._execute_move(ai_move)
            logger.info(f"✅ AI made move: {ai_move}")
            
        except (StockfishError, GameStateError) as e:
            logger.error(str(e))
            self.show_error_dialog("AI Error", str(e))
        except Exception as e:
            logger.error(f"❌ Unexpected error in AI move: {e}", exc_info=True)
            self.show_error_dialog("AI Error", f"Unexpected error: {str(e)}")

    def _execute_move(self, move):
        """Execute a move with proper validation and error handling"""
        try:
            if not self.board.is_legal(move):
                raise GameStateError(f"❌ Illegal move attempted: {move}")
            
            # Get capture info before making move
            captured = self.board.piece_at(move.to_square)
            
            # Make the move
            self.board.push(move)
            self.move_stack.append(move)
            
            # Update move history
            self.update_move_history(move)
            
            # Handle capture if any
            if captured:
                logger.debug(f"👊 Piece captured: {captured}")
                self.update_captured_pieces(captured)
            
            self.update_board()
            self.update_turn_indicator()
            self.check_game_state()
            
        except GameStateError as e:
            logger.error(str(e))
            raise
        except Exception as e:
            logger.error(f"❌ Error executing move: {e}", exc_info=True)
            raise

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
                    if (os.path.exists(piece_image)):
                        self.buttons[(i, j)].setIcon(QIcon(piece_image))
                        # Set size based on piece type
                        size = self.PIECE_SIZES[piece_type]
                        self.buttons[(i, j)].setIconSize(QSize(size, size))
                    else:
                        print(f"Missing image: {piece_image}")
                else:
                    self.buttons[(i, j)].setIcon(QIcon())

    def show_game_over_message(self):
        """Show styled game over message with the result"""
        self.stop_timer()  # Stop the timer when the game is over
        
        if self.board.is_checkmate():
            winner = "Black" if self.board.turn else "White"
            title = "Checkmate!"
            message = f"{winner} Wins the Game!"
            dialog = GameOverDialog(title, message, self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.restart_game()
        elif self.board.is_stalemate():
            dialog = GameOverDialog("Stalemate!", "The Game is a Draw!", self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.restart_game()
        elif self.board.is_insufficient_material():
            dialog = GameOverDialog("Draw!", "Insufficient Material to Continue", self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.restart_game()

    # Determine why the game has ended by applying standard chess rules:
# - Checkmate: The player's king is under threat with no escape moves, so the opponent wins.
# - Stalemate: The current player has no legal moves, but their king is not in check, resulting in a draw.
# - Insufficient Material: There aren't enough pieces remaining to force a checkmate, so the game is drawn.
# - Fifty Moves Rule: If fifty consecutive moves occur without a pawn move or a capture, the game is drawn.
# - Threefold Repetition: If the same board position occurs three times, the game is drawn.

    def check_game_state(self):
        """Check the game state and handle game over conditions"""
        # Check if current player has no legal moves
        has_legal_moves = any(self.board.legal_moves)
        is_in_check = self.board.is_check()

        if not has_legal_moves:
            self.stop_timer()
            if is_in_check:  # Checkmate - current player lost
                loser = "White" if self.board.turn else "Black"
                winner = "Black" if self.board.turn else "White"
                title = "Checkmate!"
                message = f"{winner} is Victorious!\n{loser} has been defeated!"
            else:  # Stalemate
                title = "Stalemate!"
                message = "The game is a draw!"
            
            dialog = GameOverDialog(title, message, self)
            result = dialog.exec()
            
            if result == QDialog.DialogCode.Accepted:
                if dialog.choice == "new_game":
                    self.new_game()
                else:  # Return to menu
                    self.close()
                    self.show_start_menu()

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

    def show_error_dialog(self, title, message):
        """Show error dialog with enhanced styling"""
        error_box = QMessageBox(self)
        error_box.setIcon(QMessageBox.Icon.Critical)
        error_box.setWindowTitle(title)
        error_box.setText(message)
        error_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        error_box.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        return error_box.exec()

    def save_game(self):
        """Save the current game state with enhanced error handling"""
        try:
            logger.info("💾 Initiating game save")
            
            # Validate game state before saving
            if not self.board or not hasattr(self, 'game_mode'):
                raise GameStateError("❌ Invalid game state for saving")
            
            file_path = self._get_save_file_path()
            if not file_path:
                logger.info("ℹ️ Game save cancelled by user")
                return
            
            game_data = self._prepare_game_data()
            self._write_game_data(file_path, game_data)
            
            logger.info(f"✅ Game saved successfully to {file_path}")
            QMessageBox.information(self, "Success", "Game saved successfully!")
            
        except GameStateError as e:
            logger.error(str(e))
            self.show_error_dialog("Save Error", str(e))
        except Exception as e:
            error_msg = f"❌ Failed to save game: {str(e)}"
            logger.error(error_msg, exc_info=True)
            self.show_error_dialog("Save Error", error_msg)

    def _prepare_game_data(self):
        """Prepare game data for saving with validation"""
        try:
            return {
                'fen': self.board.fen(),
                'moves': [move.uci() for move in self.board.move_stack],
                'game_mode': self.game_mode,
                'move_history': self.move_history,
                'current_move_number': self.current_move_number,
                'time': self.time.toString('mm:ss'),
                'captured_pieces': {
                    'white': {str(k): v for k, v in self.captured_pieces['white'].items()},
                    'black': {str(k): v for k, v in self.captured_pieces['black'].items()}
                }
            }
        except Exception as e:
            logger.error(f"❌ Error preparing game data: {e}", exc_info=True)
            raise

    def _write_game_data(self, file_path, game_data):
        """Write game data to file with proper error handling"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(game_data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            logger.error(f"❌ IO Error while saving game: {e}", exc_info=True)
            raise
        except json.JSONEncodeError as e:
            logger.error(f"❌ JSON encoding error: {e}", exc_info=True)
            raise

    def load_game(self):
        """Load a game state with improved error handling"""
        try:
            logger.info("📂 Initiating game load")
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Load Game",
                "",
                "Chess Files (*.chess)",
                options=QFileDialog.Option.DontUseNativeDialog
            )
            
            if not file_path:
                logger.info("ℹ️ Game load cancelled by user")
                return
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    game_data = json.load(file)
                logger.debug(f"Successfully read game data from {file_path}")
            except json.JSONDecodeError as e:
                logger.error(f"Invalid game file format: {e}", exc_info=True)
                raise ValueError("Invalid game file format")
            except IOError as e:
                logger.error(f"Error reading game file: {e}", exc_info=True)
                raise
            
            # Validate required game data
            required_fields = ['fen', 'moves', 'game_mode']
            missing_fields = [field for field in required_fields if field not in game_data]
            if missing_fields:
                error_msg = f"Missing required fields in game file: {', '.join(missing_fields)}"
                logger.error(error_msg)
                raise ValueError(error_msg)
            
            # Process the loaded game
            self.process_loaded_game(game_data)
            logger.info("✅ Game loaded successfully")
            
        except Exception as e:
            error_msg = f"❌ Failed to load game: {str(e)}"
            logger.error(error_msg, exc_info=True)
            self.show_error_dialog("Load Error", error_msg)

    def process_loaded_game(self, game_data):
        """Process loaded game data with validation"""
        try:
            # Validate FEN string
            if not chess.Board.is_valid_fen(game_data['fen']):
                raise ValueError("Invalid FEN string in game file")
            
            self.board.set_fen(game_data['fen'])
            self.game_mode = game_data.get('game_mode', 'Player')
            self.move_history = game_data.get('move_history', [])
            self.current_move_number = game_data.get('current_move_number', 1)
            
            # Load captured pieces with validation
            if 'captured_pieces' in game_data:
                try:
                    self.captured_pieces = {
                        'white': {eval(k): v for k, v in game_data['captured_pieces']['white'].items()},
                        'black': {eval(k): v for k, v in game_data['captured_pieces']['black'].items()}
                    }
                except (SyntaxError, NameError) as e:
                    logger.warning(f"Error loading captured pieces: {e}")
                    self.captured_pieces = {'white': Counter(), 'black': Counter()}
            
            # Reset game state
            self.selected_square = None
            self.possible_moves.clear()
            self.move_list.clear()
            
            # Update display
            self.update_board()
            self.update_turn_indicator()
            
            QMessageBox.information(self, "Success", "Game loaded successfully!")
            
        except Exception as e:
            logger.error(f"Error processing loaded game data: {e}", exc_info=True)
            raise

    def update_turn_indicator(self):
        """Update the status label to show current turn with dynamic styling"""
        current_turn = "White" if self.board.turn else "Black"
        self.status_label.setText(f"Player: {current_turn}")
        
        # Set background and text color based on current turn
        if self.board.turn:  # White's turn
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #2C3E50;
                    color: white;
                    font-size: 10px;
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
                    font-size: 12px;
                    font-weight: bold;
                    padding: 5px 15px;
                    border-radius: 5px;
                }
            """)

    def __del__(self):
        """Clean up resources with improved error handling"""
        try:
            if hasattr(self, 'engine') and self.engine:
                logger.info("🧹 Cleaning up Stockfish engine")
                try:
                    if hasattr(self.engine, '_stockfish'):
                        self.engine._stockfish.terminate()
                    logger.info("✅ Stockfish engine cleaned up successfully")
                except Exception as e:
                    logger.error(f"❌ Error terminating Stockfish: {e}", exc_info=True)
        except Exception as e:
            logger.error(f"❌ Error in cleanup: {e}", exc_info=True)



