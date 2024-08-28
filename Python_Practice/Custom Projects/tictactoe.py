# Import Necessary Modules
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")  # Window Title
        self.current_player = "X"  # Initialize the starting player
        self.initUI()  # Call the method to set up the user interface
    
    def initUI(self):
        # Central widget & layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QGridLayout()  # Use a grid layout for the buttons
        
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
                layout.addWidget(button, i, j)  # Add the button to the grid layout at position (i, j)
            self.buttons.append(row)
        
        self.central_widget.setLayout(layout)  # Apply the layout to the central widget

    def on_button_clicked(self, x, y):
        # Handle a button click at position (x, y)
        if self.buttons[x][y].text() == " ":  # Check if the button is still empty
            self.buttons[x][y].setText(self.current_player)  # Set the button to the current player's symbol
            if self.check_winner():  # Check for a win
                self.end_game(f"Player {self.current_player} wins!")
            elif self.is_draw():  # Check for a draw
                self.end_game("It's a draw!")
            else:  # Change the player
                self.current_player = "O" if self.current_player == "X" else "X"
    
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