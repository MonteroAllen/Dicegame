import random
import time



def dicegame():
    dice = list(range(1, 7))
    ans = (random.choice(dice))
    print("You rolled a " + str(ans))


def game():
    print("Good choice!")
    time.sleep(1)
    print("It's time to roll the dice!")
    time.sleep(1)
    print("Rolling dice please wait")
    time.sleep(4)
    dicegame()
    ans2 = input("Would you like to play again? Yes or No?")
    if ans2 in ['Yes', 'yes']:
        game()




