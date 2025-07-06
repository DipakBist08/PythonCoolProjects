import random
print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")
low = int(input("Enter lower bound: "))
high = int(input("Enter high bound: "))

random_num = random.randint(low,high)
attempts=7
user_guess = 0


while user_guess<attempts:
    user_guess+=1
    guess = int(input("Enter your guess: "))
    if guess==random_num:
        print("you got it !!!")
        break
    elif user_guess>=attempts and guess!=random_num:
        print(f"sorry the number was {random_num}.")
    elif guess>random_num:
        print("Too high! Try again!")

    elif guess<random_num:
        print("Too low! try again")



