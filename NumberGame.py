import os
import json
import random
import time


def clear_screen():
    #Clears the console screen
    os.system('cls' if os.name == 'nt' else 'clear')


def center_text(text):
    #Centers text based on terminal width with fallback
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        # Fallback width if terminal size cannot be determined
        terminal_width = 220
    return text.center(terminal_width)

def updateStatistics(result):
    #Updates the win/loss statistics in the JSON file
    with open("Util/GameSettings.json", "r") as file:
        stats = json.load(file)

    if result == 1:
        stats["wins"] += 1
    elif result == 0:
        stats["losses"] += 1

    with open("Util/GameSettings.json", "w") as file:
        json.dump(stats, file)


def gameStart(upperLimit, guessLimit):
    #Starts a new game and handles guessing logic
    rand = random.randint(1, upperLimit)
    # Clear the screen before the game starts
    clear_screen()
    print(center_text(f"Welcome to the Number Guessing Game!\n"))
    print(center_text(f"Your goal is to guess a number between 1 and {upperLimit}."))

    while guessLimit > 0:
        print(center_text(f"Attempts left: {guessLimit}"))
        numberGuessed = int(input(center_text("Guess a number: ")))

        if numberGuessed == rand:
            print(center_text("Correct! You've guessed the number."))
            updateStatistics(1)
            break
        else:
            if(numberGuessed > rand):
                print(center_text("Wrong! Pick a smaller number."))
            else:
                print(center_text("Wrong! Pick a larger number."))
            guessLimit -= 1
            # Delay for effect
            time.sleep(1)

    if guessLimit == 0:
        print(center_text("Unfortunately, you've run out of guesses. Better luck next time!"))
        updateStatistics(0)
    # Give user time to read the final message
    time.sleep(2)
    menuScreen()


def printStatistics():
    #Displays the current game statistics (wins/losses)
    with open("Util/GameSettings.json", "r") as file:
        stats = json.load(file)

    clear_screen()
    print(center_text(f"Current Stats"))
    print(center_text(f"-----------------"))
    print(center_text(f"Wins: {stats['wins']}"))
    print(center_text(f"Losses: {stats['losses']}"))
    input(center_text("Press Enter to return to the menu..."))


def menuScreen():
    #Displays the main menu and handles user choices
    while True:
        try:
            clear_screen()
            print(center_text("Welcome to the Number Guessing Game!"))
            choice = input(center_text(
                "Would you like to play, see stats, or quit? (Enter 'play', 'stats', or 'quit'): ")).strip().lower()

            if choice == "quit":
                clear_screen()
                print(center_text("Thanks for visiting! Goodbye!"))
                break
            elif choice == "stats":
                printStatistics()
            elif choice == "play":
                gameType = input(center_text(
                    "Choose a game type: Custom game, predefined game, or quit (Enter 'custom', 'predefined', or 'quit'): ")).strip().lower()

                if gameType == "quit":
                    print(center_text("Thanks for playing! Goodbye!"))
                    break
                elif gameType == "custom":
                    upperLimit = int(
                        input(center_text("Enter the maximum number for the guessing range (starting from 1): ")))
                    guessLimit = int(input(center_text("How many attempts would you like to have? Choose a number: ")))
                    printGameSettings(upperLimit, guessLimit)
                elif gameType == "predefined":
                    upperLimit = 100
                    print(center_text("Please select the difficulty level:"))
                    difficulty = int(input(center_text("1. Easy (10 chances) "
                                                       "2. Medium (5 chances) "
                                                       "3. Hard (3 chances) ")))
                    guessLimit = 10 if difficulty == 1 else 5 if difficulty == 2 else 3
                    printGameSettings(upperLimit, guessLimit)
                else:
                    print(center_text("Invalid option. Please try again."))
            else:
                print(center_text("Invalid input. Please enter 'play', 'stats', or 'quit'."))
        except KeyboardInterrupt:
            break


def printGameSettings(upperLimit, guessLimit):
    #Prints game settings and starts the game
    print(center_text(
        f"You've chosen a range from 1 to {upperLimit} and set {guessLimit} attempts for this game. Good luck!"))
    time.sleep(2)
    gameStart(upperLimit, guessLimit)


def initalizeData():
    #Initializes the statistics file if it doesn't exist
    if not os.path.exists("Util/GameSettings.json"):
        data = {"wins": 0, "losses": 0}
        with open("Util/GameSettings.json", "w") as file:
            json.dump(data, file)


def main():
    #Main entry point of the game
    menuScreen()


if __name__ == "__main__":
    initalizeData()
    main()
