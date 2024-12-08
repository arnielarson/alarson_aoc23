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

  Ughh.. Pt 2.  Do 1B cycles.. NWSE..
  So, if after 4 cycles, N is the same, then the cycle is stable.
  Can just emit the answer? 
"""

"""
print("\nOriginal Grid\n\n")
for g in grid:
  print(g)
"""

"""
  Mapping
    0 <=> O
    1 <=> .
"""
def tipNS(N=True):
  NC=len(grid)
  for j in range(len(grid[0])):
    i=0
    d=[]
    while i < NC:
      if grid[i][j] == 'O':
        d.append(0)
      elif grid[i][j] == '.':
        d.append(1)
      # Process block if '#' OR if at end of full block
      elif grid[i][j] == '#':
        if N:
          d.sort()
        else:
          d.sort(reverse=True)
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
        if N:
          d.sort()
        else:
          d.sort(reverse=True)
        idx = i-len(d)
        didx = 0
        #print(f"found a # at row {i}, d has len {len(d)}, idx is {idx}")
        while idx < NC:
          #print(f"assigning grid, idx {idx}, len(d) {len(d)}")
          t = 'O' if d[didx]==0 else '.'
          grid[idx][j] = t
          idx+=1
          didx+=1

## W is tipped left, e.g. sort is ordered
## E is tipped right, e.g. sort is reversed
def tipEW(W=True):
  NC=len(grid[0])
  NR=len(grid)
  for i in range(NR):
    j=0
    d=[]
    while j < NC:
      if grid[i][j] == 'O':
        d.append(0)
      elif grid[i][j] == '.':
        d.append(1)
      # Process block if '#' OR if at end of full block
      elif grid[i][j] == '#':
        if W:
          d.sort()
        else:
          d.sort(reverse=True)
        idx = j-len(d)
        didx = 0
        #print(f"found a # at row {i}, col {j} d block has len {len(d)}, idx is {idx}")
        while idx < j:
          #print(f"assigning grid, idx {idx}, len(d) {len(d)}")
          t = 'O' if d[didx]==0 else '.'
          grid[i][idx] = t
          idx+=1
          didx+=1
        d=[]
      j+=1
      # Edge case, at bottom of column 
      if j==NR and len(d) > 0:
        if W:
          d.sort()
        else:
          d.sort(reverse=True)
        idx = j-len(d)
        didx = 0
        #print(f"found a # at row {i}, d has len {len(d)}, idx is {idx}")
        while idx < NR:
          #print(f"assigning grid, idx {idx}, len(d) {len(d)}")
          t = 'O' if d[didx]==0 else '.'
          grid[i][idx] = t
          idx+=1
          didx+=1
def show():
  for g in grid:
    print(g)
   
# cycle is 4 successive tips
def cycle():
  tipNS() # North
  tipEW() # West
  tipNS(False) # South
  tipEW(False) # East

CM = {}

# Sanity check, (100-3)%7=6.  
# start = 3, so 3+6=9 and 100 should be same
"""
for i in range(1,200):
  cycle()
  if i==9 or i==100 :
    print(f"\n{i} cycles")
    show()

"""

# looking for repeating cylce?
N=10000
s=0
c=0
print(f"Trying {N} cycles of the grid looking for a cycle")
for i in range(1,N):
  cycle()
  h = hash("".join([x for row in grid for x in row]))
  
  if h in CM.keys():
    r=CM[h]
    s=r
    c=i-r
    print(f"Cycle {r} repeats on {i} cycle")
    break
  else:
    CM[h]=i


# What about 1B?  find the pattern and score for this value
N = (1000000000 - s) % c

# Advance to index, (since we're at 1, advance N-1 times
for i in range(N):
  cycle()

#print("\nOn 1B should be here:\n")
#for g in grid:
#  print(g)
    
## Score the setup
score=0
S=len(grid)
for i in range(len(grid)):
  #print(f"summing: {grid[i]}")
  score+=S*sum(map(lambda x: 1 if x=='O' else 0, grid[i]))
  S-=1

print(f"score is {score}")
  

    

