from Question import Question
from Survey import Survey
from Section import Section
from Answer import Answer

# Welcome User to Survey
Survey.start_survey()

# 1 - ask if they are a student or a mentor

# qualify_one = Question('Are you a student or a mentor? ')
# qualify_two = Question('How many classes have you attended? ')
# qualify_three = Question('Are you comfortable using skill social? ')
# qualify_four = Question('Are you comfortable using slack? ')

# answer_one = (qualify_one.ask_question('Are you a student or a mentor?'))
# answer_two = Question(qualify_two.ask_question('How many classes have you attended?'))
# answer_three = Question(qualify_three.ask_question('Are you comfortable using skill social? '))
# answer_four = Question(qualify_four.ask_question('Are you comfortable using slack?'))

# print (answer_one)
# print (answer_two)
# print (answer_three)
# print (answer_four)
answer_options_list = ['A', 'B']
# question_one = Question('This is your first question', answer_options_list)

# question_one.ask_question()


#STUDENT OR MENTOR QUESTION SECTION
student_or_mentor = Section(
    #qualifying_question
    Question(
        'Are you a student or mentor?', 
        ['[A] - Yes, I am a student', 
         '[B] - No I am not a student']),
    #first_question
    Question ('Do you like being a student?', answer_options_list),
    #description
    'This section will ask you about being a shecodes student'
)

print(student_or_mentor.description)
print(student_or_mentor.qualifying_question)

my_answer = Answer('A', 'This is my answer', Question('this is a question', answer_options_list), True)

# ASK QUALIFYING QUESTION ONE
print(f'{student_or_mentor.qualifying_question.answers[0]} ')
print(f'{student_or_mentor.qualifying_question.answers[1]} ')
student_or_mentor.qualifying_question.get_answer_by_code()



#QUALIFYING QUESTIONS

    # SECTION 1 (OBJECT) 
        # QUESTION  - QUALIFYING QUESTION

    # SECTION 2 (QUESTION) - QUESTION 2

    # OBJECT (QUESTION) - QUESTION 3 

#OBJECT (SECTION) - SECTION 1 - STUDENT QUESTIONS

    # OBJECT (QUESTION) - QUESTION 1

    # OBJECT (QUESTION) - QUESTION 2


#OBJECT (SECTION) SECTION 3 - IN CLASS QUESTIONS

#SECTION 4 - SLACK QUESTIONS

