# Import Necessary Modules
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")  # Window Title
        self.current_player = "X"  # Human always starts
        self.is_human_turn = True  # Track if it's human's turn
        self.scores = {'Human': 0, 'AI': 0}  # Track scores for human & AI
        self.initUI()  # Call the method to set up the user interface

    def initUI(self):
        # Central widget & layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # Create a vertical layout to include both the grid & the restart button
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()  # Use a grid layout for the buttons

        # Initialize a Grid to hold button references organized in a 3x3 matrix
        self.buttons = []
        for i in range(3):  # Loop for each row
            row = []
            for j in range(3):  # Loop for each column
                button = QPushButton(" ")  # Create a button w/ an empty label
                button.setFixedSize(100, 100)  # Set fixed size for the button
                # Connect button click to the handler w/ parameters x and y
                button.clicked.connect(lambda _, x=i, y=j: self.on_button_clicked(x, y))
                row.append(button)
                grid_layout.addWidget(button, i, j)  # Add the button to the grid layout at position (i, j)
            self.buttons.append(row)
        
        # Add a label to display the scores
        self.score_label = QLabel("Human: 0, AI: 0")  # Score label to display scores
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add restart button below the grid
        self.restart_button = QPushButton("Restart")
        self.restart_button.clicked.connect(self.restart_game)  # Connect the restart button to its handler
        
        main_layout.addWidget(self.score_label) # Add the score label to the main layout
        main_layout.addLayout(grid_layout)  # Add the grid layout to the main layout
        main_layout.addWidget(self.restart_button)  # Add the restart button to the main layout

        self.central_widget.setLayout(main_layout)  # Apply the main layout to the central widget

    def on_button_clicked(self, x, y):
        # Handle a button click at position (x, y)
        if self.buttons[x][y].text() == " ":  # Check if the button is still empty
            self.buttons[x][y].setText(self.current_player)
            if not self.check_game_over():
                self.switch_player()
                self.ai_move()

    # AI Algorithm To Block Human Win
    def ai_move(self):
        x, y = self.find_best_move()
        self.buttons[x][y].setText(self.current_player)
        if not self.check_game_over():  # Check if the game is over after AI move
            self.switch_player()
            
    # Checks if placing a mark at a given position results in a win & if not, returns the position to block the human win
    
    def find_best_move(self):
        # Check for possible win or block needed
        for is_ai in [True, False]:  # First check for AI win, then for human win to block
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j].text() == " ": # Check if space is empty
                        self.buttons[i][j].setText("O" if is_ai else "X") # Set the text to AI or Human
                        if self.check_winner(): # Check if the move results in a win
                            self.buttons[i][j].setText(" ") # Reset the button text
                            return i, j  # Return winning/blocking move
                        self.buttons[i][j].setText(" ") # Reset the button text
        
        # After immediate win/block moves, check for other strategies w/ Center > Corners > Random
        if self.buttons[1][1].text() == " ": # Check if the center is empty
            return 1, 1 # Return the center position
        
        # Prefer corners if available
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)] # List of corner positions
        available_corners = [(i, j) for i, j in corners if self.buttons[i][j].text() == " "] # Check for empty corners
        if available_corners: # If there are empty corners
            return random.choice(available_corners) # Return a random corner
        
        # Random fallback for any other empty spaces
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j].text() == " "] # Check for empty spaces
        return random.choice(available_moves) if available_moves else (None, None) # Return a random empty space or None

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.is_human_turn = not self.is_human_turn

    def check_game_over(self):
        if self.check_winner():
            winner = "Human" if self.current_player == "X" else "AI"
            self.scores[winner] += 1  # Update scores based on winner
            self.update_score_label()
            self.end_game(f"Player {self.current_player} wins!")
            return True
        elif self.is_draw():
            self.end_game("It's a draw!")
            return True
        return False

    def update_score_label(self):
        self.score_label.setText(f"Human: {self.scores['Human']}, AI: {self.scores['AI']}")

    def restart_game(self):
        # Reset the game state
        for row in self.buttons:
            for button in row:
                button.setText(" ")
                button.setEnabled(True)
        self.current_player = "X"  # Reset the starting player
        self.is_human_turn = True

    def check_winner(self):
        # Check rows, columns, & diagonals for a winning pattern
        for i in range(3):
            if (self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != " " or
                self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != " "):
                return True
        if (self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != " " or
            self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != " "):
            return True
        return False

    def is_draw(self):
        # Check all buttons to determine if the game is a draw (no empty spaces left)
        for row in self.buttons:
            for button in row:
                if button.text() == " ":
                    return False
        return True

    def end_game(self, message):
        # Disable all buttons & print the game result
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)
        print(message)

# Initialize the app & display the game window
app = QApplication([])
window = TicTacToe()
window.show()
app.exec()

# To run this code, you need to have Python & PyQt6 installed by running the following commands:
# `pip install PyQt6` or `pip3 install PyQt6` or `pipenv install PyQt6` if you're using pipenv to manage dependencies.
# Then, you can run the script using the command `python tictactoe.py` or `python3 tictactoe.py`.