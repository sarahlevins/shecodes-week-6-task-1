from Answer import Answer

class Question:
    def __init__(self, question_text, answers):
        self.question_text = question_text
        self.answers = answers

    def get_answer_by_code(self):
        code = input('What is your answer? ')
        if code == 'A':
            return True
        else:
            return False

        