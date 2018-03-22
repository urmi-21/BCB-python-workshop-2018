'''
BCBGSO Basic python workshop
Exercise 1
'''


#Don't change this
stringDNA='ACATCCAGGGATACATCCAGGATCCAATCCAATCCAATCCAGAATCCAGACATAATCCATATCATCCAGCCGAATCCACGAGATCCAACATATAATCCATACGAATCCAGAGAGACTAATCCATATATATCCAATGCAACGAGACATGACAT'
stringMotif='ATCCA'
'''
Given above is an arbitary DNA sequence and a small motif. Write your code for the following problems
'''
#1. What is the length of the given DNA sequence and the motif ? Print your answers on a single line using a single print statement
print "length DNA:",len(stringDNA),"length motif:",len(stringMotif)

#2. How many times the motif occurs in the DNA sequence (search only non-overlapping occurrences)
print stringDNA.count(stringMotif)

#3. Out of the total occurences, what percent of ocuurences are in the second half of the DNA sequence? Hint: use slice operator to divide DNA sequence
print stringDNA[len(stringDNA)//2:].count(stringMotif)/float(stringDNA.count(stringMotif))*100,"%"



#Don't change this
stringEncrypted='pTDnfulxYZzom5DeKxYZquDPklyxYZwTtPhxYZTxYZjDnxedxYZgrTveyTrd'
'''
The above string is encrypted by replacing a few characters to other numbers and characters. Fortunately, know the decryption key is as follows:
xYZ=blankspace
T=a
5=b
P=c
D=i
K=s
Hint: Remember a string is immutable to replace a character in a string you have to store it in a new variable.
'''
# Can you decipher the text? Print you answer below
print stringEncrypted.replace('xYZ',' ').replace('T','a').replace('5','b').replace('P','c').replace('D','i').replace('K','s')
print """
sdas
"""
