import pygame
import random
import sys

# Setup
pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Player settings
player_size = 40
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Block settings
block_size = 40
block_speed = 10
blocks = []

score = 0


def spawn_block():
    x = random.randint(0, WIDTH - block_size)
    y = -block_size
    blocks.append([x, y])


def draw_player():
    pygame.draw.rect(screen, (0, 200, 0), (player_x, player_y, player_size, player_size))


def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, (200, 0, 0), (block[0], block[1], block_size, block_size))


def draw_score():
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))


def main():
    global player_x, score

    spawn_timer = 0
    running = True

    while running:
        clock.tick(60)
        screen.fill((20, 20, 20))

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        # Spawn blocks
        spawn_timer += 1
        if spawn_timer > 30:
            spawn_block()
            spawn_timer = 0

        # Move blocks
        for block in blocks:
            block[1] += block_speed

        # Collision detection
        for block in blocks:
            if (
                player_x < block[0] + block_size
                and player_x + player_size > block[0]
                and player_y < block[1] + block_size
                and player_y + player_size > block[1]
            ):
                running = False

        # Remove off‑screen blocks & update score
        blocks[:] = [b for b in blocks if b[1] < HEIGHT]
        score += 1

        # Draw everything
        draw_player()
        draw_blocks()
        draw_score()

        pygame.display.flip()

    # Game over screen
    screen.fill((0, 0, 0))
    text = font.render("Game Over! Press R to restart", True, (255, 255, 255))
    screen.blit(text, (40, HEIGHT // 2))
    pygame.display.flip()

    # Restart loop
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                blocks.clear()
                score = 0
                main()


if __name__ == "__main__":
    main()
