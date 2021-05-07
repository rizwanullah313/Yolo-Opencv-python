
# youtuber = "rizwan"

# print("subscriber to "+youtuber)
# print("Subscriber to {}".format(youtuber))
# print(f"subscriber to {youtuber}")


# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")

# maltlib = f"computer progamming is so {adj}! It makes me so excited all the time beacuse \ " \
#          f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

# print(maltlib)

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        print(guess)
        guess(10)



