from Answer import Answer

class Question:
    def __init__(self, question_text, answers, result = False):
        self.question_text = question_text
        self.answers = answers
        self.result = result

    def get_answer_by_code(self):
        ans = input('What is your answer? ')
        if ans == 'A':
            return True
        else:
            return False

        