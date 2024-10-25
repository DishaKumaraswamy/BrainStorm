class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        item = self.question_list[self.question_num]
        self.question_num+=1
        res = input(f"Q.{self.question_num}: {item.txt} (True/False)?: ")
        self.is_correct(res, item.ans)

    def is_correct(self, user_answer, correct_ans):
        if user_answer.lower() == correct_ans.lower():
            print("You've got it right! ")
            self.score+=1

        else:
            print("That's wrong. ")
        print(f"The answer was {correct_ans}")
        print(f"Score: {self.score}/{self.question_num}")
        print("\n")