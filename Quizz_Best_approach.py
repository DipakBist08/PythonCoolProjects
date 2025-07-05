print("Welcome to my computer quiz!!!")

playing = input("Do you want to play? yes/no: ").lower()
if playing != "yes":
    quit()

print("Okay! Let's play!")

score = 0

# Store questions and answers in a list
questions = [
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
    {"question": "What does GPU stand for?", "answer": "graphical processing unit"},
    {"question": "What does RAM stand for?", "answer": "random access memory"},
    {"question": "Who is known as the father of the computer?", "answer": "charles babbage"}
]

# Ask each question
for q in questions:
    answer = input(q["question"] + " ").lower().strip()
    if answer == q["answer"]:
        print("✅ You got it right!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {q['answer'].title()}")

# Calculate and show final score
print(f"\nYou got {score} out of {len(questions)} questions right.")
percentage = (score / len(questions)) * 100
print(f"Your final score: {percentage:.2f}%")
