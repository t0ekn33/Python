
file_out = open(filename, 'wt')
# Where filename contains the full path and name of file
# If you just give the file name, it will be placed in the current
# directory.

line1 = 'This is record one'
line2 = 'This is record two'
line3 = 'This is record three'

print ("Write records to the file.")

file_out.write(line1)
file_out.write(line2)
file_out.write(line3)

file_out.close()
print("Now, open the file with a text editor")
