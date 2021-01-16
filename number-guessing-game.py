#Method-1 guess the number game
import random

number = random.randint(1,10)
guess = 0
count = 0
print("You can exit the game anytime. Just enter 'exit'.")
while guess != number and guess != "exit":
    guess = input("Guess a number between 1 to 10 :- ")

    if guess == "exit":
        print("Closing the game...")
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("\nCongratulation, You got it!")
        print("You have tried ", count ," times")
