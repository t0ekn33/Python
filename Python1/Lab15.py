
file_out = open('C:\\Users\\s728417\\Documents\\Python\\Python1\\lab15.dat', 'wt')
# Where filename contains the full path and name of file
# If you just give the file name, it will be placed in the current
# directory.

line1 = 'This is record one\n'
line2 = 'This is record two\n'
line3 = 'This is record three\n'

print ("Write records to the file.")

file_out.write(line1)
file_out.write(line2)
file_out.write(line3)

file_out.close()
print("Now, open the file with a text editor")
