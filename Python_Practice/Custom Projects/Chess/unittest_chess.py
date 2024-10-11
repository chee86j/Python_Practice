# Unittests aka PyUnit version for testing the Chess game
import unittest
import chess
from chess_game_ui import save_game, load_game, start_menu, game_over_screen
import os

class TestChessGame(unittest.TestCase):

    def setUp(self):
        # Ensure there's no saved game before each test
        if os.path.exists("saved_game.pkl"):
            os.remove("saved_game.pkl")

    def tearDown(self):
        # Clean up saved game file after each test
        if os.path.exists("saved_game.pkl"):
            os.remove("saved_game.pkl")

    def test_save_and_load_game(self):
        # Create a board & make some moves
        board = chess.Board()
        board.push(chess.Move.from_uci("e2e4"))
        board.push(chess.Move.from_uci("e7e5"))

        # Save the game
        save_game(board)

        # Load the game
        loaded_board = load_game()

        # Assert that the loaded board matches the saved board
        self.assertEqual(board.fen(), loaded_board.fen())

    def test_load_game_no_save(self):
        # Test loading a game when no save file exists
        loaded_board = load_game()
        self.assertIsInstance(loaded_board, chess.Board)

    def test_initial_board(self):
        # Test the initial state of the chess board
        board = chess.Board()
        self.assertFalse(board.is_checkmate())
        self.assertFalse(board.is_stalemate())
        self.assertFalse(board.is_insufficient_material())
        self.assertEqual(board.turn, chess.WHITE)

    def test_game_over(self):
        # Set up a board state that ends in a checkmate
        board = chess.Board()
        moves = [
            "f2f3", "e7e5", "g2g4", "d8h4"
        ]
        for move in moves:
            board.push(chess.Move.from_uci(move))

        # The game should now be in a checkmate
        self.assertTrue(board.is_checkmate())
        self.assertTrue(board.is_game_over())

    def test_start_menu(self):
        # Since start_menu() depends on Pygame user input, we just check if the function is callable
        self.assertTrue(callable(start_menu))

    def test_game_over_screen(self):
        # Similar to start_menu, we can't directly test Pygame UI here, but we ensure the function exists & is callable
        self.assertTrue(callable(game_over_screen))

if __name__ == '__main__':
    unittest.main()

# To run the unit tests, use the following command in your terminal:
# `python unittest_chess_game.py`
# Ensure that the required modules are installed & that the 'chess_game_ui.py' 
# file is in the same directory or in your Python path.