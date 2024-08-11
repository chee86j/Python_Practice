import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QRadioButton, QButtonGroup, QMessageBox
)
from PySide6.QtCore import Qt

# Dictionary of questions, options, and answers
questions = [
    {
        'prompt': 'What are the most common shades of an apple?',
        'options': ['Red/Green', 'Purple', 'Orange', 'Yellow'],
        'answer': 'Red/Green'
    },
    {
        'prompt': 'What is the capital of France?',
        'options': ['London', 'Paris', 'Rome', 'Berlin'],
        'answer': 'Paris'
    },
    {
        'prompt': 'Which planet is known as the Red Planet?',
        'options': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'prompt': 'Who wrote "To Kill a Mockingbird"?',
        'options': ['Harper Lee', 'J.K. Rowling', 'Mark Twain', 'Ernest Hemingway'],
        'answer': 'Harper Lee'
    },
    {
        'prompt': 'What is the chemical symbol for water?',
        'options': ['Wa', 'H2O', 'Wi', 'H'],
        'answer': 'H2O'
    },
    {
        'prompt': 'What is the tallest mammal?',
        'options': ['Giraffe', 'Elephant', 'Hippopotamus', 'Rhinoceros'],
        'answer': 'Giraffe'
    },
    {
        'prompt': 'Which country is home to the kangaroo?',
        'options': ['Australia', 'Brazil', 'Canada', 'South Africa'],
        'answer': 'Australia'
    },
    {
        'prompt': 'Who painted the Mona Lisa?',
        'options': ['Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Michelangelo'],
        'answer': 'Leonardo da Vinci'
    },
    {
        'prompt': 'What is the currency of Japan?',
        'options': ['Yen', 'Dollar', 'Euro', 'Pound'],
        'answer': 'Yen'
    },
    {
        'prompt': 'Which gas do plants absorb to produce oxygen?',
        'options': ['Carbon Dioxide', 'Oxygen', 'Nitrogen', 'Hydrogen'],
        'answer': 'Carbon Dioxide'
    },
    {
        'prompt': 'What is the largest ocean on Earth?',
        'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
        'answer': 'Pacific Ocean'
    },
    {
        'prompt': 'Who developed the theory of relativity?',
        'options': ['Isaac Newton', 'Galileo Galilei', 'Albert Einstein', 'Niels Bohr'],
        'answer': 'Albert Einstein'
    },
    {
        'prompt': 'What is the hardest natural substance on Earth?',
        'options': ['Gold', 'Iron', 'Diamond', 'Platinum'],
        'answer': 'Diamond'
    },
    {
        'prompt': 'Which planet is closest to the Sun?',
        'options': ['Earth', 'Venus', 'Mercury', 'Mars'],
        'answer': 'Mercury'
    },
    {
        'prompt': 'What is the main ingredient in guacamole?',
        'options': ['Tomato', 'Avocado', 'Pepper', 'Onion'],
        'answer': 'Avocado'
    },
    {
        'prompt': 'What is the capital of Japan?',
        'options': ['Kyoto', 'Osaka', 'Tokyo', 'Hiroshima'],
        'answer': 'Tokyo'
    },
    {
        'prompt': 'Who is the author of "1984"?',
        'options': ['George Orwell', 'Aldous Huxley', 'Ray Bradbury', 'Philip K. Dick'],
        'answer': 'George Orwell'
    },
    {
        'prompt': 'What is the largest continent by area?',
        'options': ['Africa', 'Asia', 'Europe', 'North America'],
        'answer': 'Asia'
    },
    {
        'prompt': 'What year did the Titanic sink?',
        'options': ['1900', '1912', '1920', '1930'],
        'answer': '1912'
    },
    {
        'prompt': 'What is the chemical symbol for gold?',
        'options': ['Au', 'Ag', 'Pb', 'Fe'],
        'answer': 'Au'
    },
    {
        'prompt': 'What is the name of the longest river in South America?',
        'options': ['Amazon', 'Nile', 'Yangtze', 'Mississippi'],
        'answer': 'Amazon'
    },
    {
        'prompt': 'Who was the first person to walk on the moon?',
        'options': ['Buzz Aldrin', 'Michael Collins', 'Yuri Gagarin', 'Neil Armstrong'],
        'answer': 'Neil Armstrong'
    },
    {
        'prompt': 'What is the value of Planck’s constant?',
        'options': ['6.626 x 10^-34 J·s', '3.14 x 10^-20 J·s', '9.81 x 10^9 J·s', '1.602 x 10^-19 J·s'],
        'answer': '6.626 x 10^-34 J·s'
    },
    {
        'prompt': 'What is the capital city of Mongolia?',
        'options': ['Astana', 'Ulaanbaatar', 'Tashkent', 'Baku'],
        'answer': 'Ulaanbaatar'
    },
    {
        'prompt': 'Which element has the atomic number 79?',
        'options': ['Gold', 'Silver', 'Platinum', 'Copper'],
        'answer': 'Gold'
    },
    {
        'prompt': 'In which year did the Cold War officially end?',
        'options': ['1985', '1989', '1991', '1995'],
        'answer': '1991'
    },
    {
        'prompt': 'What is the name of the largest volcano in the solar system?',
        'options': ['Mount Fuji', 'Kilauea', 'Olympus Mons', 'Mauna Kea'],
        'answer': 'Olympus Mons'
    },
    {
        'prompt': 'Who is known as the father of modern chemistry?',
        'options': ['Dmitri Mendeleev', 'Antoine Lavoisier', 'Robert Boyle', 'Joseph Priestley'],
        'answer': 'Antoine Lavoisier'
    },
    {
        'prompt': 'Which famous physicist is known for the uncertainty principle?',
        'options': ['Albert Einstein', 'Werner Heisenberg', 'Niels Bohr', 'Max Planck'],
        'answer': 'Werner Heisenberg'
    },
    {
        'prompt': 'What is the name of the ship that famously sank in 1912?',
        'options': ['RMS Titanic', 'RMS Lusitania', 'HMS Bounty', 'MS Andrea Doria'],
        'answer': 'RMS Titanic'
    }
]

