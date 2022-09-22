from helpers import data_processor


QUESTIONS = [
    "What is the number of Partipants attending General Meeting per date, date filter between 9/12/2022 and 9/16/2022?", # noqa
    "What is the Meeting duration of General Meeting per date, date filter between between 9/12/2022 and 9/16/2022?" # noqa
]


OPTIONS = {
    'meeting_title': 'Enter the meeting name: ',
    'start_date':'Enter the start date: ',
    'end_date': 'Enter the end date: '
}


def process_questions():
    print('''
        Question templates:
    ''')
    for index, question in enumerate(QUESTIONS):
        print(f'\t{index}. {question}')

    selected_question = input('\nWrite the number of the question you want: ').lower()
    return selected_question


def process_question_options(question):
    arguments = {}
    arguments['question'] = question
    for key, value in OPTIONS.items():
        arguments[key] = input(value)
        print('-'*40)
    return arguments


def main():
    while True:
        print('_'*100)
        selected_question = process_questions()

        if(selected_question == 'q'):
            break

        arguments =  process_question_options(selected_question)
        print(data_processor.get_data(arguments))

main()