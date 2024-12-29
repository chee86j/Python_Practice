import pytest
from PyQt6.QtWidgets import QApplication
from tictactoe import TicTacToe

@pytest.fixture(scope="module")
def app():
    return QApplication([])  # Create a QApplication instance

@pytest.fixture
def game_window():
    return TicTacToe()  # Create a new TicTacToe instance for each test

def test_initial_setup(game_window):
    # Test initial setup of the game
    assert game_window.current_player == "X"
    assert game_window.is_human_turn is True
    assert len(game_window.buttons) == 3
    assert all(len(row) == 3 for row in game_window.buttons)

    # Ensure all buttons are empty at the start
    for row in game_window.buttons:
        for button in row:
            assert button.text() == " "

def test_human_move(game_window):
    # Simulate a human move
    game_window.on_button_clicked(0, 0)
    assert game_window.buttons[0][0].text() == "X"
    assert game_window.current_player == "O"

def test_ai_move(game_window):
    # Simulate a human move followed by AI move
    game_window.on_button_clicked(0, 0)  # Human move
    assert game_window.buttons[0][0].text() == "X"

    game_window.ai_move()  # AI makes a move
    ai_moved = any(button.text() == "O" for row in game_window.buttons for button in row)
    assert ai_moved is True

def test_winner_check(game_window):
    # Simulate a winning move for "X"
    game_window.buttons[0][0].setText("X")
    game_window.buttons[0][1].setText("X")
    game_window.buttons[0][2].setText("X")
    assert game_window.check_winner() is True

def test_draw(game_window):
    # Simulate a draw
    moves = ["X", "O", "X", "X", "X", "O", "O", "X", "O"]
    for i in range(3):
        for j in range(3):
            game_window.buttons[i][j].setText(moves.pop(0))
    assert game_window.is_draw() is True
    assert game_window.check_winner() is False

def test_restart_game(game_window):
    # Simulate a game and restart
    game_window.buttons[0][0].setText("X")
    game_window.buttons[1][1].setText("O")
    game_window.restart_game()

    # Check if all buttons are reset
    for row in game_window.buttons:
        for button in row:
            assert button.text() == " "
            assert button.isEnabled() is True

    assert game_window.current_player == "X"
    assert game_window.is_human_turn is True

def test_score_update(game_window):
    # Simulate a win for "X"
    game_window.buttons[0][0].setText("X")
    game_window.buttons[0][1].setText("X")
    game_window.buttons[0][2].setText("X")
    game_window.check_game_over()

    assert game_window.scores["Human"] == 1
    assert game_window.score_label.text() == "Human: 1, AI: 0"

def test_ai_blocking(game_window):
    # Simulate a scenario where AI needs to block
    game_window.buttons[0][0].setText("X")
    game_window.buttons[0][1].setText("X")
    x, y = game_window.find_best_move()

    # AI should block the winning move
    assert (x, y) == (0, 2)

def test_ai_center_preference(game_window):
    # Reset and test AI's center preference
    game_window.restart_game()
    x, y = game_window.find_best_move()

    # AI should pick the center initially
    assert (x, y) == (1, 1)
