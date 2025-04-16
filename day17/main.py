import data
from question_model import Questions
from quiz_brain import QuizBrain


all_questions =[]
for item in data.question_data:
    all_questions.append(Questions(item['text'],item['answer']))

quiz = QuizBrain(all_questions)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")