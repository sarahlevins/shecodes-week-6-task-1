from Question import Question
from Survey import Survey
from Section import Section
from Answer import Answer
from shecodes_survey_questions import survey

survey.start_survey('SHE CODES SURVEY', 'Please answer the following quesions so we can improve the programme')
survey.ask_qualifying_questions()
survey.ask_questions()
survey.show_answers()
survey.end_and_repeat_survey()
