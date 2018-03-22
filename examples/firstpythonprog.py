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


#lists
flowers = ['Orchid','Carnation','Sunflower','Marigold']
print flowers[2:]
print len(flowers[2:])
print len(flowers[2])
flowers.remove('Orchid')
flowers.append(564)
#flowers.extend(3.1415)
print flowers

#sets
s=set() #creates empty set
s.add(1) #add to set
print s
s=set([1,2,3,4,5,1,2,6,7,2]) #creates set from give list
print s
s=set('Mississippi')
print s

#dict
d = {} #empty dict
d[1]='value 1'
d[2]='value 2'
print d
d = {1:'value1',2:'value2',3:'value3'}
print d[1]
d['x']='valueNA'
print d

i=0
for i in range(10):
    print i
print i

#if else
grades=True
gf=False
gaming=True
if (grades and gf and not gaming):
	print "no money"
elif(grades and gaming and not gf):
	print "no social life"
elif(not grades and gaming and gf):
	print "no career"
elif(grades and gf and gaming):
	print "Impossible"


#break continue
mylist = [1,2,3,4,5,6,7,8]
for i in mylist:
    if (i % 2==0):
        continue
    if (i == 7):
        break
    print i

#sum inside loop
n=5
totalsum=0			#important to initialize sum
for x in range(n+1):
    totalsum=totalsum+x		#adds numbers 0 till 5
print totalsum	


#scopes
x1=10		#a has global scope
def func():
    x2=10
    x1=5
    print "x2 in func:",x2	#prints b=10
    print "x1 in func:",x1		#prints a=5
    
func()
print "x1 in main:",x1		#prints a=10	
print "x2 in main:",x2		#error b is not defined, its scope ended with the function
