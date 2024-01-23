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
