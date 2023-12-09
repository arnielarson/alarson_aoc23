#!/usr/bin/python3
import re
from functools import reduce
from math import gcd
import sys


## example p1 = 6440

print("hello day 8")

data = open("../data/" + sys.argv[1]).read().split("\n\n")

inst = data[0]
raw = data[1].strip().split("\n")
print(f"Inst: {inst}\n\n Parsing raw: \n")
#print(raw)
k = []
g = {}

# start/end conditions in parsing below
start=[]
end=[]

for r in raw:
  row = r.split("=")
  k=row[0].strip()
  if k[2]=='A':
    print(f"Found 'A' {k}")
    start.append(k)
  if k[2]=='Z':
    print(f"Found 'Z' {k}")
    end.append(k)
  #if not start:
  #  start=k
  #  print(f"Selecting {k} as start node")
  s=row[1].lstrip(" (").rstrip(")").split(", ")
  #if s[0]==s[1]:
  #  print(f"Found terminal node: {k} => ({s[0]},{s[1]})")
  #print(s)
  g[k] = s



""" 
  Now start and end is a set..
  And traversing  the graph simultaneously until 
  all members of the end end set are met.
  
  In theory, if a single node gets to the end in 10,000 steps..
  Then the prob that one of the traversals is at an end node
  is ~ (1/6)*(1/10,0000) or ~ (1/1000)
  
  The prob that all members of the end set are simultaneously 
  reached is ~ (1/1000)^6 with 6 nodes being mapped per step

  This is likely a larger number than I can brute force,
  So it turns out that looking for cycles and using some 
  math was needed and much hair pulling ensued.
"""

print(f"Starting: {start}\nEnding: {end}")


"""
  0. Look at using GCD in python
  1. Look at a couple inputs, how does the path cycle?
    a. Oh, they do cycle.  So find least common multiple
  2. lcm(a,b) = a*b/gcd(a,b), gcd = greatest common denominator
  3. I didn't know this off hand, saw this in other peoples code..
  4. So keep track of cycles.. to find the first "ghost" output

"""

cycles = [-1]*len(start)
steps=0
go=True
idx=0
node=[s for s in start]

while go:
  steps +=1
  if idx == len(inst):
    idx=0
  l=inst[idx]=='L'
  idx+=1
  midx=0 if l else 1
  
  for i in range(len(node)):
    node[i] = g[node[i]][midx]

  # Look at the outputs..
  for i,n in enumerate(node):
    if n[2]=='Z':
      print(f"cycle end: step = {steps}, i = {i}, end = {n}")
      if cycles[i] < 0:
        cycles[i]=steps
  
    
    if -1 not in cycles:
      go=False
print(cycles)
      
# LCM, e.g 2,3,10 = LCM 6,10 = 30
lcm = reduce(lambda a,b : a*b//gcd(a,b), cycles)
print(f"LCM is {lcm}")
  
  
      
 





