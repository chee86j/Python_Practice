import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QGridLayout
)
from PySide6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the layout
        layout = QVBoxLayout()
        
        # Create display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)
        
        # Create buttons
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Create a grid layout for buttons
        grid_layout = QGridLayout()
        for i, button_text in enumerate(self.buttons):
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, i // 4, i % 4)
        
        layout.addLayout(grid_layout)
        
        # Set the main layout of the window
        self.setLayout(layout)
        self.setWindowTitle("Basic Calculator")
        self.show()

    def on_button_click(self):
        button = self.sender()
        button_text = button.text()

        current_text = self.display.text()

        if button_text == '=':
            try:
                # Evaluate the expression and set the result to the display
                result = str(eval(current_text))
                self.display.setText(result)
            except Exception as e:
                # Show an error message if there is an exception
                QMessageBox.critical(self, 'Error', 'Invalid Input')
        else:
            # Append the button text to the current display text
            new_text = current_text + button_text
            self.display.setText(new_text)

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
# The Calculator class inherits from QWidget and initializes the UI with a 
# display QLineEdit and buttons for numbers and operators.
# The init_ui() method sets up the layout, display, and buttons for the calculator.
# The on_button_click() method handles button clicks and updates the display text.
# The main() function creates the QApplication and Calculator instance to run the app.
# The if __name__ == "__main__": block ensures that the main function is called when the script is run.

# To run the script, navigate to the directory containing the calculator.py file and run
# 'python3 calculator.py' or 'python calculator.py' in the terminal.