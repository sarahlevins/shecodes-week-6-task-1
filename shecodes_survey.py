from Question import Question
from Survey import Survey
from Section import Section
from Answer import Answer


survey = Survey({
#STUDENT OR MENTOR QUESTION SECTION
    1 :
        Section(
            #qualifying_question
            Question(
                'Are you a student or mentor?', 
                ['[A] - Yes, I am a student', 
                '[B] - No, I am not a student']),
            #first_question
            Question ('Do you like being a student?', 
                ['[A] - Yes',
                '[B] - No']),
            #description
            'This section will ask you about being a shecodes student'
        )
    ,
    2 : 
        #SKILLSOCIAL SECTION
        Section(
            #qualifying_question
            Question(
                'Have you used skill social before?', 
                ['[A] - Yes', 
                '[B] - No']),
            #first_question
            Question ('Do you like skill social', 
                ['[A] - Yes',
                '[B] - No']),
            #description
            'This section is about using skill social'
        )
    ,
    3 :
        #SKILLSOCIAL SECTION
        Section(
            #qualifying_question
            Question(
                'Have you used slack before?', 
                ['[A] - Yes', 
                '[B] - No']),
            #first_question
            Question ('Do you like slack', 
                ['[A] - Yes',
                '[B] - No']),
            #description
            'This section is about using slack'
        )
}
)

survey.start_survey('Welcome to my shecodes survey!')
survey.start_survey('I hope you enjoy completing it!')
print('')

survey.ask_qualifying_questions(1)
survey.ask_qualifying_questions(2)
survey.ask_qualifying_questions(3)



# ASK QUALIFYING QUESTION ONE, take answer and return true or false
# print(student_or_mentor.description)
# print(f'{student_or_mentor.qualifying_question.question_text}')
# print(f'{student_or_mentor.qualifying_question.answers[0]} ')
# print(f'{student_or_mentor.qualifying_question.answers[1]} ')
# # do method to get true or false
# is_student = student_or_mentor.qualifying_question.get_answer_by_code()



