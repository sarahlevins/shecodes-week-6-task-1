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
            'Student or Mentor'
        )
    ,
    2 : 
        #SKILLSOCIAL SECTION
        Section(
            #qualifying_question
            Question(
                'Have you used skill social before?', 
                    [
                    Answer('A', 'Yes, I have used skill social before.'), 
                    Answer('B', 'No, I have never used it')
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
            'Skill Social'
        )
    ,
    3 :
        #SLACK SECTION
        Section(
            #qualifying_question
            Question(
                'Have you used slack before?', 
                    [
                    Answer('A', 'Yes, I have used slack before'), 
                    Answer('B', 'No, I have never used it')
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
            'Slack'
        )
}
)
#survey_name, instructions
survey.start_survey('SHE CODES SURVEY', 'Please answer the following quesions so we can improve the programme')
survey.ask_qualifying_questions()
survey.ask_questions()
survey.show_answers()

