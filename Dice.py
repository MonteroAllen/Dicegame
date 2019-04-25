import random
import time
import Bot

name = input("What is your name")

print("Hello " + name)
time.sleep(1)
print("Welcome to Sterben's dice game test")
time.sleep(1)

answer = input('Would you like to play?')

if answer in ['Yes', 'yes']:
    (Bot.game())
if answer == "No":
    print("Eat pant")



