import unittest
from PyQt6.QtWidgets import QApplication
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the QApplication for testing
        cls.app = QApplication([])

    def setUp(self):
        # Create a new game window for each test
        self.game_window = TicTacToe()

    def test_initial_setup(self):
        # Test initial game setup
        self.assertEqual(self.game_window.current_player, "X")
        for row in self.game_window.buttons:
            for button in row:
                self.assertEqual(button.text(), " ")

    def test_human_move(self):
        # Simulate a human move
        self.game_window.on_button_clicked(0, 0)
        self.assertEqual(self.game_window.buttons[0][0].text(), "X")
        self.assertEqual(self.game_window.current_player, "O")
        self.assertFalse(self.game_window.is_human_turn)

    def test_ai_move(self):
        # Simulate a human move followed by an AI move
        self.game_window.on_button_clicked(0, 0)
        ai_move = [(i, j) for i in range(3) for j in range(3) if self.game_window.buttons[i][j].text() == "O"]
        self.assertEqual(len(ai_move), 1)  # Ensure AI made one move

    def test_winner_check(self):
        # Simulate a winning move for "X"
        self.game_window.buttons[0][0].setText("X")
        self.game_window.buttons[0][1].setText("X")
        self.game_window.buttons[0][2].setText("X")
        self.assertTrue(self.game_window.check_winner())
        self.assertEqual(self.game_window.scores["Human"], 1)

    def test_draw(self):
        # Simulate a draw scenario
        moves = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        for i in range(3):
            for j in range(3):
                self.game_window.buttons[i][j].setText(moves.pop(0))
        self.assertTrue(self.game_window.is_draw())
        self.assertFalse(self.game_window.check_winner())

    def test_restart_game(self):
        # Simulate restarting the game
        self.game_window.buttons[0][0].setText("X")
        self.game_window.restart_game()
        for row in self.game_window.buttons:
            for button in row:
                self.assertEqual(button.text(), " ")
                self.assertTrue(button.isEnabled())
        self.assertEqual(self.game_window.current_player, "X")
        self.assertTrue(self.game_window.is_human_turn)

    def test_score_update(self):
        # Simulate a win for "X"
        self.game_window.buttons[0][0].setText("X")
        self.game_window.buttons[0][1].setText("X")
        self.game_window.buttons[0][2].setText("X")
        self.game_window.check_game_over()
        self.assertEqual(self.game_window.scores["Human"], 1)
        self.assertEqual(self.game_window.score_label.text(), "Human: 1, AI: 0")

    def test_ai_blocking(self):
        # Simulate a scenario where AI needs to block
        self.game_window.buttons[0][0].setText("X")
        self.game_window.buttons[0][1].setText("X")
        x, y = self.game_window.find_best_move()
        self.assertEqual((x, y), (0, 2))  # AI should block the winning move

    def test_ai_center_preference(self):
        # Test AI's center preference
        self.game_window.restart_game()
        x, y = self.game_window.find_best_move()
        self.assertEqual((x, y), (1, 1))  # AI should pick the center if available

    @classmethod
    def tearDownClass(cls):
        cls.app.exit()

if __name__ == "__main__":
    unittest.main()
