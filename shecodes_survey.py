from Question import Question
from Survey import Survey

# Welcome User to Survey
Survey.start_survey()

# 1 - ask if they are a student or a mentor

qualify_one = Question('Are you a student or a mentor? ')
qualify_two = Question('How many classes have you attended? ')
qualify_three = Question('Are you comfortable using skill social? ')
qualify_four = Question('Are you comfortable using slack? ')

answer_one = (qualify_one.ask_question('Are you a student or a mentor?'))
answer_two = Question(qualify_two.ask_question('How many classes have you attended?'))
answer_three = Question(qualify_three.ask_question('Are you comfortable using skill social? '))
answer_four = Question(qualify_four.ask_question('Are you comfortable using slack?'))

print (answer_one)
print (answer_two)
print (answer_three)
print (answer_four)
