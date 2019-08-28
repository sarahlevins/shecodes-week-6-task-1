class Question:
    def __init__(self, question):
        self.question = question
    
    def ask_question (self, question):
        print(question)
        answer = input('what is your answer? ')
        return answer