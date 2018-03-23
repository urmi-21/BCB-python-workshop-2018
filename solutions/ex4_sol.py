'''
BCBGSO Basic Python workshop
Exercise 4

@author urmi
'''

#1. We know len() returns the length of a string. Define a function that takes a string as an argument
# and prints its squared length. E.g. if input to function is 'ABCD' return value should be 16.

def lenSquare(s):
    return len(s)**2


s='abc'
print lenSquare(s)

#2. Write another function that takes two strings as arguments and returns the sum of square of lengths of the two Strings.
# E.g. if in put to function is 'ABC' and 'DE' return value should be 9+4=13.

def lenSquare2(t,u):
    return len(t)**2+len(u)**2

t='dafg'
u='vwxyz'

print lenSquare2(s,t)
print lenSquare(u)


#3. Let me define a term "Pythagorean string triplets" as set of three strings such that squared length of any one is
# equal to the sum of the squared lengths of other two. Given three strings check whether they form a pythagorean string triplet.
# Hint: You don't have to check each possible combination, just check if the largest string's squared length is equal to
# sum of squared lengths of the other two.

#find largest string
largest=t
if len(s) > len(t) and len(s) > len(u):
    if lenSquare2(t,u)==lenSquare(s):
        print 'Found Pythagorean string triplets'
elif len(u) > len(s) and len(u) > len(t):
    if lenSquare2(s,t)==lenSquare(u):
        print 'Found Pythagorean string triplets'

if lenSquare2(u,s)==lenSquare(t):
        print 'Found Pythagorean string triplets'


