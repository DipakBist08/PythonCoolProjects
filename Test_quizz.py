print("Welcome to Quizz!!!")

score = 0

playing = input("Do you want to play quizz?(yes/no): ").lower()
if playing!="yes":
    quit()

print("Let's play")

answer = input("CPU stands for ? ").lower()
if answer=="central processing unit":
    print("correct")
    score+=1
else:
    print("Incorrect")

answer = input("RAM stands for? ")

if answer=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print(f"Your score is {score}")

