import random
import sys
import time

def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.01)
    print()

def room_event():
    events = [
        "monster",
        "treasure",
        "trap",
        "empty",
        "healer"
    ]
    return random.choice(events)

def play():
    hp = 10
    gold = 0
    rooms = 0

    slow("=== DUNGEON ESCAPE LITE ===")
    slow("Find treasure, avoid traps, and survive.\n")

    while hp > 0:
        rooms += 1
        slow(f"\nYou enter room {rooms}...")
        event = room_event()

        if event == "monster":
            slow("A monster attacks!")
            dmg = random.randint(1, 4)
            hp -= dmg
            slow(f"You fight it off but lose {dmg} HP.")
        
        elif event == "treasure":
            gain = random.randint(2, 6)
            gold += gain
            slow(f"You find a treasure chest with {gain} gold!")
        
        elif event == "trap":
            slow("A hidden trap snaps!")
            dmg = random.randint(1, 5)
            hp -= dmg
            slow(f"You take {dmg} damage.")
        
        elif event == "healer":
            heal = random.randint(2, 5)
            hp += heal
            slow(f"A wandering healer restores {heal} HP.")
        
        else:
            slow("The room is empty. You catch your breath.")

        slow(f"HP: {hp} | Gold: {gold}")

        if hp <= 0:
            break

        choice = input("Continue deeper? (y/n): ").strip().lower()
        if choice != "y":
            break

    slow("\n=== GAME OVER ===")
    slow(f"You reached room {rooms} and collected {gold} gold.")
    slow("Thanks for playing!")

if __name__ == "__main__":
    play()
