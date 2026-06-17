import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)


def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def random_food_position():
    x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return x, y


def main():
    # Initial snake
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (BLOCK_SIZE, 0)  # moving right
    food = random_food_position()
    score = 0
    game_over = False

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction[1] == 0:
                    direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and direction[1] == 0:
                    direction = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and direction[0] == 0:
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction[0] == 0:
                    direction = (BLOCK_SIZE, 0)
                elif event.key == pygame.K_r and game_over:
                    # Restart game
                    return main()

        if not game_over:
            # Move snake
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # Check collisions with walls
            if (
                new_head[0] < 0
                or new_head[0] >= WIDTH
                or new_head[1] < 0
                or new_head[1] >= HEIGHT
            ):
                game_over = True

            # Check collisions with self
            if new_head in snake:
                game_over = True

            snake.insert(0, new_head)

            # Check food collision
            if new_head == food:
                score += 1
                food = random_food_position()
            else:
                snake.pop()

        # Drawing
        screen.fill(BLACK)

        # Draw snake
        for segment in snake:
            pygame.draw.rect(
                screen,
                GREEN,
                (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE),
            )

        # Draw food
        pygame.draw.rect(
            screen,
            RED,
            (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE),
        )

        # Draw score
        draw_text(f"Score: {score}", WHITE, 10, 10)

        if game_over:
            draw_text("Game Over! Press R to restart", WHITE, WIDTH // 2 - 150, HEIGHT // 2)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
