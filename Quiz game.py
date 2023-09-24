questions = [
    {
        "question": "How many faces does a Dodecahedron have?",
        "options": ["A) 9", "B) 12", "C) 10", "D) 8"],
        "Answer": "B"
    },
    {
        "question": "Which planet has the most moons?",
        "options": ["A) Saturn", "B) Mercury", "C) Mars", "D) Jupiter"],
        "Answer": "A"
    },
    {
        "question": "How many bones do we have in an ear?",
        "options": ["A) 6", "B) 9", "C) 3", "D) 12"],
        "Answer": "C"
    },
    {
        "question": "What country has won the most World Cups?",
        "options": ["A) Australia", "B) New Zealand", "C) Brazil", "D) England"],
        "Answer": "C"
    },
    {
        "question": "Aureolin is a shade of what color?",
        "options": ["A) Blue", "B) Violet", "C) Red", "D) Yellow"],
        "Answer": "D"
    }
]

def run(questions):
    score = 0  

    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        user_answer = input("Enter your option (A/B/C/D): ").upper()

        if user_answer == question["Answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is", question["Answer"], "\n")

    print("Quiz completed! Your score is", score, "out of", len(questions))

run(questions)