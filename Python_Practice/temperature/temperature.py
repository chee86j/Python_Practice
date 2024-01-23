# Purpose: Temperature Converter App
# Starting Code Below to Use PySide6 (Qt for Python) to Build a GUI
import sys 
from PySide6.QtWidgets import (
    QApplication, QWidget
)
from PySide6.QtCore import Qt

class TemperatureConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Temperature Converter")
        self.setGeometry(100, 100, 400, 100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperatureConverterApp()
    window.show()
    sys.exit(app.exec_())

# -----------------------------------------------------------------------
#  Key Takeaways:
import sys 
from PySide6.QtWidgets import (
    QApplication, QWidget
)
from PySide6.QtCore import Qt

# TemperatureConverterApp is a custom class inheriting from QWidget.
# QWidget is a base class for all UI objects in PySide6 applications.
class TemperatureConverterApp(QWidget):
    def __init__(self):
        # Calls the constructor of the parent class (QWidget).
        super().__init__()
        # Initializes the user interface.
        self.init_ui()

    # Method to set up the user interface.
    def init_ui(self):
        # Sets the title of the window.
        self.setWindowTitle("Temperature Converter")
        # Sets the geometry of the window (x position, y position, width, height).
        self.setGeometry(100, 100, 400, 100)

# The following code will only run if this script is the main program.
if __name__ == "__main__":
    # Creates an instance of QApplication, necessary for any PySide6 application.
    app = QApplication(sys.argv)
    # Creates an instance of the TemperatureConverterApp.
    window = TemperatureConverterApp()
    # Shows the window.
    window.show()
    # Starts the event loop for the application. 
    # The application will wait here until it is closed.
    sys.exit(app.exec_())

# -----------------------------------------------------------------------

# Start of Solution with GUI Elements and Layouts

import sys 
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QPushButton, QHBoxLayout
)
from PySide6 import QtCore

class TemperatureConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Temperature Converter")
        self.setGeometry(100, 100, 400, 100)
        
        self.lbl_fahrenheit = QLabel("Fahrenheit:")
        self.edit_fahrenheit = QLineEdit()
        fahrenheit_layout = QVBoxLayout()
        fahrenheit_layout.addWidget(self.lbl_fahrenheit)
        fahrenheit_layout.addWidget(self.edit_fahrenheit)
        
        self.lbl_celsius = QLabel("Celsius:")
        self.edit_celsius = QLineEdit()
        celsius_layout = QVBoxLayout()
        celsius_layout.addWidget(self.lbl_celsius)
        celsius_layout.addWidget(self.edit_celsius)
        
        self.btn_to_celsius = QPushButton("\u2192")
        self.btn_to_celsius.setFixedWidth(50)
        self.btn_to_fahrenheit = QPushButton("\u2190")
        self.btn_to_fahrenheit.setFixedWidth(50)
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.btn_to_celsius)
        button_layout.addWidget(self.btn_to_fahrenheit)
        
        top_layout = QHBoxLayout()
        top_layout.addLayout(fahrenheit_layout)
        top_layout.addLayout(button_layout)
        top_layout.addLayout(celsius_layout)
        
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red")
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.error_label, alignment=QtCore.Qt.AlignCenter)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperatureConverterApp()
    window.show()
    sys.exit(app.exec_())
    
# -----------------------------------------------------------------------
#  Key Takeaways:

import sys 
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QPushButton, QHBoxLayout
)
from PySide6 import QtCore

class TemperatureConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Temperature Converter")
        self.setGeometry(100, 100, 400, 100)
        
        # The Design Below Can Be However You Want It to Be
        # The Cool Thing About PySide6 is That You Can Design Your Own GUI
        self.lbl_fahrenheit = QLabel("Fahrenheit:") # Creating a label for the Fahrenheit input.
        self.edit_fahrenheit = QLineEdit() # Creating a line edit (text input) for Fahrenheit.
        fahrenheit_layout = QVBoxLayout() # Setting up a vertical layout for the Fahrenheit label and input.
        fahrenheit_layout.addWidget(self.lbl_fahrenheit)
        fahrenheit_layout.addWidget(self.edit_fahrenheit)
        
        self.lbl_celsius = QLabel("Celsius:") # Creating a label for the Celsius input.
        self.edit_celsius = QLineEdit() # Creating a line edit (text input) for Celsius.
        celsius_layout = QVBoxLayout() # Setting up a vertical layout for the Celsius label and input.
        celsius_layout.addWidget(self.lbl_celsius)
        celsius_layout.addWidget(self.edit_celsius)
        
        self.btn_to_celsius = QPushButton("\u2192") # Creating a button for converting to Celsius, with an arrow symbol.
        self.btn_to_celsius.setFixedWidth(50)
        self.btn_to_fahrenheit = QPushButton("\u2190") # Creating a button for converting to Fahrenheit, with an arrow symbol.
        self.btn_to_fahrenheit.setFixedWidth(50)
        button_layout = QVBoxLayout() # Setting up a vertical layout for the conversion buttons.
        button_layout.addWidget(self.btn_to_celsius)
        button_layout.addWidget(self.btn_to_fahrenheit)
        
        # Setting up a horizontal layout for combining the above layouts.
        top_layout = QHBoxLayout()
        top_layout.addLayout(fahrenheit_layout)
        top_layout.addLayout(button_layout)
        top_layout.addLayout(celsius_layout)
        
        # Creating a label for displaying error messages.
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red")
        
        # Setting up the main layout for the window, including the error label.
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.error_label, alignment=QtCore.Qt.AlignCenter)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperatureConverterApp()
    window.show()
    sys.exit(app.exec_())
    
# -----------------------------------------------------------------------
