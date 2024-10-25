import random
from Data import question_bank
from Question import Quest
from quiz_brain import QuizBrain

q_list = []
for i in question_bank:
    j = random.choice(question_bank)
    question = j["question"]
    answer = j["correct_answer"]
    new_q = Quest(question, answer)
    q_list.append(new_q)

quiz = QuizBrain(q_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score: {quiz.score}/{quiz.question_num}")