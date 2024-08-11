import sys
import time
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
)
from PySide6.QtCore import QTimer, Qt

class PomodoroTimer(QWidget):
    def __init__(self):
        super().__init__()
        # Initialize UI & Timer
        self.init_ui()
        self.timer = QTimer()  # QTimer to handle countdown
        self.timer.timeout.connect(self.update_time)  # Connect timeout signal to update_time method
        self.remaining_time = 0  # Time left for the current duration
        self.current_mode = 'work'  # Track current mode (work or break)
        # Default durations in seconds
        self.work_duration = 25 * 60  # 25 minutes for Work
        self.break_duration = 5 * 60   # 5 minutes for Short Break
        self.long_break_duration = 15 * 60  # 15 minutes for Long Break

    def init_ui(self):
        # Set up the UI Layout
        layout = QVBoxLayout()

        # Label to Display the Remaining Time
        self.time_Display = QLabel()
        self.time_Display.setAlignment(Qt.AlignCenter)  # Center the text
        layout.addWidget(self.time_Display)

        # Button to Start the Timer
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_timer)  # Connect to start_timer method
        layout.addWidget(self.start_button)

        # Button to Skip the Current Duration
        self.skip_button = QPushButton('Skip')
        self.skip_button.clicked.connect(self.skip_duration)  # Connect to skip_duration method
        layout.addWidget(self.skip_button)

        # Input Fields to Customize Durations
        self.work_input = QLineEdit()
        self.work_input.setPlaceholderText('Work Duration (minutes)')  # Placeholder text
        layout.addWidget(self.work_input)

        self.break_input = QLineEdit()
        self.break_input.setPlaceholderText('Short Break Duration (minutes)')
        layout.addWidget(self.break_input)

        self.long_break_input = QLineEdit()
        self.long_break_input.setPlaceholderText('Long Break Duration (minutes)')
        layout.addWidget(self.long_break_input)

        # Set Widget Layout
        self.setLayout(layout)
        self.setWindowTitle('Pomodoro Timer')  # Set the Window Title
        self.show()

    def start_timer(self):
        try:
            # Convert Input Durations from minutes to seconds
            self.work_duration = int(self.work_input.text()) * 60
            self.break_duration = int(self.break_input.text()) * 60
            self.long_break_duration = int(self.long_break_input.text()) * 60
        except ValueError:
            # Show an Error Message if the input is invalid
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numbers for durations.')
            return

        self.current_mode = 'work'  # Start w/Work Mode
        self.remaining_time = self.work_duration  # Set Initial Duration
        self.update_time_Display()  # Update the Display
        self.timer.start(1000)  # Start the Timer w/1-second Intervals

    def update_time(self):
        self.remaining_time -= 1  # Decrement the Remaining time by 1 second
        if self.remaining_time <= 0:
            self.timer.stop()  # Stop the timer if duration is over
            if self.current_mode == 'work':
                self.current_mode = 'break'  # Switch to break mode
                self.remaining_time = self.break_duration
                QMessageBox.information(self, 'Break Time', 'Time for a short break!')
            elif self.current_mode == 'break':
                self.current_mode = 'work'  # Switch back to work mode
                self.remaining_time = self.work_duration
                QMessageBox.information(self, 'Work Time', 'Back to work!')
            self.update_time_Display()  # Update the Display with new duration
            self.timer.start(1000)  # Restart the timer
        else:
            self.update_time_Display()  # Update the Display with the Remaining time

    def update_time_Display(self):
        # Format the Remaining Time into minutes and seconds
        minutes, seconds = divmod(self.remaining_time, 60)
        self.time_Display.setText(f'{minutes:02}:{seconds:02}')  # Update the Display

    def skip_duration(self):
        # Immediately End the Current Duration
        self.remaining_time = 0
        self.update_time()  # Update the Display to reflect the skipped duration

def main():
    app = QApplication(sys.argv)  # Create a QApplication instance
    timer = PomodoroTimer()  # Create an instance of the PomodoroTimer
    sys.exit(app.exec())  # Start the event loop and exit when done

if __name__ == "__main__":
    main()  # Run the App
