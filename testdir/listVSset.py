import random
import time
import itertools

l=[]
s=set()
start = time.time()
alpha=[chr(x) for x in range(35,250)]
'''for n in range(130):
    #print 'n=',n
    alpha=[chr(x) for x in range(35+n,35+8+n)]
    perms=list(itertools.permutations(alpha))
    #print 'perms',len(perms)
    #generate a lot of non-repeating strings
    for p in perms:
        temp=''.join(p)          
        #print temp
        l.append(temp)
        s.add(temp)
'''
N=1000000
for i in range(N):
    temp=''.join(random.sample(alpha, 100))
    temp=temp+''.join(random.sample(alpha, 150))
    temp=temp+''.join(random.sample(alpha, 200))
    temp=temp+''.join(random.sample(alpha, 200))
    temp=temp+''.join(random.sample(alpha, 130))
    s.add(temp)

for e in s:
    l.append(e)

    
end = time.time()
print 'Time to build dataset',end

            
toSearch=l[random.randint(0,len(l))]
print toSearch
print len(l)
print len(s)
start = time.time()
if toSearch in l:
    print "y"
end = time.time()
print 'time for list', end - start
start = time.time()
if toSearch in s:
    print "found in set"
end = time.time()
print 'time for set', end - start

