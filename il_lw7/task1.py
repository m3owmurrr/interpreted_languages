import csv
from datetime import datetime, timedelta
import re


def parseTime(timeStr):
    timeComponents = re.split(":| ", timeStr)

    if (len(timeComponents) == 1):
        minutes, seconds = float(timeComponents[0]), 0.0
    elif (len(timeComponents) == 2):
        minutes, seconds = float(timeComponents[0]), float(timeComponents[1])
    else:
        minutes, seconds = float(timeComponents[0]), float(timeComponents[2])
    return timedelta(minutes=minutes, seconds=seconds)


filePath = ('10-2.csv')
print("Enter a letter: ", end="")
startingLetter = input()
print("Enter the maximum execution time: ", end="")
maxTime = parseTime(input())

passedTests = []

with open(filePath, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        lastName, firstName, org, dep, email, status, startTime, endTime, spentTime, totalScore, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10 = row

        if lastName.startswith(startingLetter) and parseTime(spentTime) < maxTime:
            passedTests.append({
                'last_name': lastName,
                'first_name': firstName,
                'start_time': startTime,
                'end_time': endTime,
                'spent_time': parseTime(spentTime)
            })

print()
for person in passedTests:
    print(
        f"{person['last_name']} - Start: {person['start_time']}, End: {person['end_time']}, Spent time: {person['spent_time']}")
