class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        answer_user = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer_user, current_question.answer)
    
    def check_answer(self,answer_user, correct_answer):
        if answer_user.lower() == correct_answer.lower():
            print("You got it right")
            self.score+=1
            print(f"the current score is {self.score}/{self.question_number}")
        else:
             print("It's  wrong")
             print(f"the correct answer is {correct_answer}")
             print(f"the current score is {self.score}/{self.question_number}")


    
