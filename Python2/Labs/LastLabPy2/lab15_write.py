"""lab15_write.py

This code is extracted from Learn Python the Hard Way and modified
to simplify the task.  The objective here is just to write text to
a file first with the new-line character then without it.
"""

print("Opening the file...")
target = open('c:/pydata/test.txt', 'wt')
# target = open('/home/student/pydata/test.txt', 'wt')

line1 = 'Anydata you want 1'
line2 = 'Anydata you want 2'
line3 = 'Anydata you want 3'

print("I'm going to write these to the file.")

target.write(line1 + '\n')  # Concatenate a new-line character to the string
target.write(line2 + '\n')
target.write(line3 + '\n')

print("And finally, we close it.")
target.close()
