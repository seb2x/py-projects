import random

lowest = int(input("Enter your lowest number: "))
highest = int(input("Enter your highest number: "))
 
number = random.randint(lowest, highest)

tries = 0

while True:
    guess = int(input(f"Guess a random number from {lowest}-{highest}: "))
    tries += 1
    if guess == number:
        print(f"Correct number! it took you ({tries}) tries.")
        prompt = input(("Play again? (y/n)")).lower()
        if prompt == "y":
            tries = 0
            lowest = int(input("Enter your lowest number: "))
            highest = int(input("Enter your highest number: "))
            number = random.randint(lowest, highest)   
        else:
            print("thanks for playing!")
            break
        
    elif guess > number:
        tries = tries + 1
        print("too high of a guess try again.")
        
    elif guess < number:
        tries = tries + 1
        print("too low of a guess try again.")
        
    if tries == 5:
        prompt_2 = input(("Too many tries! restart? (y/n)")).lower()
        if prompt_2 == "y":
            tries = 0
            lowest = int(input("Enter your lowest number: "))
            highest = int(input("Enter your highest number: "))
            number = random.randint(lowest, highest)   
        else:
            print("thanks for playing!")
            break
        