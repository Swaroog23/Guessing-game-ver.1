from random import randint


def guess_the_number():

    """Function for guessing game with the computer, where you have to guess the number between 1 and 100"""

    answer = randint(1, 100)
    player_choice = 0

    print("Guess the number!!!")

    while player_choice != answer:
        try:
            player_choice = int(input("Your guess: "))
        except (TypeError, ValueError):
            print("It's not a number!")

        if player_choice > answer:
            print("Too big!")
        elif player_choice < answer:
            print("Too small!")

    return "Congrats!!! You've won!!!"
