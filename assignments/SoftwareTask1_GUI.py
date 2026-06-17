import random
import os

# True color (RGB) ANSI escape codes for terminal output
GREEN = "\033[38;2;0;255;0m"
RED = "\033[38;2;255;0;0m"
YELLOW = "\033[38;2;255;255;0m"
CYAN = "\033[38;2;0;255;255m"
BLUE = "\033[38;2;0;0;255m"
RESET = "\033[0m"

# Use os module to construct the file path safely
HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscore.txt")

def load_highscore():
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            line = f.read().strip()
            if line:
                name, score, difficulty = line.split(",")
                return name, int(score), difficulty
    except FileNotFoundError:
        return None
    return None

def save_highscore(name, score, difficulty):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(f"{name},{score},{difficulty}")

def choose_difficulty():
    print(f"\n{CYAN}Choose difficulty:{RESET}")
    print(f"{YELLOW}1. Easy   (1–10, 5 attempts){RESET}")
    print(f"{YELLOW}2. Medium (1–50, 7 attempts){RESET}")
    print(f"{YELLOW}3. Hard   (1–100, 10 attempts){RESET}")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return 1, 10, 5, "Easy"
        elif choice == "2":
            return 1, 50, 7, "Medium"
        elif choice == "3":
            return 1, 100, 10, "Hard"
        else:
            print("Invalid choice. Try again.")

def play_game(player_name):
    low, high, attempts, difficulty = choose_difficulty()
    secret = random.randint(low, high)
    score = 100

    print(f"\n{BLUE}I'm thinking of a number between {low} and {high}.{RESET}")
    print(f"{BLUE}You have {attempts} attempts.{RESET}\n")

    for attempt in range(1, attempts + 1):
        guess = input(f"{CYAN}Attempt {attempt}: Enter your guess: {RESET}")

        if not guess.isdigit():
            print(f"{RED}Please enter a number.{RESET}")
            continue

        guess = int(guess)

        if guess == secret:
            print(f"{GREEN}Correct! You guessed the number!{RESET}")
            print(f"{GREEN}Your score: {score}{RESET}")
            return score, difficulty

        elif guess < secret:
            print(f"{YELLOW}Too low!{RESET}")
        else:
            print(f"{YELLOW}Too high!{RESET}")

        score -= 10

    print(f"\n{RED}You ran out of attempts! The number was {secret}.{RESET}")
    print(f"{RED}Your score: 0{RESET}")
    return 0, difficulty

def main():
    print(f"{GREEN}=== NUMBER GUESSING GAME ==={RESET}")
    player_name = input(f"{CYAN}Enter your name: {RESET}")

    highscore = load_highscore()
    if highscore:
        print(f"\n{BLUE}Current High Score: {highscore[0]} - {highscore[1]} ({highscore[2]}){RESET}")

    while True:
        score, difficulty = play_game(player_name)

        if not highscore or score > highscore[1]:
            print(f"\n{GREEN}New High Score!{RESET}")
            save_highscore(player_name, score, difficulty)
            highscore = (player_name, score, difficulty)

        again = input(f"\n{CYAN}Play again? (y/n): {RESET}").lower()
        if again != "y":
            print(f"{CYAN}Thanks for playing!{RESET}")
            break

if __name__ == "__main__":
    main()
