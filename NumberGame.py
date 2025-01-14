import os
import json
import random

def center_text(text):
    """Centers text based on terminal width with fallback."""
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        # Fallback width if terminal size cannot be determined
        terminal_width = 220
    return text.center(terminal_width)

def updateStatistics(result):
    with open("Util/GameSettings.json", "r") as file:
        stats = json.load(file)

    if result == 1:
        stats["wins"] += 1
    elif result == 0:
        stats["losses"] += 1

    with open("Util/GameSettings.json", "w") as file:
        json.dump(stats, file)


def gameStart(upperLimit, guessLimit):
    rand = random.randint(1, upperLimit)
    while guessLimit != 0:
        numberGuessed = int(input(center_text(
            "Guess a number: ")))
        if numberGuessed == rand:
            print(center_text(
                "Correct!"))
            updateStatistics(1)
            break
        else:
            print(center_text(
                "Wrong!"))
            guessLimit -= 1
    if guessLimit == 0:
        print(center_text(
            "Unfortunately you have used all guesses without finding the number! Better luck next time."))
        updateStatistics(0)


def printGameSettings(upperLimit, guessLimit):
    print(center_text(
        f"You've chosen a range from 1 to {upperLimit} and set {guessLimit} attempts for this game. Good luck!"))
    gameStart(upperLimit, guessLimit)


def printStatistics():
    with open("Util/GameSettings.json", "r") as file:
        stats = json.load(file)

    print(center_text(
        f"Wins: {stats['wins']}"))
    print(center_text(
        f"Losses: {stats['losses']}"))

def menuScreen():
    while True:
        try:
            print(center_text("Welcome to the Number Guessing Game!"))
            choice = input(center_text("Would you like to play,see stats or quit? (Enter 'play', 'stats' or 'quit'): ")).strip().lower()

            if choice == "quit":
                print(center_text("Thanks for visiting! Goodbye!"))
                break
            elif choice == "stats":
                with open("Util/GameSettings.json", "r") as file:
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
                    difficulty = int(
                        input(center_text("1. Easy (10 chances) "
                                          "2. Medium (5 chances) "
                                          "3. Hard (3 chances) ")))
                    guessLimit = 10 if difficulty == 1 else 5 if difficulty == 2 else 3
                    printGameSettings(upperLimit, guessLimit)
                else:
                    print(center_text("Invalid option. Please try again."))
            else:
                print(center_text("Invalid input. Please enter 'play' or 'quit'."))
        except KeyboardInterrupt:
            break


def main():
    # Call the menuScreen function
    menuScreen()


def initalizeData():
    if not os.path.exists("Util/GameSettings.json"):
        data = {"wins": 0, "losses": 0}
        with open("Util/GameSettings.json", "w") as file:
            json.dump(data, file)


if __name__ == "__main__":
    initalizeData()
    main()
