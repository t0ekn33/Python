"""
Lab 04d
Read the data in tmpprecip2012.dat and create a two-dimensional list containing all
the data that will allow you to print a report by month of the following:
Average high temperature,
Maximum high temperature,
Minimum high temperature
Once that works, try your program on tmpprecip.dat. It contains over 100 years of
daily data.
"""


weather = []
cnt = 0
fin = open('Python2/Labs/tmpprecip2012.dat', 'r')
# fin = open('/home/student/pydata/tmpprecip.dat', 'r')
for rec in fin:
    month = rec[0:2]
    temp = int(rec[13:16])
    for entry in weather:
        
        if entry[0] == month:
            entry[1] += temp
            entry[2] = max.temp()
            entry[2] = cnt 
            break
    else:
        weather.append([month, temp, cnt])

for month, temp, cnt in weather:
    print(month, temp, cnt)
print(weather)