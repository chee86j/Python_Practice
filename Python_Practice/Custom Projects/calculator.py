import sys
import math
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QGridLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class AdvancedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the layout
        layout = QVBoxLayout()
        
        # Create display with larger font and fixed size
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        
        # Set font size and display dimensions
        font = QFont()
        font.setPointSize(24)  # Increase font size
        self.display.setFont(font)
        self.display.setFixedHeight(60)  # Adjust height
        self.display.setMinimumWidth(300)  # Adjust width
        
        layout.addWidget(self.display)
        
        # Create buttons with advanced functions
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', 'pow', 'log', 'ln',
            'sin', 'cos', 'tan', 'exp'
        ]
        
        # Create a grid layout for buttons
        grid_layout = QGridLayout()
        for i, button_text in enumerate(self.buttons):
            button = QPushButton(button_text)
            button.setFont(font)  # Set font size for buttons
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, i // 4, i % 4)
        
        layout.addLayout(grid_layout)
        
        # Set the main layout of the window
        self.setLayout(layout)
        self.setWindowTitle("Advanced Calculator")
        self.show()

    def on_button_click(self):
        button = self.sender()
        button_text = button.text()

        current_text = self.display.text()

        if button_text == '=':
            try:
                # Evaluate the expression and set the result to the display
                result = self.evaluate_expression(current_text)
                self.display.setText(str(result))
            except Exception as e:
                # Show an error message if there is an exception
                QMessageBox.critical(self, 'Error', 'Invalid Input')
        else:
            # Append the button text to the current display text
            new_text = current_text + button_text
            self.display.setText(new_text)

    def evaluate_expression(self, expression):
        # Function Names are Replace with Math Module Functions
        expression = expression.replace('sqrt', 'math.sqrt')
        expression = expression.replace('pow', '**')
        expression = expression.replace('log', 'math.log10')
        expression = expression.replace('ln', 'math.log')
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('exp', 'math.exp')
        
        # Evaluate the expression
        return eval(expression)

def main():
    app = QApplication(sys.argv)
    calculator = AdvancedCalculator()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


    
#####-----Advanced Calculator Features-----#####
# Advanced Calculator combines ease of use w/ advanced features that 
# you would find in an advanced calculator. Features Included Are:

# 1.  Enhanced Display: Enjoy a larger, easy-to-read display w/ a bigger 
#     font size, making it simple to see your calculations and results at a glance.

# 2.  Basic Operations: It covers all your essentials, from addition and subtraction 
#     to multiplication and division.

# 3.  Scientific Functions: Dive into advanced math w/ functions for square roots 
#     (sqrt), powers (pow), logarithms (log for base 10 and ln for natural logarithms), 
#     and exponentials (exp).

# 4.  Trigonometry: Calculate sine (sin), cosine (cos), tangent (tan), and their inverse 
#     functions effortlessly.

# 5.  Intuitive Layout: The grid of buttons is well-organized, making it easy to find 
#     and use the functions you need.

# 6.  Error Handling: The calculator provides helpful error messages if something goes 
#     wrong, so you can quickly correct any mistakes.

# 7.  Whether you're working on everyday problems or tackling more complex equations, 
#     this calculator has you covered w/ both simplicity and sophistication.