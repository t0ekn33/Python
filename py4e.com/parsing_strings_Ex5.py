data = 'X-DSPAM-Confidence:0.8475'
atpos = data.find(':') #find starting char
print(atpos)
#sppos = data.find(' ',atpos) #find white space after starting char
#print(sppos)
host = data[atpos + 1:] #get string after starting char and before white space
#float(host)
type(host)
print(host)
