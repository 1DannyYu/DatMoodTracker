import pygame
import random
import sys

# --- CONFIG ---
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 15, 15
MINES = 30
CELL_SIZE = WIDTH // COLS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
font = pygame.font.SysFont(None, 32)

# Colors
GRAY = (180, 180, 180)
DARK_GRAY = (120, 120, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)


class Cell:
    def __init__(self):
        self.mine = False
        self.revealed = False
        self.flagged = False
        self.number = 0


def create_board():
    board = [[Cell() for _ in range(COLS)] for _ in range(ROWS)]

    # Place mines
    mines_placed = 0
    while mines_placed < MINES:
        r = random.randrange(ROWS)
        c = random.randrange(COLS)
        if not board[r][c].mine:
            board[r][c].mine = True
            mines_placed += 1

    # Count numbers
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c].mine:
                continue
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if board[nr][nc].mine:
                            count += 1
            board[r][c].number = count

    return board


def reveal(board, r, c):
    if board[r][c].revealed or board[r][c].flagged:
        return
    board[r][c].revealed = True

    # Flood fill empty cells
    if board[r][c].number == 0 and not board[r][c].mine:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if not board[nr][nc].revealed:
                        reveal(board, nr, nc)


def draw_board(board):
    for r in range(ROWS):
        for c in range(COLS):
            cell = board[r][c]
            x, y = c * CELL_SIZE, r * CELL_SIZE

            if cell.revealed:
                pygame.draw.rect(screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
                if cell.mine:
                    pygame.draw.circle(screen, RED, (x + CELL_SIZE//2, y + CELL_SIZE//2), CELL_SIZE//4)
                elif cell.number > 0:
                    text = font.render(str(cell.number), True, BLACK)
                    screen.blit(text, (x + CELL_SIZE//3, y + CELL_SIZE//4))
            else:
                pygame.draw.rect(screen, DARK_GRAY, (x, y, CELL_SIZE, CELL_SIZE))
                if cell.flagged:
                    pygame.draw.rect(screen, GREEN, (x + 10, y + 10, CELL_SIZE - 20, CELL_SIZE - 20))

            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)


def check_win(board):
    for r in range(ROWS):
        for c in range(COLS):
            cell = board[r][c]
            if not cell.mine and not cell.revealed:
                return False
    return True


def main():
    board = create_board()
    game_over = False
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                r, c = y // CELL_SIZE, x // CELL_SIZE
                cell = board[r][c]

                if event.button == 1:  # Left click
                    if cell.mine:
                        cell.revealed = True
                        game_over = True
                    else:
                        reveal(board, r, c)

                elif event.button == 3:  # Right click
                    cell.flagged = not cell.flagged

                if check_win(board):
                    win = True
                    game_over = True

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return main()

        screen.fill(WHITE)
        draw_board(board)

        if game_over:
            msg = "You Win!" if win else "Game Over!"
            text = font.render(msg + " Press R to restart.", True, BLACK)
            screen.blit(text, (20, HEIGHT - 40))

        pygame.display.flip()


if __name__ == "__main__":
    main()
