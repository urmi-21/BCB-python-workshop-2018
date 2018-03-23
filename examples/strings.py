'''
BCBGSO Basic Python workshop 3/23/2018
strings

@author urmi
'''

s='so many books, so little time'

#get length of string
l=len(s)
print "Length is "+str(l)

#print only l/3 characters from beginning

print s[:l/3]

#make first letter capital
print s.capitalize()

#count number of 'e'
print "e occurs "+str(s.count('e'))+" times"

#count number of 'tt' is latter half of the string
print "tt occurs "+str(s[len(s)/2:].count('tt'))+" times in latter half"
#len(s)/2 is the middle index in the string

#find all the words in the string
words=s.split(' ')
#the split function will split a string based on a given pattern. The words are
# separated by single space hence we use single space in split finction
print words
			
# change the word books to videogames

print s.replace('books','videogames')
print s
#print s again, the word "books" is still here because strings are immutable
# to make a new string do

s2=s.replace('books','videogames')
print s2

# add a period at the end of the line

s3=s2+'.'
print s3


# a list of string functions can be found at:
# https://docs.python.org/2/library/string.html
