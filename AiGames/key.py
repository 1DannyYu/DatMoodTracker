import random
import time
import sys

def play():
    score = 0
    delay = 1.5  # starting time allowed per round

    print("=== CATCH THE DOT ===")
    print("Press the matching key before time runs out!")
    print("Game speeds up every round.\n")

    while True:
        target = random.choice("asdfjkl;")
        print(f"Press: {target}")

        start = time.time()
        user_input = ""

        # Read a single character without Enter (Windows & Unix)
        try:
            import msvcrt
            while True:
                if msvcrt.kbhit():
                    user_input = msvcrt.getwch()
                    break
                if time.time() - start > delay:
                    break
        except ImportError:
            import sys, termios, tty, select
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setraw(fd)
            try:
                r, _, _ = select.select([sys.stdin], [], [], delay)
                if r:
                    user_input = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if user_input == target:
            score += 1
            delay *= 0.92  # speed up
            print(f"Good! Score: {score}\n")
        else:
            print("\nMissed!")
            print(f"Final Score: {score}")
            break


if __name__ == "__main__":
    play()
