'''
BCBGSO Basic Python workshop
Exercise 5

@author urmi
'''

'''
The file names contain names of transcripts and another file lengths contains coressponding
lengths of the transcripts.
Answer the following. 
'''

#1. Read the two files into two lists names and lengths
with open('C:\Users\mrbai\Documents\GitHub\BCB-python-workshop-2018\exercises\\data\\names.txt') as f:
    names=f.read().splitlines()
    print len(names)
with open('C:\Users\mrbai\Documents\GitHub\BCB-python-workshop-2018\exercises\\data\\lengths.txt') as f:
    lengths=f.read().splitlines()
print len(lengths)
#convert string to int
len_int=[]
for x in lengths:
    len_int.append(int(x))

#2. Which transcript are biggest and shortest
# hint max function gives the maximum element in a list

maxL=max(len_int)
print maxL
#get index of max
print names[len_int.index(maxL)]


#3. How many transcripts have the same length. Hint: Use set. Save results as a file
# e.g. n transcripts have length x and so on
# len(set(len_int)) have unique
setLens=set(len_int)

for s in setLens:
    print len_int.count(s),"have length",s
    

