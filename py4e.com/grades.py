"""
prompt for score between 0.0 and 1.0. If score is out of range, print error. 
If in range, print grade.
"""

score = input("Enter score between 0.0 and 1.0:")
score = float(score)
if(score < 0.0 or score > 1.0):
    print("Invalid score.")
elif(score >= 0.9):
    print("Grade: A")
elif(score >= 0.8):
    print("Grade: B")
elif(score >= 0.7):
    print("Grade: C")
elif(score >= 0.6):
    print("Grade: D")
else:
    print("Grade: F")

