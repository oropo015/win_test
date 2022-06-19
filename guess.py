import random


def guess(x):
    name = input("Enter your name: ")
    guess_num = random.randint(1, x)
    guess = 0
    while guess != guess_num:
        guess = int(input("Enter your guess: "))
        if guess > guess_num:
            print("Guess number too high")
        elif guess < guess_num:
            print("Guess number too low")
        
    print(f"Good one {name}")

guess(10)
            
            
