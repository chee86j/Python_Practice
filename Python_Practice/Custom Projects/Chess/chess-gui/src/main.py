import sys
from PyQt6.QtWidgets import QApplication, QDialog
from gui.start_menu import StartMenu
from gui.chess_gui import ChessGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    def show_start_menu():
        start_menu = StartMenu()
        if start_menu.exec() == QDialog.DialogCode.Accepted:
            window = ChessGUI(start_menu.game_mode)
            window.show()
    
    show_start_menu()
    sys.exit(app.exec())
