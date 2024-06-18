# Step 1: Define the Quiz Data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    }
]

# Step 2: Implement the Scoring System
score = 0

# Step 3: Handle User Input
def get_user_answer():
    answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    return answer

# Step 4: Provide Feedback
def check_answer(question_data, user_answer):
    global score
    if user_answer == question_data["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {question_data['answer']}.")
    print()

# Step 5: Display the Final Score
def display_final_score():
    print(f"Your final score is {score} out of {len(quiz_data)}.")

# Main Function to Run the Quiz
def run_quiz():
    for question_data in quiz_data:
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        user_answer = get_user_answer()
        check_answer(question_data, user_answer)
    display_final_score()

# Run the quiz game
if __name__ == "__main__":
    run_quiz()
