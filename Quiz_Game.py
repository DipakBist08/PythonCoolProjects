print("Welcome to my computer quizz!!!")
playing  = input("Do you want to play? yes/no: ")
if playing.upper()!="YES":
    quit()

print("Okay ! Let's play : )")
score = 0

answer = input("What does CPU stands for? ")
if answer == "central processing unit":
    print("You got it.")
    score+=1

else:
    print("Wrong!! Give a shot one more time!!!")

answer = input("What does GPU stands for? ")
if answer == "graphical processing unit":
    print("You got it.")
    score+=1

else:
    print("Wrong!! Give a shot one more time!!!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("You got it.")
    score+=1

else:
    print("Wrong!! Give a shot one more time!!!")

answer = input("Who was the father of computer? ")
if answer.lower() == "charls babbies":
    print("You got it.")
    score+=1
else:
    print("Wrong!! Give a shot one more time!!!")
print("you got " + str(score)  +  " questions wright")

