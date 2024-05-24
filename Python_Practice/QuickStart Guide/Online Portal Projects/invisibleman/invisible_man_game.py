import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QTextEdit
)
from PySide6.QtCore import Qt

class InvisibleManUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout setup
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setWindowTitle("Invisible Man Game")

        # Instruction text
        instructions = QLabel("Welcome to the Invisible Man Game!\nEnter a word or get a random one, then guess letters to find the hidden word.")
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

        # Word input
        self.input_word = QLineEdit()
        self.input_word.setPlaceholderText("Enter a word or click 'Get Random Word'")
        setup_layout.addWidget(QLabel("Word:"))
        setup_layout.addWidget(self.input_word)

        # Buttons for game control
        self.btn_get_random = QPushButton("Get Random Word")
        self.btn_get_random.clicked.connect(self.fetch_random_word)
        self.btn_start_game = QPushButton("Start Game")
        self.btn_start_game.clicked.connect(self.start_game)
        setup_layout.addWidget(self.btn_get_random)
        setup_layout.addWidget(self.btn_start_game)

        # Game screen components
        game_layout = QVBoxLayout()
        main_layout.addLayout(game_layout)

        self.label_word_display = QLabel("")
        self.guess_input = QLineEdit()
        self.guess_input.setPlaceholderText("Enter a letter or word")
        self.btn_guess = QPushButton("Guess")
        self.btn_guess.clicked.connect(self.make_guess)

        game_layout.addWidget(self.label_word_display)
        game_layout.addWidget(self.guess_input)
        game_layout.addWidget(self.btn_guess)

        # Result/Feedback area
        self.feedback = QTextEdit()
        self.feedback.setReadOnly(True)
        self.feedback.setPlaceholderText("Results and feedback will appear here.")
        game_layout.addWidget(self.feedback)

        # Initial visibility
        self.show()

    def fetch_random_word(self):
        response = requests.get('https://random-word-api.herokuapp.com/word')
        if response.status_code == 200:
            self.input_word.setText(response.json()[0])
        else:
            QMessageBox.critical(self, "API Error", f"Failed to fetch word: {response.status_code}")

    def start_game(self):
        word = self.input_word.text().strip()
        if not word:
            QMessageBox.critical(self, "Error", "Please enter a word or fetch one to start the game.")
            return

        self.game = InvisibleManGame(word)
        self.update_display()
        self.feedback.append("Game started! Try guessing a letter or the entire word.")

    def make_guess(self):
        guess = self.guess_input.text().strip().lower()
        if not guess:
            QMessageBox.critical(self, "Error", "Please enter a guess.")
            return

        result, message = self.game.guess(guess)
        self.update_display()
        self.feedback.append(message)
        if result:
            self.guess_input.clear()

    def update_display(self):
        display_word = self.game.get_display_word()
        self.label_word_display.setText(' '.join(display_word))

    def get_random_word(self):
        try:
            response = requests.get('https://random-word-api.herokuapp.com/word')
            if response.status_code == 200:
                return response.json()[0]
            else:
                QMessageBox.critical(self, "API Error", f"Failed to fetch word: {response.status_code}")
        except Exception as e:
            QMessageBox.critical(self, "Network Error", str(e))
        return None

class InvisibleManGame:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = set()

    def get_display_word(self):
        return [letter if letter in self.guessed else '_' for letter in self.word]

    def guess(self, guess):
        if guess in self.guessed:
            return False, f"You've already guessed '{guess}'. Try something different."
        self.guessed.add(guess)

        if guess in self.word:
            if set(self.word) <= self.guessed:
                return True, "Congratulations! You've guessed the word correctly!"
            return True, f"Good guess! '{guess}' is in the word."
        else:
            return False, f"Wrong guess! There's no '{guess}' in the word."

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = InvisibleManUI()
    sys.exit(app.exec())
