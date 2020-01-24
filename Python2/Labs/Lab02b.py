"""
LAB 02b
Review the file tmpprecip2012.dat. It is laid out as follows:
Columns Content
1 – 2 Month
3 – 4 Day
5 – 8 Year
9 – 13 Precipitation in the format dd.dd (inches)
14 – 16 High Temperature
The file contains San Antonio temperature and precipitation data for
2012. Accumulate the number of days with measurable
precipitation and the precipitation total for the year and print them. 
Rain days: 72
Rain amount: 39.230000...01 inches

"""
rainDays = 0 
ttlRain = 0

fin = open('Python2/Labs/tmpprecip2012.dat', 'r')
for line in fin:
    rain = float(line[8:13])
    if rain > 0:
        ttlRain += rain
        rainDays += 1
        #print("r:", rain)
        #print("d:", days)

print("Rain days:", rainDays)
print("Rain amount:", ttlRain, "inches")
fin.close()