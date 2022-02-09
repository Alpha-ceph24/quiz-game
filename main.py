from question_model import Question
from data import question_data
from quiz_brain import Brain
question_bank =[]
for i in question_data:
    question_bank.append(Question(i["question"],i["correct_answer"]))

x = Brain(question_bank)
while x.still_has_questions():
    x.next_question()

print(f"You have completed the quiz. \nYour final score is {x.score}/{x.question_no}")