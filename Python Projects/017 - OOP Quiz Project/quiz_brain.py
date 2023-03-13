class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(answer, current_question)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.answer:
            self.score += 1
            print(f"You got it right! Score: {self.score}/{self.question_number}\n")
            return True
        else:
            print("You got it wrong.")
        print(f"The answer was {correct_answer.answer}.\n")
        return False
