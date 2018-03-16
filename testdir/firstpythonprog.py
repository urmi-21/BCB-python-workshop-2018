# This is a single line comment
'''
This
is a
multiline
comment
'''
#printing different line
print "OK Computer"
print "Yes"
#printing same line
print "OK Computer",
print "OKNOTOK"

stringA="A string in double quotes"
stringB='A string in single quotes'
stringC='''A multiline
        String in triple quotes'''

print stringA
print stringB
print stringC

s='belisha beacon'
print s.capitalize()
print s.count('a')
print s.replace('e','xx')
index=s.find('sha')
print 'sha occurs at '+str(index)
print s[1:5].replace('b','')+s[5:]

stringD='Blackstar'
print stringD[2:5]
print stringD[4:]
print stringD[:-1]
print stringD[-4:-1]
print stringD[-3:-4]

var='A string'
print type(var)
var=2
print type(var)

a=10
b=15
c=3.0
print a+b
print b+c
print a-b
print b-c
print a*b
print b*c
print b/a
print b/c
print b/float(a)
print float(b)/a
print b%a
print a%c
print a**b
print a**c
print b//a
print b//c
print b//float(a)
print float(b)//a

#generate encrypted
s='painful zombies quickly watch a jinxed graveyard'
print s.replace(' ','xYZ').replace('a','T').replace('b','5').replace('c','P').replace('i','D').replace('s','K')
print s
print s.replace('xYZ',' ').replace('T','a').replace('5','b').replace('P','c').replace('D','i').replace('K','s')

stringDNA='ACATCCAGGGATACATCCAGGATCCAATCCAATCCAATCCAGAATCCAGACATAATCCATATCATCCAGCCGAATCCACGAGATCCAACATATAATCCATACGAATCCAGAGAGACTAATCCATATATATCCAATGCAACGAGACATGACAT'
stringMotif='ATCCA'
print stringDNA.count(stringMotif)
print stringDNA[:len(stringDNA)//2].count(stringMotif)
print stringDNA[len(stringDNA)//2:].count(stringMotif)
print stringDNA[len(stringDNA)//2:].count(stringMotif)/float(stringDNA.count(stringMotif))*100

