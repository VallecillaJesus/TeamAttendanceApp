from datetime import datetime
import json
import os



converted = {}

def parse_to_json(attendance_reports, type):
    if len(attendance_reports) == 0:
        return converted 

#   Access to the attendance_reports meeting_title position
    converted['meeting_title'] = attendance_reports[0][2][1]
    converted['data'] = []

    if type == "durations":
        convert_to_durations_template(attendance_reports)
    elif type == "participants":
        convert_to_participants_template(attendance_reports)
    return converted


def generate_json_file(path, filename, content):
    foldername = filename.replace('log_','')[:8]
    target = path + foldername + '\\' + filename

    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w") as file:
        json.dump(content,file)
        

def convert_to_durations_template(attendance_reports):
    for attendance_report in attendance_reports:
        record = {}

        start_time = ''.join(attendance_report[3][1].split(',')[1])
        end_time = ''.join(attendance_report[4][1].split(',')[1])

        record["date"] = attendance_report[3][1].split(',')[0]
        record["duration"] = get_duration(start_time, end_time)
        converted['data'].append(record)


def get_duration(start_time, end_time):
    start_time = datetime.strptime(start_time.strip(),'%H:%M:%S %p')
    end_time = datetime.strptime(end_time.strip(), '%H:%M:%S %p')
    result = datetime.strptime(str(end_time - start_time), '%H:%M:%S')
    return f'{result.hour}h {result.minute}m'


def convert_to_participants_template(attendance_reports):
    for attendance_report in attendance_reports:
        record = {}
        record["date"] = attendance_report[3][1].split(',')[0]
        record["participants"] = attendance_report[1][1]
        converted["data"].append(record)
