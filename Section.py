from Question import Question
from Answer import Answer

class Section:
    def __init__ (self, qualifying_question, first_question, description):
        self.qualifying_question = qualifying_question
        self.first_question = first_question
        self.description = description
