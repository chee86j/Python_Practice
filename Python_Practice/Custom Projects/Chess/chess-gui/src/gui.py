import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget
from PyQt5.QtCore import QSize
import chess
import subprocess

class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Game")
        self.setFixedSize(QSize(800, 800))
        self.board = chess.Board()
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
        stockfish = subprocess.Popen(
            ["python", "sunfish.py"],
            universal_newlines=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            cwd="c:/Users/jeffr/Documents/Python_Practice/Python_Practice/Custom Projects/Chess/chess-gui/src/sunfish"
        )
        stockfish.stdin.write(f"position fen {self.board.fen()}\n")
        stockfish.stdin.write("go movetime 1000\n")
        stockfish.stdin.flush()

        while True:
            text = stockfish.stdout.readline().strip()
            if text.startswith("bestmove"):
                move = chess.Move.from_uci(text.split()[1])
                break

        stockfish.stdin.write("quit\n")
        stockfish.stdin.flush()
        stockfish.terminate()
        return move

    def update_board(self):
        # Update the GUI to reflect the current board state
        for i in range(8):
            for j in range(8):
                piece = self.board.piece_at(chess.square(j, 7 - i))
                self.buttons[(i, j)].setText(piece.symbol() if piece else "")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessGUI()
    window.show()
    sys.exit(app.exec_())