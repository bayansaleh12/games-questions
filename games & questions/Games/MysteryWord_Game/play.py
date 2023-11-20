import random

print("Welcome to Mystery Word!\n")

words = ["snake", "cherry", "lion", "python", "banana", "cat", "apple", "computer"]


def display_clues(word):
    print("Clues: ")
    print(f"* The word has {len(word)} letters.")
    print(f"* The first letter is '{word[0]}'.")

    types = ["animal", "fruit", "animal", "programming language", "fruit", "animal", "fruit", "electronic device"]
    thisdict = dict(zip(words, types))
    x = thisdict[word]
    print(f"* The word is a type of '{x}'.")


def play_game():
    attempts_left = 5
    word_to_guess = random.choice(words)
    while attempts_left > 0:
        display_clues(word_to_guess)
        print(f"\nAttempts left: {attempts_left}")
        guess = input("\nGuess the word: ").lower()

        if guess == word_to_guess:
            print(f"Congratulations! You guessed the word \"{word_to_guess}\"! Well done!")
            break
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print("\nIncorrect! Try again.")
            else:
                print(f"\nSorry, you're out of attempts. The correct word was \"{word_to_guess}\".")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == "yes"


def main():
    while play_game():
        pass

    print("\nThanks for playing Mystery Word! Goodbye.")


if __name__ == "__main__":
    main()
