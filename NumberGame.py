import os


def center_text(text):
    """Centers text based on terminal width with fallback."""
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        # Fallback width if terminal size cannot be determined
        terminal_width = 220
    return text.center(terminal_width)

def gameStart(upperLimit, guessLimit):
    print("TODO")

def printGameSettings(upperLimit, guessLimit):
    print(center_text(
        f"You've chosen a range from 1 to {upperLimit} and set {guessLimit} attempts for this game. Good luck!"))
    gameStart(upperLimit, guessLimit)


def menuScreen():
    while True:
        print(center_text("Welcome to the Number Guessing Game!"))
        choice = input(center_text("Would you like to play or quit? (Enter 'play' or 'quit'): ")).strip().lower()

        if choice == "quit":
            print(center_text("Thanks for visiting! Goodbye!"))
            break
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


def main():
    # Call the menuScreen function
    menuScreen()


# Entry point of the program
if __name__ == "__main__":
    main()
