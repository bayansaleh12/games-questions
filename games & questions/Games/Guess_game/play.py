# name = "morad"
# lower_bound = 5
# txt = f"hello my name is {name} +> {lower_bound}"

# i= 1
# while G_Num != random_Num:
# i += 1
# if G_Num < random_Num : print ("Too low, Try again.")
# elif G_Num > random_Num : print ("Too high, Try again.")
# print (f"Congratulations! You guessed the correct number ({random_Num}) in {i} attempts.")

import random

print("Welcome to the Guess the Number Game!")


def play_game():
    lower_bound = int(input("Enter the lower bound of the range: \t"))
    upper_bound = int(input("Enter the lower bound of the range: \t"))

    random_num = random.randint(int(lower_bound), upper_bound)
    user_number = int(input(f"Guess the number between {lower_bound} and {upper_bound}\t"))

    check = True
    attempt = 1
    while check:
        if user_number > random_num:
            print("Too high")
            user_number = int(input(", Try again.\t"))
            attempt += 1
        elif user_number < random_num:
            print("Too low")
            user_number = int(input(", Try again.\t"))
            attempt += 1
        else:
            print(f"\nCongratulations! You guessed the correct number {random_num} in {attempt} attempts.")
            check = False


play_game()
check_play = True
while check_play:
    play_again = input("Do you want to play again? (yes/no):")
    if play_again == "yes":
        play_game()
    else:
        check_play = False
        print("\nThanks for playing! Goodbye.")
