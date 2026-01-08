def ask_question(q):
    print(q["question"])
    user_answer = input("Your answer: ").lower()

    if user_answer == q["answer"].lower():
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer is: {q['answer']}\n")
        return 0


def quiz_game():
    questions = [
        {"question": "Who painted the Monalisa?", "answer": "Leonardo da Vinci"},
        {"question": "What is the smallest prime number?", "answer": "2"},
        {"question": "Which country discovered pizza ?", "answer": "Italy"},
        {"question": "What is the tallest building in the world?", "answer": "Burj Khalifa"},
        {"question": "- What is the national animal of India?", "answer": "Tiger"},
        {"question": "Worst Kenyan President ?", "answer": "Kasongo"},
    ]

    print("\n WELCOME TO THE PYTHON SMART QUIZ!\n")
    score = 0

    for q in questions:
        score += ask_question(q)

    print(f"Your final score: {score}/{len(questions)}")

    if score == len(questions):
        print("Perfect score! You’re a  genius!\n")
    elif score >= len(questions) * 0.7:
        print("Great job! You’re doing well.\n")
    else:
        print("Keep practicing, you’ll get better.\n")


while True:
    quiz_game()
    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye!")
        break
