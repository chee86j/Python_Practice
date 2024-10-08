import pygame
import chess
import chess.svg
import chess.engine
import io
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

# Main Game Function
def main():
    clock = pygame.time.Clock()
    board = chess.Board()
    selected_square = None
    running = True

    # Set up Stockfish chess engine for AI
    engine = chess.engine.SimpleEngine.popen_uci("/path/to/stockfish") # Remember to replace w/ Stockfish executable path
    
    while running:
        clock.tick(FPS)
        
        # Draw board
        WIN.fill(WHITE)
        board_img = render_chessboard(board)
        WIN.blit(board_img, (0, 0))
        pygame.display.update()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
                square = chess.square(col, 7 - row)
                if selected_square is None:
                    if board.piece_at(square) and board.piece_at(square).color == board.turn:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        # AI makes a move immediately after player's move
                        if not board.is_game_over():
                            result = engine.play(board, chess.engine.Limit(time=1.0))
                            board.push(result.move)
                    selected_square = None
    
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
#   Future features: AI opponents, move validation, and checkmate detection.

#   To execute the script, run the following command in the terminal:
#   `python chess.py`