class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score =0

    def next_question(self):
        ques = self.question_list[self.question_number]
        self.question_number +=1
        u_answer = input(f"Q.{self.question_number}: {ques.text} (True/False): ")
        self.check_answer(u_answer,ques.answer)

    def still_has_questions(self):
       return self.question_number<len(self.question_list)
    
    def check_answer(self,u_ans,c_ans):
        if u_ans.lower()==c_ans.lower():
            print("You got it right")
            self.score +=1
        else:
            print("That's Wrong.")
        print(f"The correct answer was: {c_ans}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print('\n')

        

        