import random
import os
import re

# ANSI color codes for colorful terminal output
GREEN = "\033[38;2;0;255;0m"     # Green text color
RED = "\033[38;2;255;0;0m"       # Red text color
YELLOW = "\033[38;2;255;255;0m"  # Yellow text color
CYAN = "\033[38;2;0;255;255m"    # Cyan text color
BLUE = "\033[38;2;0;0;255m"      # Blue text color
MAGENTA = "\033[38;2;255;0;255m" # Magenta text color
RESET = "\033[0m"                # Reset to default color

# Path to the highscore file stored in the same directory as this script
HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscore.txt")


def strip_ansi(text):
    """
    Removes hidden color codes from text so we can measure its real length.
    """
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def box_line(content, width=39):
    """
    Creates a pretty line for a box by centering text between left and right borders.
    """
    clean_content = strip_ansi(content)
    total_padding = width - len(clean_content)
    left_pad = total_padding // 2
    right_pad = total_padding - left_pad
    return f"{GREEN}║{RESET}{' ' * left_pad}{content}{' ' * right_pad}{GREEN}║{RESET}"

def clear_screen():
    """Clears the screen to show a fresh display."""
    os.system('clear')

def print_centered(text, color=RESET):
    """Prints text in the middle of the screen."""
    print(f"{color}{text.center(80)}{RESET}")

def print_separator():
    """Prints a decorative line across the screen."""
    print(f"{CYAN}{'─' * 80}{RESET}")


def load_highscores():
    """
    Reads the high scores from a file and returns the top 5 best scores.
    """
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            lines = f.read().strip().split("\n")
            scores = []
            for line in lines:
                if line:
                    name, score, difficulty = line.split(",")
                    scores.append((name, int(score), difficulty))
            scores.sort(key=lambda x: x[1], reverse=True)
            return scores[:5]
    except FileNotFoundError:
        return []

def save_highscore(name, score, difficulty):
    """
    Saves a new score to the file and keeps only the best 5 scores.
    """
    scores = load_highscores()
    scores.append((name, score, difficulty))
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:5]
    with open(HIGHSCORE_FILE, "w") as f:
        for entry in scores:
            f.write(f"{entry[0]},{entry[1]},{entry[2]}\n")


def show_title_screen():
    """
    Shows the game's welcome screen with the title and instructions.
    """
    clear_screen()
    print()
    print(f"{GREEN}╔═══════════════════════════════════════╗{RESET}")
    print(box_line(f"{MAGENTA}✦ NUMBER GUESSING GAME ✦{RESET}"))
    print(f"{GREEN}╚═══════════════════════════════════════╝{RESET}")
    print()
    print_centered("Guess the mystery number!", YELLOW)
    print_centered("Test your luck and intuition!", CYAN)
    print()

def choose_difficulty():
    """
    Asks the player to pick a difficulty level and returns the game settings.
    """
    print_separator()
    print_centered("SELECT DIFFICULTY", CYAN)
    print_separator()
    print()
    print(f"{YELLOW}  1. Easy   {RESET}(1–10, 5 attempts)")
    print(f"{YELLOW}  2. Medium {RESET}(1–50, 7 attempts)")
    print(f"{YELLOW}  3. Hard   {RESET}(1–100, 10 attempts)")
    print()

    while True:
        choice = input(f"{CYAN}Enter 1, 2, or 3: {RESET}")
        if choice == "1":
            return 1, 10, 5, "Easy"
        elif choice == "2":
            return 1, 50, 7, "Medium"
        elif choice == "3":
            return 1, 100, 10, "Hard"
        else:
            print(f"{RED}Invalid choice. Try again.{RESET}")



def play_game(player_name):
    """
    Runs one round of the guessing game and returns the player's score.
    """
    low, high, attempts, difficulty = choose_difficulty()
    secret = random.randint(low, high)
    score = 100

    print()
    print_centered(f"🎮 {player_name}'s Turn!", MAGENTA)
    print_separator()
    print(f"{BLUE}I'm thinking of a number between {low} and {high}.{RESET}")
    print(f"{BLUE}You have {attempts} attempts.{RESET}\n")

    for attempt in range(1, attempts + 1):
        guess = input(f"{CYAN}[Attempt {attempt}/{attempts}] Enter your guess: {RESET}")
        if not guess.isdigit():
            print(f"{RED}Please enter a number.{RESET}")
            continue

        guess = int(guess)
        
        if guess < low or guess > high:
            print(f"{RED}Please enter a number between {low} and {high}.{RESET}")
            continue

        if guess == secret:
            print(f"{GREEN}✓ Correct! You guessed the number!{RESET}")
            print(f"{GREEN}Your score: {score}{RESET}")
            return score, difficulty
        elif guess < secret:
            print(f"{YELLOW}↑ Too low!{RESET}")
        else:
            print(f"{YELLOW}↓ Too high!{RESET}")

        score -= 10
        print()

    print(f"\n{RED}✗ You ran out of attempts! The number was {secret}.{RESET}")
    print(f"{RED}Your score: 0{RESET}")
    return 0, difficulty


def main():
    """
    Runs the whole game from start to finish.
    """
    show_title_screen()
    
    highscores = load_highscores()
    if highscores:
        print_separator()
        print_centered("TOP 5 HIGH SCORES", MAGENTA)
        print_separator()
        for i, (name, score, difficulty) in enumerate(highscores, 1):
            print(f"  {GREEN}{i}. {name:<20} {score:>5} points ({difficulty}){RESET}")
        print()
    
    player_name = input(f"{CYAN}Enter your name: {RESET}")
    print()

    while True:
        score, difficulty = play_game(player_name)

        if len(highscores) < 5 or score > highscores[-1][1]:
            print(f"\n{GREEN}🏆 New High Score! 🏆{RESET}")
            save_highscore(player_name, score, difficulty)
            highscores = load_highscores()

        again = input(f"\n{CYAN}Play again? (y/n): {RESET}").lower()
        if again != "y":
            print_separator()
            print_centered("Thanks for playing! Goodbye!", GREEN)
            print_separator()
            break


if __name__ == "__main__":
    main()
