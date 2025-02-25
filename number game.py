import random 

playing = True

number = random.randint(1, 10)

print("Guess a number between 1 to 10!")

while playing:
    guess = int(input("Give me your bet guess: "))
    
    if guess > number:
        print("No! Your guessed number is greater than the correct number.")
        print("Please try again!")
    elif guess < number:
        print("No! Your guessed number is smaller than the correct number.")
        print("Please try again!")
    else:
        print("You win the game!")
        print(f"The number was {guess}")
        break