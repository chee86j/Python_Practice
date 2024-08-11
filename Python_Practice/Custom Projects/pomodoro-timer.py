import time
import os

def clear_screen():
    # Clear the terminal screen (works on Windows and Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f'{minutes:02}:{seconds:02}'

def countdown_timer(duration):
    # Countdown timer function
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        clear_screen()
        print(f'Time Remaining: {format_time(remaining_time)}')
        time.sleep(1)
    clear_screen()
    print('Time’s up!')

def pomodoro_timer():
    work_duration = 25 * 60  # 25 minutes in seconds
    break_duration = 5 * 60  # 5 minutes in seconds
    long_break_duration = 15 * 60  # 15 minutes in seconds

    while True:
        print('Starting work session...')
        countdown_timer(work_duration)
        print('Time for a short break...')
        countdown_timer(break_duration)
        
        # After four work sessions, take a long break
        for _ in range(3):  # Example: 3 work sessions
            print('Starting work session...')
            countdown_timer(work_duration)
            print('Time for a short break...')
            countdown_timer(break_duration)
        
        print('Time for a long break...')
        countdown_timer(long_break_duration)

        # Ask the user if they want to start another cycle
        restart = input('Do you want to start another cycle? (Y/N): ').strip().upper()
        if restart != 'Y':
            break

if __name__ == '__main__':
    pomodoro_timer()

# Test the Pomodoro Timer by running the script by navigating to the directory containing the script & running the following command:
# `python3 pomodoro-timer.py` or `python pomodoro-timer.py` depending on the Python version installed on your system.