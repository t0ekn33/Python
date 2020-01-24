"""LAB 08
Use the split() method to process the following files: gdp.txt and
split.txt. Examine each file and determine how best to separate the
various elements to accomplish the assigned task.
In the first file, each record has three elements: country name, total
population and gross domestic product (GDP) in millions of dollars.
Your job is to calculate the GDP per person for each country and
print out country and GDP/person in descending order of percapita GDP. 
Format the results for a professional look. The data
itself comes from Wikipedia, so don't take it seriously.

In the second file, determine how many words there are in the file
and how many of those words are unique. Then print out each
unique word in ascending order. Be sure to change every
alphabetic character to one case and remove/replace all
punctuation using the replace method.
Use the split() method to process the following files: gdp.txt and
split.txt. Examine each file and determine how best to separate the
various elements to accomplish the assigned task. 
"""
tempgdp = []
opengdp = open('Python2/Labs/gdp.txt', 'r')
for i in opengdp:
    #print(i)
    tempgdp.append([i])
#print(tempgdp)
gdp = tempgdp.split(",")
print(gdp)
#gdp = tempgdp.split("\n")



""" 
Each record has three elements: 
country name, total population and gross domestic product (GDP) in millions of dollars.
Your job is to calculate the GDP per person for each country and
print out country and GDP/person in descending order of percapita GDP.
"""


""" for cntry in gdp:
    gdp
#    print(cntry)
"""
"""
    gdp_pers = cntry.split(",")
    for entry in gdp_pers:
        print(entry[1])#, entry[2])
        gdp_pers[1] = float(entry[1]) / float(entry[2])
"""

""" 
opensplit= open('Python2/Labs/split.txt', 'r')
tempsplit= opensplit.read()
split = tempsplit.split()
print(split)
"""