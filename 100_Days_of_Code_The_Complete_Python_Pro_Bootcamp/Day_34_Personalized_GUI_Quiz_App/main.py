from ui import QuizInterface

quiz_ui = QuizInterface()

print("You've completed the quiz")
print(f"Your final score was: {quiz_ui.quiz.score}/{quiz_ui.quiz.question_number}")