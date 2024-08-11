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