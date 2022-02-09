
class Brain:
    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q{self.question_no}: {current_question.text} (True/False)").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer is: {correct_answer} \nYour currnt score is {self.score}/{self.question_no}\n")





