"""
Camp1_Day2_assign2
"""

import random



while True:
    number = random.randint(1,10)
    guess = input("Guess the number: ")
    if str(guess) == str(number):
        print("Correct!")
        print ("Press \"n\" to exit ")
    elif (str(guess) != str(number) and str(guess) != "n"):
         print("Wrong, try again! " + "The number is " + str(number))
         print ("Press \"n\" to exit ")
    elif str(guess) == "n":
         break








