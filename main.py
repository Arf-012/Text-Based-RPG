import sys
import os
import time
import player.player as Player

screen_width = 100

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def title_screen_selections():
    option = input("> ").lower()
    if option == "play":
        slow_print("Loading game...", 0.05)
        time.sleep(1)
        start_game()
    elif option == "help":
        slow_print("Opening help menu...", 0.05)
        time.sleep(1)
        help_menu()
    elif option == "exit":
        slow_print("Exiting game...", 0.05)
        time.sleep(1)
        sys.exit()
    else:
        slow_print("Invalid option. Please choose from the menu.", 0.03)
        title_screen_selections()

def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * screen_width)
    print("Welcome to the Game!".center(screen_width))
    print("=" * screen_width)
    print("Play".center(screen_width))
    print("Help".center(screen_width))
    print("Exit".center(screen_width))
    print("=" * screen_width)
    title_screen_selections()

def help_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * screen_width)
    print("Help Menu".center(screen_width))
    print("=" * screen_width)
    slow_print("> Use up, down, left, right to move.")
    slow_print("> Type the available commands to do something.")
    slow_print("> Good luck and have fun!")
    time.sleep(2)
    title_screen()

def start_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    slow_print("Starting new game...", 0.05)
    time.sleep(2)
    title_screen()
    
def player_creations():
    os.system('cls' if os.name == 'nt' else 'clear')
    slow_print("Select your character:", 0.05)
    time.sleep(1)
    print()
    title_screen()

if __name__ == "__main__":
    title_screen()
