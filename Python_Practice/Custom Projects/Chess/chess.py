import pygame
import chess
import chess.svg
import chess.engine
import io
import pickle
from cairosvg import svg2png

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Load SVG as image using cairosvg and BytesIO
def render_chessboard(board):
    svg_code = chess.svg.board(board, size=WIDTH)
    png_data = io.BytesIO()
    svg2png(bytestring=svg_code.encode('utf-8'), write_to=png_data)
    png_data.seek(0)
    board_img = pygame.image.load(png_data)
    return pygame.transform.scale(board_img, (WIDTH, HEIGHT))

# Save Game Function using Pickle to serialize the board object
def save_game(board):
    with open("saved_game.pkl", "wb") as f:
        pickle.dump(board, f)

# Load Game Function
def load_game():
    try:
        with open("saved_game.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return chess.Board()

# Start Menu Function to choose between AI and PvP (on the same device)
def start_menu():
    font = pygame.font.Font(None, 74)
    running = True
    while running:
        WIN.fill(WHITE)
        title_text = font.render("Chess Game", True, BLACK)
        play_ai_text = font.render("Play AI", True, BLACK)
        play_pvp_text = font.render("Play PvP", True, BLACK)
        load_game_text = font.render("Load Saved Game", True, BLACK)
        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        WIN.blit(play_ai_text, (WIDTH // 2 - play_ai_text.get_width() // 2, HEIGHT // 2 - 100))
        WIN.blit(play_pvp_text, (WIDTH // 2 - play_pvp_text.get_width() // 2, HEIGHT // 2))
        WIN.blit(load_game_text, (WIDTH // 2 - load_game_text.get_width() // 2, HEIGHT // 2 + 100))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play_ai_text.get_rect(topleft=(WIDTH // 2 - play_ai_text.get_width() // 2, HEIGHT // 2 - 100)).collidepoint(pos):
                    return "ai"
                elif play_pvp_text.get_rect(topleft=(WIDTH // 2 - play_pvp_text.get_width() // 2, HEIGHT // 2)).collidepoint(pos):
                    return "pvp"
                elif load_game_text.get_rect(topleft=(WIDTH // 2 - load_game_text.get_width() // 2, HEIGHT // 2 + 100)).collidepoint(pos):
                    return "load"

# Game Over Screen Function w/ Restart, Main Menu Options, Save / Load Game
def game_over_screen(result):
    font = pygame.font.Font(None, 74)
    running = True
    while running:
        WIN.fill(WHITE)
        result_text = font.render(result, True, BLACK)
        restart_text = font.render("Restart", True, BLACK)
        main_menu_text = font.render("Main Menu", True, BLACK)
        WIN.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 4))
        WIN.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 - 50))
        WIN.blit(main_menu_text, (WIDTH // 2 - main_menu_text.get_width() // 2, HEIGHT // 2 + 50))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_text.get_rect(topleft=(WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 - 50)).collidepoint(pos):
                    return "restart"
                elif main_menu_text.get_rect(topleft=(WIDTH // 2 - main_menu_text.get_width() // 2, HEIGHT // 2 + 50)).collidepoint(pos):
                    return "main_menu"

# Main Game Function
def main():
    while True:
        clock = pygame.time.Clock()
        player_mode = start_menu()

        # Load game if selected
        if player_mode == "load":
            board = load_game()
            player_mode = "ai"  # Assume AI mode for loaded games
        else:
            board = chess.Board()

        selected_square = None
        running = True

        # Set up chess engine if playing against AI
        engine = None
        if player_mode == "ai":
            engine = chess.engine.SimpleEngine.popen_uci("stockfish")
        
        while running:
            clock.tick(FPS)
            
            # Draw board
            WIN.fill(WHITE)
            board_img = render_chessboard(board)
            WIN.blit(board_img, (0, 0))

            # Draw Save Game button
            font = pygame.font.Font(None, 50)
            save_game_text = font.render("Save Game", True, BLACK)
            WIN.blit(save_game_text, (10, HEIGHT - 60))
            pygame.display.update()
            
            # Check for game over
            if board.is_game_over():
                result = "Draw"
                if board.is_checkmate():
                    result = "Black Wins" if board.turn == chess.WHITE else "White Wins"
                if engine:
                    engine.quit()
                action = game_over_screen(result)
                if action == "restart":
                    break
                elif action == "main_menu":
                    return
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # Save game button click
                    if save_game_text.get_rect(topleft=(10, HEIGHT - 60)).collidepoint(pos):
                        save_game(board)
                    else:
                        row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
                        square = chess.square(col, 7 - row) if board.turn == chess.WHITE else chess.square(7 - col, row)
                        if selected_square is None:
                            if board.piece_at(square) and board.piece_at(square).color == board.turn:
                                selected_square = square
                        else:
                            move = chess.Move(selected_square, square)
                            if move in board.legal_moves:
                                board.push(move)
                                selected_square = None
                                # AI makes a move after player if in AI mode
                                if player_mode == "ai" and not board.is_game_over() and board.turn == chess.BLACK:
                                    result = engine.play(board, chess.engine.Limit(time=1.0))
                                    board.push(result.move)
                            else:
                                selected_square = None

        if engine:
            engine.quit()
        pygame.quit()

if __name__ == "__main__":
    main()
    
#   To run the code, you need to have the following libraries installed by running the following commands:
#   `pip install pygame chess cairosvg`

#   Be sure to have the Stockfish chess engine installed on your system. 
#   You can download it from the official website: https://stockfishchess.org/download/
#   Once you have Stockfish downloaded, make sure to either add the path to your system's 
#   PATH variable or modify the script to point to the Stockfish executable's full path.

#   The code initializes a chess board using the python-chess library and renders it using the cairosvg library.
#   The chess board is displayed using the pygame library. The user can click on a piece to select it and then click on a square to move it.
#   The game starts with a menu allowing the player to choose between playing against an AI, playing against another player locally, or loading a saved ai game.
#   In AI mode, the Stockfish chess engine makes moves for the opponent.
#   During gameplay, the player can click the "Save Game" button to save the current state.
#   After a game ends, a game-over screen appears, giving the player options to restart or return to the main menu.

#   To execute the script, run the following command in the terminal:
#   `python chess.py`
