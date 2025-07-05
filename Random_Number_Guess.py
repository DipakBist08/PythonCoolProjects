import random

randomNum = random.randint(0,5)
guesses =0
while True:
    guesses+=1
    try:
        user_guess = int(input("Make a guess: "))
    except ValueError:
        print("Please input valid number.")
        continue
    if user_guess==randomNum:
            print("You got it.")
            break
    else:
            print("Make a guess again!!!")
print(f"You took {guesses} attempts.")