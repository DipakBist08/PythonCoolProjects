from Quizz_Best_approach import playing


def ask_questoin(question,correct_answer):
    answer = input(question+ " ").lower()
    if answer== correct_answer.lower():
        print("You got it !:)")
        return 1
    else:
        print("Incorrect! Give a shot one moret ime")
        return 0


print("Welcome to my computer quizz!!")

playing =input("Do you want to play?(yes/no): ").lower()
if playing !="yes":
    quit()
print("Let's Play game!!")
score = 0

questions = [
    ("What does CPU stand for?", "Central Processing Unit"),
    ("What does GPU stand for?", "Graphical Processing Unit"),
    ("What does RAM stand for?", "Random Access Memory"),
    ("Who was the father of computer?", "Charles Babbage")
]
for question, correct_answer in questions:
    score +=ask_questoin(question,correct_answer)


print(f"\n you got {score} out of {len(questions)}")

print(f"\n your score: {round((score/len(questions)))} questions right!")

print(f"Your score:{round(score/len(questions))*100,2}%")
print("Thanks for playing")