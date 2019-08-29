from Question import Question
from Answer import Answer
from Section import Section


class Survey:
    def __init__(self,survey_sections):
        self.survey_sections = survey_sections

    def start_survey(self, survey_name, instructions):
        print ('*******************************************')
        print (f'************* {survey_name} ************')
        print ('*******************************************')
        print ('')
        print(instructions)
        print('')
        
    def ask_qualifying_questions(self):
        for a in range(1, len(self.survey_sections)+1):
            
            print (f'{self.survey_sections[a].qualifying_question.question_text}')
            print (f'[{self.survey_sections[a].qualifying_question.answers[0].code}] - {self.survey_sections[a].qualifying_question.answers[0].answer_text}')
            print (f'[{self.survey_sections[a].qualifying_question.answers[1].code}] - {self.survey_sections[a].qualifying_question.answers[1].answer_text}')

            if self.survey_sections[a].qualifying_question.get_answer_by_code() == True:
                self.survey_sections[a].qualifying_question.result = True


    def ask_questions(self):
        for a in range(1, len(self.survey_sections)+1):
            if self.survey_sections[a].qualifying_question.result == True:
                print (f'{self.survey_sections[a].first_question.question_text}')
                print (f'[{self.survey_sections[a].first_question.answers[0].code}] - {self.survey_sections[a].first_question.answers[0].answer_text}')
                print (f'[{self.survey_sections[a].first_question.answers[1].code}] - {self.survey_sections[a].first_question.answers[1].answer_text}')
                print('')
                if self.survey_sections[a].first_question.get_answer_by_code() == True:
                    self.survey_sections[a].first_question.result = True
                print('')

    def show_answers(self):

        print ('*******************************************')
        print ('************* YOUR ANSWERS ****************')
        print ('*******************************************')
        print ('')

        for a in range(1, len(self.survey_sections)+1):

            if self.survey_sections[a].qualifying_question.result == True:
                print (f'For Section {a}, {self.survey_sections[a].description}, you answered')
                print (f'{self.survey_sections[a].qualifying_question.answers[0].code} - {self.survey_sections[a].qualifying_question.answers[0].answer_text}')
                print ('')

                if self.survey_sections[a].first_question.result == True:
                    print(f'For Question, {self.survey_sections[a].first_question.question_text}, you answered')
                    print(f'{self.survey_sections[a].first_question.answers[0].code} - {self.survey_sections[a].first_question.answers[0].answer_text}')
                    print ('')
                else:
                    print(f'For the question, \'{self.survey_sections[a].first_question.question_text}\', you answered')
                    print(f'{self.survey_sections[a].first_question.answers[1].code} - {self.survey_sections[a].first_question.answers[1].answer_text}')
                    print ('')

