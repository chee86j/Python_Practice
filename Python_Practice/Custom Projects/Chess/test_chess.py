# Backend Logic test cases for core functionality like saving/loading games, 
# board state, & game flow logic. 

import pytest
import chess
from chess_game_ui import save_game, load_game, start_menu, game_over_screen

# Test saving & loading the game
def test_save_and_load_game():
    # Create a board & make some moves
    board = chess.Board()
    board.push(chess.Move.from_uci("e2e4"))
    board.push(chess.Move.from_uci("e7e5"))

    # Save the game
    save_game(board)

    # Load the game
    loaded_board = load_game()

    # Assert that the loaded board matches the saved board
    assert board.fen() == loaded_board.fen()

# Test loading an empty save file
def test_load_game_no_save():
    try:
        loaded_board = load_game()
        assert isinstance(loaded_board, chess.Board)
    except FileNotFoundError:
        pytest.fail("The saved game file does not exist, but should be handled gracefully.")

# Test initial board state
def test_initial_board():
    board = chess.Board()
    assert board.is_checkmate() == False
    assert board.is_stalemate() == False
    assert board.is_insufficient_material() == False
    assert board.turn == chess.WHITE

# Test game over logic
def test_game_over():
    board = chess.Board()
    # Set up a board state that ends in a checkmate
    moves = [
        "f2f3", "e7e5", "g2g4", "d8h4"
    ]
    for move in moves:
        board.push(chess.Move.from_uci(move))

    # The game should now be in a checkmate
    assert board.is_checkmate() == True
    assert board.is_game_over() == True

# Test start menu response types
def test_start_menu():
    # Since start_menu() depends on Pygame user input, mock its return value
    assert callable(start_menu)

# Test game over screen functionality
def test_game_over_screen():
    # Similar to start_menu, we can't directly test Pygame UI here, but we ensure the function exists & is callable
    assert callable(game_over_screen)


# Steps to Run the Test:
# Go to the directory `cd Python_Practice/Custom%20Projects/Chess``
# Install dependencies by running `pip install pytest pygame chess cairosvg``
# Run in the terminal `pytest test_chess.py` or `python -m pytest test_chess.py` if the first command doesn't work.

# Note test are run on the backend logic of the chess game, not the UI due to
# the complexity of testing UI with Pygame. The tests cover core functionality
# like saving/loading games, board state, & game flow logic. The tests ensure
# that the game behaves correctly under different conditions & that the core
# logic is functioning as expected. The tests help identify bugs & issues in
# the game logic & ensure that the game is stable & reliable. 