from datetime import datetime

def solution(a, b):
    strToDate = datetime.strptime(f'2016-{a}-{b}', "%Y-%m-%d")
    week = strToDate.weekday()
    
    if week == 0:
        answer = 'MON'
    elif week == 1:
        answer = 'TUE'
    elif week == 2:
        answer = 'WED'
    elif week == 3:
        answer = 'THU'
    elif week == 4:
        answer = 'FRI'
    elif week == 5:
        answer = 'SAT'
    elif week == 6:
        answer = 'SUN'
    
    return answer