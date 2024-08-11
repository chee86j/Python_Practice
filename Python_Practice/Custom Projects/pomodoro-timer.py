import sys
import time
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont, QColor

class PomodoroTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.remaining_time = 0
        self.current_mode = 'work'
        self.work_duration = 25 * 60
        self.break_duration = 5 * 60
        self.long_break_duration = 15 * 60

    def init_ui(self):
        # Set up the UI Layout
        layout = QVBoxLayout()
        
       # Instruction Label
        self.instruction_label = QLabel(
            "Welcome to the Pomodoro Timer!\n\n"
            "1. **Set your work and break times.**\n"
            "2. **Start the timer** and focus on your task.\n"
            "3. **Take breaks** as indicated.\n"
            "4. **Repeat** and boost your productivity!"
        )
        self.instruction_label.setAlignment(Qt.AlignCenter)
        self.instruction_label.setWordWrap(True)  # Allow text to wrap
        self.instruction_label.setStyleSheet("color: #e0e0e0; padding: 10px; font-size: 14px;")
        layout.addWidget(self.instruction_label)

        # Label to Display the Remaining Time
        self.time_display = QLabel()
        self.time_display.setAlignment(Qt.AlignCenter)
        self.time_display.setFont(QFont("Arial", 48))  # Large Font Size
        self.time_display.setStyleSheet("color: #e0e0e0;")  # Light Text Color for Dark Mode
        layout.addWidget(self.time_display)

        # Input Fields to Customize Durations
        self.work_input = QLineEdit()
        self.work_input.setPlaceholderText('Work Duration (mins)')
        self.work_input.setStyleSheet("padding: 10px; font-size: 16px; border: 1px solid #444; background-color: #333; color: #e0e0e0;")  # Dark Background, Light Text
        layout.addWidget(self.work_input)

        self.break_input = QLineEdit()
        self.break_input.setPlaceholderText('Short Break Duration (mins)')
        self.break_input.setStyleSheet("padding: 10px; font-size: 16px; border: 1px solid #444; background-color: #333; color: #e0e0e0;")
        layout.addWidget(self.break_input)

        self.long_break_input = QLineEdit()
        self.long_break_input.setPlaceholderText('Long Break Duration (mins)')
        self.long_break_input.setStyleSheet("padding: 10px; font-size: 16px; border: 1px solid #444; background-color: #333; color: #e0e0e0;")
        layout.addWidget(self.long_break_input)

        # Button to Start the Timer
        self.start_button = QPushButton('Start')
        self.start_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-size: 18px; border-radius: 5px;")
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        # Button to Skip the Current Duration
        self.skip_button = QPushButton('Skip')
        self.skip_button.setStyleSheet("background-color: #f44336; color: white; padding: 10px; font-size: 18px; border-radius: 5px;")
        self.skip_button.clicked.connect(self.skip_duration)
        layout.addWidget(self.skip_button)

        # Set Widget Layout
        self.setLayout(layout)
        self.setWindowTitle('Pomodoro Timer')
        self.setStyleSheet("background-color: #1e1e1e;")  # Dark Background for Widget
        self.show()

    def start_timer(self):
        try:
            self.work_duration = int(self.work_input.text()) * 60
            self.break_duration = int(self.break_input.text()) * 60
            self.long_break_duration = int(self.long_break_input.text()) * 60
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numbers for durations.')
            return

        self.current_mode = 'work'
        self.remaining_time = self.work_duration
        self.update_time_display()
        self.timer.start(1000)

    def update_time(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.timer.stop()
            if self.current_mode == 'work':
                self.current_mode = 'break'
                self.remaining_time = self.break_duration
                QMessageBox.information(self, 'Break Time', 'Time for a short break!')
            elif self.current_mode == 'break':
                self.current_mode = 'work'
                self.remaining_time = self.work_duration
                QMessageBox.information(self, 'Work Time', 'Back to work!')
            self.update_time_display()
            self.timer.start(1000)
        else:
            self.update_time_display()

    def update_time_display(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        self.time_display.setText(f'{minutes:02}:{seconds:02}')

    def skip_duration(self):
        self.remaining_time = 0
        self.update_time()

def main():
    app = QApplication(sys.argv)
    timer = PomodoroTimer()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
