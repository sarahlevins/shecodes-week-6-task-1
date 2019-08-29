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
                    [
                    Answer('A', 'Yes, I am a student'), 
                    Answer('B', 'No, I am not a student')
                    ]
                    ),
            #first_question
            Question(
                'Do you like being a student?', 
                    [
                    Answer('A', 'Yes, I love it!'), 
                    Answer('B', 'No, I don\'t like it')
                    ]
                    ),
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
                    [
                    Answer('A', 'Yes.'), 
                    Answer('B', 'No.')
                    ]
                    ),
            #first_question
            Question(
                'Do you like skillsocial?', 
                    [
                    Answer('A', 'Yes, I love it!'), 
                    Answer('B', 'No, I don\'t like it')
                    ]
                    ),
            #description
            'This section will ask you about being using skill social'
        )
    ,
    3 :
        #SLACK SECTION
        Section(
            #qualifying_question
            Question(
                'Have you used slack before?', 
                    [
                    Answer('A', 'Yes.'), 
                    Answer('B', 'No.')
                    ]
                    ),
            #first_question
            Question(
                'Do you like slack?', 
                    [
                    Answer('A', 'Yes, I love it!'), 
                    Answer('B', 'No, I don\'t like it')
                    ]
                    ),
            #description
            'This section will ask you about using slack'
        )
}
)

survey.start_survey('Welcome to my shecodes survey!')
survey.start_survey('I hope you enjoy completing it!')
print('')


for x in range(1,len(survey.survey_sections)+1):
    survey.ask_qualifying_questions(x)
    survey.answer_qualifying_question(x)


for y in range(1, len(survey.survey_sections)+1):
    if survey.survey_sections[y].qualifying_question.result == True:
        survey.ask_question(y)
        survey.answer_question(y)

