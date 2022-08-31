import os
import dictionary
from artwork import logo, stages


def main():
    word = dictionary.get_word()
    word_length = len(word)

    display = ["_" for iter in range(word_length)]
    is_game_over = False
    lives = len(stages) - 1
    guesses = []

    def show_board():
        print("-" * 40)
        print(stages[lives])
        print(f"{' '.join(display)}\n")
        print(f"Used Letters: {', '.join(guesses)}\n")

    if "HANGMAN_DEBUG" in os.environ:
        separator = "-" * 80
        print(f"{separator}\nChosen Word: {word}\n{separator}\n")

    while not is_game_over:
        show_board()
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Must be a single letters from A to Z\n")
            continue

        elif guess in guesses:
            print("You have already tried that letter.")
            continue

        guesses += guess
        guesses = sorted(guesses)

        if guess in word:
            for idx in range(word_length):
                if word[idx] == guess:
                    display[idx] = guess

            if "_" not in display:
                show_board()
                print(f"You Win!\n")
                is_game_over = True

        else:
            lives -= 1

            if lives == 0:
                show_board()
                print(f"You lose!\nThe word was {word}.\n")
                is_game_over = True

    play_again = input("Would you like to play again? ").lower()
    if play_again == "y":
        main()


if __name__ == "__main__":
    print(logo)
    main()
