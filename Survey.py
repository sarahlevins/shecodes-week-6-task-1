from Question import Question
from Answer import Answer
from Section import Section


class Survey:
    def __init__(self,survey_sections):
        self.survey_sections = survey_sections

    def start_survey(self, survey_name = 'SURVEY', instructions = 'COMPLETE THE FOLLOWING SURVEY'):
        print (f'\n**********************\n{survey_name}\n**********************')
        print(f'\n{instructions}:')
        
    def ask_qualifying_questions(self):
        for a in range(1, len(self.survey_sections)+1):
            
            print (f'\n{self.survey_sections[a].qualifying_question.question_text}')
            print (f'[{self.survey_sections[a].qualifying_question.answers[0].code}] - {self.survey_sections[a].qualifying_question.answers[0].answer_text}')
            print (f'[{self.survey_sections[a].qualifying_question.answers[1].code}] - {self.survey_sections[a].qualifying_question.answers[1].answer_text}')
            if self.survey_sections[a].qualifying_question.get_answer_by_code() == True:
                self.survey_sections[a].qualifying_question.result = True

    def ask_questions(self):
        for a in range(1, len(self.survey_sections)+1):
            if self.survey_sections[a].qualifying_question.result == True:
                print (f'\n**********************\nSection {a}')
                for b in range(1, len(self.survey_sections[a].first_question)+1):
                    print (f'\n{self.survey_sections[a].first_question[b].question_text}')
                    print (f'[{self.survey_sections[a].first_question[b].answers[0].code}] - {self.survey_sections[a].first_question[b].answers[0].answer_text}')
                    print (f'[{self.survey_sections[a].first_question[b].answers[1].code}] - {self.survey_sections[a].first_question[b].answers[1].answer_text}')
                    if self.survey_sections[a].first_question[b].get_answer_by_code() == True:
                        self.survey_sections[a].first_question[b].result = True


    def show_answers(self):
        print (f'\n**********************\nYOUR ANSWERS\n**********************')
        for a in range(1, len(self.survey_sections)+1):
            if self.survey_sections[a].qualifying_question.result == True:
                print (f'\nFor section {a}, {self.survey_sections[a].description}, you answered')
                print (f'{self.survey_sections[a].qualifying_question.answers[0].code} - {self.survey_sections[a].qualifying_question.answers[0].answer_text}')
                print ('')
                for b in range(1, len(self.survey_sections[a].first_question)+1):
                    if self.survey_sections[a].first_question[b].result == True:
                        print(f'For section {a} question {b}, {self.survey_sections[a].first_question[b].question_text}, you answered')
                        print(f'{self.survey_sections[a].first_question[b].answers[0].code} - {self.survey_sections[a].first_question[b].answers[0].answer_text}')
                        print ('')
                    else:
                        print(f'For the section {a} question {b}, \'{self.survey_sections[a].first_question[b].question_text}\', you answered')
                        print(f'{self.survey_sections[a].first_question[b].answers[1].code} - {self.survey_sections[a].first_question[b].answers[1].answer_text}')
                        print ('')
            else:
                print(f'You did not qualify to answer any questions in the {self.survey_sections[a].description} section.')
    
    def end_and_repeat_survey(self):
        repeat = input('Thank you for taking the time to compete this survey.\nWould you like to complete this survey again?\n Y / N?: \n')
        if repeat == 'Y':
            self.start_survey()
            self.ask_qualifying_questions()
            self.ask_questions()
            self.show_answers()
            self.end_and_repeat_survey()
        else:
            print('\nNo worries. Thank you for your time. \n')




