import re
def EvenPairs(strParam):
    pattern = r'[02468]\d*[02468]'
    return "true" if re.search(pattern,strParam) else "false"
print(EvenPairs('dbhskdjfssdg47gdfgkj314514dfjgdf'))