import csv
from os import listdir
import codecs
from datetime import datetime



DATE_PATTERN = '%m%d%Y'
PATH = './attendace_reports/'


def get_attendance_reports_data(start_date, end_date, metting_title):
    try:

        start_date = start_date.replace('/','')
        end_date = end_date.replace('/','')
        report_directories = listdir(PATH)
        filtered_report_directories = filter_report_directories_by_date(start_date,end_date, report_directories)
        return read_attendance_reports(filtered_report_directories, metting_title)

    except Exception:
        print('Bad start date or end date format - correct format: [mm/dd/yy, mmddyy]')
        return []

def read_attendance_reports(directories, metting_tittle):
    attendance_data = []
    for directory in directories:
        reports = listdir(f'{PATH}{directory}')
        for report in reports:
            attendance = list(csv.reader(codecs.open(f'{PATH}{directory}/{report}', 'rU', 'utf-16'), delimiter="\t"))
            if attendance[2][1].lower() == metting_tittle.lower():
                attendance_data.append(attendance)
    return attendance_data


def filter_report_directories_by_date(start_date, end_date, report_directories):
    filtered_report_directories = []

    start_date = datetime.strptime(start_date, DATE_PATTERN)
    end_date = datetime.strptime(end_date, DATE_PATTERN)
        
    for directory in report_directories:
        formatted_directory = datetime.strptime(directory, DATE_PATTERN)
        if(formatted_directory >= start_date and formatted_directory <= end_date ):
            filtered_report_directories.append(directory)
    
    return filtered_report_directories

