import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QTextEdit
)
from PySide6.QtCore import Qt

class InvisibleManUI(QWidget):
    def __init__(self):
        super().__init__()
        self.game = None
        self.initUI()

    def initUI(self):
        # Main layout setup
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setWindowTitle("Invisible Man Game")

        # Instruction text
        instructions = QLabel("Welcome to the Invisible Man Game!\nPress 'Start Game' to play.")
        instructions.setWordWrap(True)
        main_layout.addWidget(instructions)

        # Setup screen components
        setup_layout = QVBoxLayout()
        main_layout.addLayout(setup_layout)

        # Option checkboxes
        self.opt_duplicate_guesses = QCheckBox("Prevent duplicate guesses")
        self.opt_show_previous = QCheckBox("Show previous guesses")
        setup_layout.addWidget(self.opt_duplicate_guesses)
        setup_layout.addWidget(self.opt_show_previous)

        # Button for game control
        self.btn_start_game = QPushButton("Start Game")
        self.btn_start_game.clicked.connect(self.start_game)
        setup_layout.addWidget(self.btn_start_game)

        # Game screen components
        game_layout = QVBoxLayout()
        main_layout.addLayout(game_layout)

        self.label_word_display = QLabel("")
        self.label_word_display.setAlignment(Qt.AlignCenter)
        self.guess_input = QLineEdit()
        self.guess_input.setPlaceholderText("Enter a letter or word")
        self.btn_guess = QPushButton("Guess")
        self.btn_guess.clicked.connect(self.make_guess)
        self.btn_guess.setEnabled(False)

        self.stick_figure_display = QLabel("")
        self.stick_figure_display.setAlignment(Qt.AlignCenter)
        game_layout.addWidget(self.label_word_display)
        game_layout.addWidget(self.guess_input)
        game_layout.addWidget(self.btn_guess)
        game_layout.addWidget(self.stick_figure_display)

        # Result/Feedback area
        self.feedback = QTextEdit()
        self.feedback.setReadOnly(True)
        self.feedback.setPlaceholderText("Results and feedback will appear here.")
        game_layout.addWidget(self.feedback)

        # Initial visibility
        self.show()

    def start_game(self):
        # Fetch a random word and start the game
        response = requests.get('https://random-word-api.herokuapp.com/word')
        if response.status_code == 200:
            self.game = InvisibleManGame(response.json()[0])
            self.update_display()
            self.feedback.clear()
            self.feedback.append("Game started! Try guessing a letter or the entire word.")
            self.btn_guess.setEnabled(True)
            self.stick_figure_display.setText('')  # Reset the stick figure display
        else:
            QMessageBox.critical(self, "API Error", f"Failed to fetch word: {response.status_code}")

    def make_guess(self):
        guess = self.guess_input.text().strip().lower()
        if not guess:
            QMessageBox.critical(self, "Error", "Please enter a guess.")
            return

        result, message = self.game.guess(guess)
        self.update_display()
        self.feedback.append(message)
        self.update_stick_figure()
        if self.game.is_game_over():
            final_message = "YOU WON!" if self.game.did_win() else "YOU LOST!"
            self.label_word_display.setText(self.game.word)  # Reveal the word
            self.feedback.append(final_message)
            self.btn_guess.setEnabled(False)

    def update_display(self):
        display_word = self.game.get_display_word()
        self.label_word_display.setText(' '.join(display_word))

    def update_stick_figure(self):
        if self.game is None:
            return
        parts = [
            " ( ) ",    # Head
            "  |  ",    # Neck
            " /|\\ ",  # Arms
            "  |  ",    # Torso
            " / \\ "   # Legs
        ]
        display = ""
        for i in range(self.game.incorrect_guesses):
            if i == 0:
                display += parts[0] + "\n"
            elif i == 1:
                display += parts[1] + "\n"
            elif i == 2:
                display += parts[2] + "\n"
            elif i == 3:
                display += parts[3] + "\n"
            elif i >= 4:
                display += parts[4] + "\n"
        self.stick_figure_display.setText(display)

class InvisibleManGame:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = set()
        self.incorrect_guesses = 0

    def get_display_word(self):
        return ['*' if letter not in self.guessed else letter for letter in self.word]

    def guess(self, guess):
        if guess in self.guessed:
            return False, f"You've already guessed '{guess}'. Try something different."
        self.guessed.add(guess)

        if guess in self.word:
            if set(self.word) <= self.guessed:
                return True, "Congratulations! You've guessed the word correctly!"
            return True, f"Good guess! '{guess}' is in the word."
        else:
            self.incorrect_guesses += 1
            return False, f"Wrong guess! There's no '{guess}' in the word."

    def is_game_over(self):
        return self.incorrect_guesses >= 5 or set(self.word) <= self.guessed

    def did_win(self):
        return set(self.word) <= self.guessed and self.incorrect_guesses < 5

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = InvisibleManUI()
    sys.exit(app.exec())
