from unittest import result
from xml.dom import NotFoundErr
from helpers import csv_processor, json_processor
from datetime import datetime



def get_data(arguments):
    results = csv_processor.get_attendance_reports_data(arguments['start_date'], arguments['end_date'], arguments['meeting_title'])
    selected_question = arguments["question"]

    if selected_question == '0':
        results = json_processor.parse_to_json(results, "participants")
    elif selected_question == '1':
        results = json_processor.parse_to_json(results, "durations")
    else:
        print('Not found question')
        return results

    if len(results) != 0:
        json_processor.generate_json_file('./',f'log_{get_datetime()}.json', results)

    return results


def get_datetime():
    current_datetime = datetime.now()
    date = str(current_datetime.date()).replace('-','') 
    time = str(current_datetime.time()).replace(':','')[:5]
    return date + time