from Question import Question
from Answer import Answer
from Section import Section

class Survey:
    def __init__(self,survey_sections):
        self.survey_sections = survey_sections

    def start_survey(self, welcome_text):
        print (welcome_text)
        
    def ask_qualifying_questions(self,a):
        print (f'{self.survey_sections[a].qualifying_question.question_text}')
        print (f'[{self.survey_sections[a].qualifying_question.answers[0].code}] - {self.survey_sections[a].qualifying_question.answers[0].answer_text}')
        print (f'[{self.survey_sections[a].qualifying_question.answers[1].code}] - {self.survey_sections[a].qualifying_question.answers[1].answer_text}')

    def answer_qualifying_question(self,a):
        if self.survey_sections[a].qualifying_question.get_answer_by_code() == True:
            self.survey_sections[a].qualifying_question.result = True


    def ask_question(self,a):
        print (f'{self.survey_sections[a].first_question.question_text}')
        print (f'[{self.survey_sections[a].first_question.answers[0].code}] - {self.survey_sections[a].first_question.answers[0].answer_text}')
        print (f'[{self.survey_sections[a].first_question.answers[1].code}] - {self.survey_sections[a].first_question.answers[1].answer_text}')

    def answer_question(self,a):
        if self.survey_sections[a].first_question.get_answer_by_code() == True:
            self.survey_sections[a].first_question.result = True

