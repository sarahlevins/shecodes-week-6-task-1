from Question import Question
from Survey import Survey
from Section import Section
from Answer import Answer

survey = Survey({
#STUDENT OR MENTOR QUESTION SECTION
    1:
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
            {1: Question(
                'Do you like being a student?', 
                    [
                    Answer('A', 'Yes, I love it!'), 
                    Answer('B', 'No, I don\'t like it')
                    ]
                ),
            2: Question(
                'Are you having fun being a student?', 
                    [
                    Answer('A', 'Yes, I love it!'), 
                    Answer('B', 'No, I don\'t like it')
                    ]
                ),
            3: Question(
                'Are you having fun being a student??', 
                    [
                    Answer('A', 'Yes, I love it!'), 
                    Answer('B', 'No, I don\'t like it')
                    ]
                )
            },
            #description
            'Student or Mentor'
        )
    ,
    2: 
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
            {1:Question(
                'Do you like skillsocial?', 
                    [
                    Answer('A', 'Yes, I love it!'), 
                    Answer('B', 'No, I don\'t like it')
                    ]
                ),
            2:Question(
                'Would you recommend skillsocial to others?',
                    [
                    Answer ('A', 'Absolutey!'),
                    Answer ('yes', 'yes')
                    ]
                )
            },
            #description
            'Skill Social'
        )
    ,
    3:
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
            {1: Question(
                'Do you like slack?', 
                    [
                    Answer('A', 'Yes, I love it!'), 
                    Answer('B', 'No, I don\'t like it')
                    ]
                ),
            2: Question(
                'Would you recommend slack to other?',
                    [
                    Answer('A', 'Yeah, sure!'),
                    Answer('B', 'No way jose!')
                    ]
                ),
            3: Question(
                'This is the third slack question',
                    [
                    Answer('A', 'Yeah, sure!'),
                    Answer('B', 'No way jose!')
                    ]
                ),
            4: Question(
                'This is the fourth slack question',
                [
                Answer('A', 'Yeah Sure!'),
                Answer('B', 'for shore')
                ]
            )
            },
            #description
            'Slack'
        )
}
)