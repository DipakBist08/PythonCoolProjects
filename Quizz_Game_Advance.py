# Quiz Game in Python

# List of questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    }
]


# Function to run the quiz
def run_quiz():
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A, B, C, or D): ").upper()

        if answer == q["answer"]:
            print("Correct")
            score += 1
        else:
            print(f"Wrong!!!. The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score} out of {len(questions)}.")


# Start the game
run_quiz()
