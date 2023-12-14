#!/usr/bin/python3
import re
from functools import reduce
import sys

print("hello day 14")

grid = open("../data/" + sys.argv[1]).read().strip().split("\n")
grid=[[s for s in g]for g in grid]

"""
  Grid is a field with rocks.. # are stationary, O can roll,  . are just space, ..
  tilt and rocks will roll up (north)
  Strategy:
    For each column
      parse blocks into [0,1,0,1..] 
      sort block and replace
      should be roughly nlogn per column, or m*nlogn

  Ughh.. Pt 2.  Do 
"""

#for g in grid:
#  print(g)

"""
  Mapping
    0 <=> O
    1 <=> .
"""
NC=len(grid)
for j in range(len(grid[0])):
  #print(f"sorting col {j}")
  i=0
  d=[]
  while i < NC:
    if grid[i][j] == 'O':
      d.append(0)
    elif grid[i][j] == '.':
      d.append(1)
    # Process block if '#' OR if at end of full block
    elif grid[i][j] == '#':
      d.sort()
      idx = i-len(d)
      didx = 0
      #print(f"found a # at row {i}, d has len {len(d)}, idx is {idx}")
      while idx < i:
        #print(f"assigning grid, idx {idx}, len(d) {len(d)}")
        t = 'O' if d[didx]==0 else '.'
        grid[idx][j] = t
        idx+=1
        didx+=1
      d=[]
    i+=1
    # Edge case, at bottom of column 
    if i==NC and len(d) > 0:
      d.sort()
      idx = i-len(d)
      didx = 0
      #print(f"found a # at row {i}, d has len {len(d)}, idx is {idx}")
      while idx < i:
        #print(f"assigning grid, idx {idx}, len(d) {len(d)}")
        t = 'O' if d[didx]==0 else '.'
        grid[idx][j] = t
        idx+=1
        didx+=1
      

#for g in grid:
#  print(g)
    
## Score the setup
score=0
S=len(grid)
for i in range(len(grid)):
  print(f"summing: {grid[i]}")
  score+=S*sum(map(lambda x: 1 if x=='O' else 0, grid[i]))
  S-=1

print(f"score is {score}")
  

    

