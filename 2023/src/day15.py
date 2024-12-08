#!/usr/bin/python3
import re
from functools import reduce
from collections import defaultdict
import sys

print("hello day 15")

G = open("../data/" + sys.argv[1]).read().strip()
C = G.split(",")

def h(s):
  c=0; i=0;
  while i < len(s):
    c+=ord(s[i])
    c*=17
    c%=256
    i+=1
  return c
  
#for s in C:
#  print(s, h(s))

"""
Part 1 is straightforward
print(sum(map(h, C)))
"""

def emp():
  return []
Box = defaultdict(emp)


# 2 operations = and -
for s in C:
  if '=' in s:
    l=s.split("=")
    
    print(f"code {s} at hash {h(l[0])}")
    # modify list
    add = True
    box = Box[h(l[0])]
    for b in box:
      if b[0] == l[0]:
        b[1]=l[1]
        add = False
        break
    if add:
      box.append(l)
    
  else: # '-'  
    l=s[:-1]
    print(f"code {s} has hash {h(l)}")
    box = Box[h(l)]
    # may have to deal with doubles..
    d = []
    for i in range(len(box)):
      print(f"checking key {l} to remove: {box[i]}")
      if box[i][0]==l:
        d.append(i)
    offset=0
    for idx in d:
      box.pop(idx+offset)
      offset+=1
        
         
fp=[]
# score?
for k in Box.keys():
  b=int(k)
  box=Box[k]
  i=0
  while i < len(box):
    fp.append((b+1)*(i+1)*int(box[i][1]))
    i+=1

print(f"FP: {sum(fp)}")  



