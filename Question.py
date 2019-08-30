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
            if ans.upper() != 'A' or 'B':
                print ('That answer is invalid, please enter "A" or "B"')
            if ans.upper() == 'A':
                validate = True
                return True
            else:
                if ans.upper() == 'B':
                    validate = True
                    return False
