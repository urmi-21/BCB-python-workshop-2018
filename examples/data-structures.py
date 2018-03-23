'''
BCBGSO Basic Python workshop 3/23/2018
data structures

@author urmi
'''
#lists
flowers = ['Orchid','Carnation','Sunflower','Marigold']
print flowers[2:]
print len(flowers[2:])
print len(flowers[2])
flowers.remove('Orchid')
flowers.append(564)
flowers.extend(['Roses','Tulips'])
#flowers.extend(3.1415) #doesn't work as 3.1415 is not iterable
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