class QuizGame(QWidget):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lifelines = 3
        self.current_question = 0
        self.init_ui()
        self.display_question()

    def init_ui(self):
        # Set up layout
        layout = QVBoxLayout()
        
        # Question label
        self.question_label = QLabel()
        layout.addWidget(self.question_label)
        
        # Options
        self.option_buttons = [QRadioButton() for _ in range(4)]
        self.option_group = QButtonGroup()
        for button in self.option_buttons:
            self.option_group.addButton(button)
            layout.addWidget(button)
        
        # Answer button
        self.submit_button = QPushButton('Submit Answer')
        self.submit_button.clicked.connect(self.check_answer)
        layout.addWidget(self.submit_button)
        
        # Lifeline button
        self.lifeline_button = QPushButton('Use Lifeline')
        self.lifeline_button.clicked.connect(self.use_lifeline)
        layout.addWidget(self.lifeline_button)
        
        # Lifeline tracker
        self.lifeline_tracker = QLabel()
        layout.addWidget(self.lifeline_tracker)
        
        # Set layout
        self.setLayout(layout)
        self.setWindowTitle('Quiz Game')
        self.show()

    def display_question(self):
        # Display current question and options
        question = questions[self.current_question]
        self.question_label.setText(question['prompt'])
        
        options = question['options']
        for i, button in enumerate(self.option_buttons):
            button.setText(options[i])
            button.setChecked(False)
            button.setEnabled(True)  # Re-enable buttons after lifeline use
            button.setStyleSheet("")  # Reset any previous styling
        
        # Update lifeline tracker
        self.update_lifeline_tracker()

    def check_answer(self):
        selected_button = self.option_group.checkedButton()
        if selected_button:
            selected_option = selected_button.text()
            correct_answer = next(q['answer'] for q in questions if q['prompt'] == self.question_label.text())
            if selected_option == correct_answer:
                self.score += 1
                QMessageBox.information(self, 'Result', 'Correct!')
            else:
                QMessageBox.information(self, 'Result', 'Incorrect!')
            
            self.current_question += 1
            if self.current_question < len(questions):
                self.display_question()
            else:
                QMessageBox.information(self, 'Quiz Finished', f'Your score is {self.score} out of {len(questions)}')
                self.close()

    def use_lifeline(self):
        if self.lifelines > 0:
            self.lifelines -= 1
            question = questions[self.current_question]
            correct_answer = question['answer']
            incorrect_options = [opt for opt in question['options'] if opt != correct_answer]
            options_to_remove = random.sample(incorrect_options, min(2, len(incorrect_options)))
            
            for button in self.option_buttons:
                if button.text() in options_to_remove:
                    button.setStyleSheet("text-decoration: line-through;")  # Apply strikethrough effect
                else:
                    button.setEnabled(True)
            QMessageBox.information(self, 'Lifeline Used', 'Two incorrect options have been crossed out.')
            
            # Update lifeline tracker and reset the question
            self.update_lifeline_tracker()
        else:
            QMessageBox.warning(self, 'No Lifelines', 'No lifelines remaining.')

    def update_lifeline_tracker(self):
        self.lifeline_tracker.setText(f'Lifelines Remaining: {self.lifelines}/3')

def main():
    app = QApplication(sys.argv)
    quiz_game = QuizGame()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

# The QuizGame class creates a simple quiz game using PySide6. It displays a question with four options
# and allows the user to select an answer. The user can also use a lifeline to eliminate two incorrect
# options. The game keeps track of the score and the number of lifelines remaining. Once all questions
# have been answered, a message box displays the final score. The game is implemented using a QWidget
# with a vertical layout that includes a question label, option buttons, an answer button, a lifeline
# button, and a lifeline tracker. 