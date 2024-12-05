import datetime

def current_time():
    return datetime.datetime.now().date()
def days_between(date1, date2):
    difference = date1 - date2
    return difference