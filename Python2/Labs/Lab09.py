"""
Optional Lab
• Read the tmpprecip.dat file and use a dictionary to accumulate the data
necessary to report the following for each year:
•   Total rainfall (precipitation)
• Maximum high temperature
• Minimum high temperature
• Average high temperature
** Use a separate dictionary to report the average precipitation by month.
• Create well-formatted reports from each dictionary
• The format of the data is repeated on the next slide along with partial answers.
• Once the program is working, exclude all data prior to 1970. Then run again
excluding all data after 1970. Note the differences in rainfall totals.
"""

"""lab_optional.py

This program reads the temperature/precipitation data for San Antonio
for the period 1/1/1900 to 12/31/2016.  The monthly dictionary is used
to accumulate, by month, the
aggregate precipitation.  The average precipitation for each month is
calculated by dividing the aggregate precipitation by the number of
years in the sample.  Note how a set is used to determine the number
of unique years.  Then, one at a time, uncomment the test to exclude
data either before or after 1970.  Note the differences in results.
"""

#dc = dict(key:[totRain,maxTemp,minTemp,days,totCnt])
#dc[year] = [rain,temp,temp,1,temp]
# Access:
# rain => dc[year][0] 
# maxTemp=> dc[year][1] 
# minTemp=> dc[year][2] 
# minTemp=> dc[year][3] 
# days => dc[year][4] += 1



fin = open('Python2/Labs/tmpprecip.dat')
mondic = {}

# mondic format: key: month(2 digit); total precip

yr_set = set()
for linein in fin:
    tyr = linein[4:8]
    tmon = linein[0:2]
    if not (tyr.isdigit()and tmon.isdigit()):
        print('Bad Data - {0!r}'.format(linein))
#        print 'Bad Data - %r' % (linein)  # Older formatting
        continue
#    if tyr < '1970':
#        continue
#    if tyr >= '1970':
#        continue
    try:
        precip = float(linein[8:13])
        temp = int(linein[13:16])
        
    except ValueError:
        print('Bad Data - {0!r}'.format(linein))
#        print 'Bad Data - %r' % (linein)  # Older formatting
        continue
    yr_set.add(tyr)
    if tmon in mondic:
        mondic[tmon] += precip
    else:
        mondic[tmon] = precip

years = len(yr_set)
monlst = sorted(mondic.items())
print('\n\n')
tot_precip = 0.0
for mon, precip in monlst:
    tot_precip += precip/years
    print('{0} {1:5.2f}'.format(mon, precip/years))
#    print '%s %5.2f' % (mon, precip/years)  # Older formatting
print('Average Annual Rainfall - {0:.1f}'.format(tot_precip))               
fin.close()
        
