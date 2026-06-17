import random
import time
import threading
import sys

WORDS = [
    "shadow", "ember", "crystal", "storm", "python",
    "galaxy", "flame", "echo", "spirit", "quantum",
    "raven", "blaze", "orbit", "nova", "cipher", 
    "phantom", "meteor", "cascade", "vertex", 
    "hollow", "emberlight", "rift", "solstice", 
    "mirage", "vortex", "nebula", "harbor", "pulse", 
    "tundra", "whisper", "emberfall", "glyph", "horizon", 
    "tidal", "cinder", "lunar", "prism", "static", "blizzard", 
    "embercore", "riftstone", "echoes", "drift", "spindle", "quiver"
]

game_over = False
player_score = 0
enemy_score = 0
current_word = ""


def enemy_ai():
    global enemy_score, current_word, game_over
    while not game_over:
        time.sleep(random.uniform(1.5, 3.5))
        if current_word != "":
            enemy_score += 1
            print(f"\nEnemy captured '{current_word}'!")
            current_word = ""


def main():
    global current_word, player_score, enemy_score, game_over

    print("=== TYPE CLASH ===")
    print("Type the word before the enemy captures it.")
    print("Game ends at 10 points.\n")

    # Start enemy thread
    threading.Thread(target=enemy_ai, daemon=True).start()

    while not game_over:
        current_word = random.choice(WORDS)
        print(f"\nWord: {current_word}")

        start = time.time()
        user_input = input("> ").strip()

        if user_input == current_word:
            player_score += 1
            print("You captured it!")
        else:
            print("Missed!")

        current_word = ""

        print(f"Score — You: {player_score} | Enemy: {enemy_score}")

        if player_score >= 10 or enemy_score >= 10:
            game_over = True

    print("\n=== GAME OVER ===")
    if player_score > enemy_score:
        print("You win the duel!")
    else:
        print("The enemy wins this time.")
    print(f"Final Score — You: {player_score} | Enemy: {enemy_score}")


if __name__ == "__main__":
    main()
