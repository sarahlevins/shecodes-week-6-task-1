from Answer import Answer

class Question:
    def __init__(self, question_text, answers, result = False):
        self.question_text = question_text
        self.answers = answers
        self.result = result

    def get_answer_by_code(self):
        validate = False
        while validate == False:
            ans = input('What is your answer? ')

            if ans.upper() != 'A':
                pass
            else:
                validate = True
                return True
            if ans.upper() != 'B':
                print ('That answer is invalid, please enter "A" or "B"')
            else:
                validate = True
                return False
