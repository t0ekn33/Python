"""
prompt for score between 0.0 and 1.0. If score is out of range, print error. 
If in range, print grade.
"""

def computerGrade(score):
    if(score < 0.0 or score > 1.0):
        grade = ("Invalid score.")
    elif(score >= 0.9):
        grade = ("Grade: A")
    elif(score >= 0.8):
        grade = ("Grade: B")
    elif(score >= 0.7):
        grade = ("Grade: C")
    elif(score >= 0.6):
        grade = ("Grade: D")
    else:
        grade = ("Grade: F")
    return grade

score = input("Enter score between 0.0 and 1.0:")
score = float(score)
grade = computerGrade(score)
print(grade)

