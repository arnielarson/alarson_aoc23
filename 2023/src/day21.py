#!/usr/bin/python3
import sys
import heapq
from functools import total_ordering

print("hello day 21")

lines = open("../data/" + sys.argv[1]).read().strip().split("\n")
grid = [[x for x in line] for line in lines]

#for g in grid:
#  print(g)
NC=len(grid[0])
NR=len(grid)

S=(0,0)
for i in range(NR):
  for j in range(NC):
    if grid[i][j]=='S':
      S=(i,j)

f=set()
f.add(S)
N=64
for i in range(N):
  nf=set()
  for p in f:
    i=p[0]; j=p[1]
    if i<NR-1 and grid[i+1][j]!='#': 
      nf.add((i+1,j))
    if i>0 and grid[i-1][j]!='#': 
      nf.add((i-1,j))
    if j>0 and grid[i][j-1]!='#': 
      nf.add((i,j-1))
    if j<NC-1 and grid[i][j+1]!='#': 
      nf.add((i,j+1))
  f=nf


print(f"Start: {S}")
print(f"After {N} steps, {len(f)} possible locations")

    



