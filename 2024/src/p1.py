#!/usr/bin/python

import math
from collections import defaultdict

i="1b.txt"
j=f"data/{i}"
with open(j) as f:
  d=f.readlines() # -> returns a list with each line
  d=[x.strip().split() for x in d]

l=[]; r=[]
for i, j in d:
  l.append(int(i))
  r.append(int(j))

l.sort()
r.sort()
r0={}
d=0

for i in range(len(l)):
  #print(l[i], r[i])
  if r[i] in r0:
    r0[r[i]]+=1
  else:
    r0[r[i]]=1
  


# Part 2 - in right list, make an occurent map.  
# sum is now l[i] * occ[r[i]]

for i in range(len(l)):
  v=l[i]
  if v in r0:
    d+=v*r0[v]

print(f"Part 2 sim score: {d}")



