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
        print (f'{self.survey_sections[a].qualifying_question.answers[0]}')
        print (f'{self.survey_sections[a].qualifying_question.answers[1]}')
        return self.survey_sections[a].qualifying_question.get_answer_by_code()


# ASK QUALIFYING QUESTION ONE, take answer and return true or false
# print(student_or_mentor.description)
# print(f'{student_or_mentor.qualifying_question.question_text}')
# print(f'{student_or_mentor.qualifying_question.answers[0]} ')
# print(f'{student_or_mentor.qualifying_question.answers[1]} ')
# # do method to get true or false
# is_student = student_or_mentor.qualifying_question.get_answer_by_code()

    # def start_survey_sections()

    # def ask_question()

    # def show_answers()

    # def answer_question()

    # def go_to_next_question()

    # def end()
    
