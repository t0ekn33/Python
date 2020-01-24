"""Lab 04c
Process all of the records in the tmpprecip.dat file.
Accumulate in a two-dimensional list the total precipitation
by year. A partial format of the records in this file is
repeated here.
Columns Content
5 – 8 Year
9 – 13 Precipitation in the format dd.dd (inches)
When you are finished creating the list, sort it by year and
print the results. A partial answer is shown here. Use the
technique shown in sample hlists8.jpg
"""

weather = []
fin = open('Python2/Labs/tmpprecip.dat', 'r') # Windows

for line in fin:
    year = line[4:8]
    rain = float(line[8:13])
    for entry in weather:
        if entry[0] == year:
            entry[1] += rain
            break
    else:
        weather.append([year, rain])

weather.sort()
for year, rain in weather:
    print('{0} {1:.2f}'.format(year, rain))        