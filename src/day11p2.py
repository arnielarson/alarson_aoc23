#!/usr/bin/python3
import re
from functools import reduce
import sys

print("hello day 11")
"""
  Part 2 - the graph, (universe w/ expansion) is modified
  to have "large" expansions for each empty row or column
  Should be able to just add "large" expansion every time a node 
  goes through an expansion col or row.
  However, instead of implicit distances, now distances will 
  depend on path.  However, also, paths from A to B will be consistent
  Still map back to manhattan distance in terms of steps. 
  So.. maybe use a node class to manage the distances
"""
   	


grid = open("../data/" + sys.argv[1]).read().strip().split("\n")
grid=[[s for s in g]for g in grid]

# expand space... first by row
re=[]
for i in range(len(grid)):
  if "#" not in grid[i]:
    re.append(i)

ce = []
for j in range(len(grid[0])):
  c=True
  for i in range(len(grid)):
    if grid[i][j]=='#':
      c=False
  if c:
    ce.append(j)

ER=1000000
print("expansion rows: ",re)
print("expansion cols: ",ce)
print("Expansion Rate: ",ER)


# Ok, now need to find the Manhattan distance between all galaxiy pairs..
# probably a BFS problem?
# First populate the galaxies with numbers..
# Then add a Node class and manage distances

G={}   # {g: (i,j)}
GN=[]  # [g]
D={}   # distances: {(g1,g2):d}
class Node:
  def __init__(self,i=0,j=0,d=0):
    self.i=i
    self.j=j
    self.d=d
  def __eq__(self,other):
    if isinstance(other, Node):
      return (self.i==other.i) and (self.j==other.j)
    else:
      return False
  def __ne__(self,other):
    return not self.__eq__(other)
  def __repr__(self):
    return(f"i:{self.i},j:{self.j},d:{self.d}")
  def __hash__(self):
    return hash((self.i,self.j))

for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j]=='#':
      g=str(len(G)+1)
      G[g]=(i,j)
      GN.append(len(G))
      grid[i][j]=g

for g in grid:
  print("".join(g))

NC = len(grid[0])
NR = len(grid)

# re = row expansion idx's
# ce = col expansion idx's 
def get_front(s):
  
  
  nodes = []
  if s.i>0:
    d=s.d
    d += ER if (s.i-1) in re else 1
    n=Node(s.i-1,s.j,d)
    nodes.append(n)
  if s.i<(NR-1):
    d=s.d
    d += ER if (s.i+1) in re else 1
    n=Node(s.i+1,s.j,d)
    nodes.append(n)
  if s.j>0:
    d=s.d
    d += ER if (s.j-1) in ce else 1
    n=Node(s.i,s.j-1,d)
    nodes.append(n)
  if s.j<(NC-1):
    d=s.d
    d += ER if (s.j+1) in ce else 1
    n=Node(s.i,s.j+1,d)
    nodes.append(n)
  return nodes

print("Galaxies: ")
for g,k in G.items():
  print(f"\t{g} , {k}")

# BFS - foreach g in G
# for g in GN:  # 1 to (N-1) find g-1 distances
def getd(g):
  # start coords
  ig=G[str(g)][0]
  jg=G[str(g)][1]
  f=0
  start=Node(ig,jg,0)
  #print(f"Start node: {start}")
  searched = set(); searched.add(start)
  frontier = set()
  for n in get_front(start):
    frontier.add(n)
    #print(f"initial frontier is: {n}")
  
  
  # continue until found between 
  while f < len(GN)-g:
    candidates = set()
    while len(frontier) > 0:
      n = frontier.pop()
      key = grid[n.i][n.j]
      # found a galaxy
      if key in G.keys():
        gkey=(str(g),key) if int(g) < int(key) else (key,str(g))
        if gkey in D.keys():  # already found
          if D[gkey] > n.d:
            D[gkey]=n.d  # possible? 
        else:  # add found distance
          f+=1
          #print(f"Found {f}th distance {d} from {g} to {key}")
          D[gkey]=n.d
      for c in get_front(n):
        candidates.add(c)
      searched.add(n)

    # move on to next frontier
    for c in candidates:
      if c not in searched:
        frontier.add(c)
    #for n in frontier:
    #print(f"Frontier {n}")

for g in GN:
  getd(g)
#getd(8)  ## can debug with just 1



#for k,v in D.items():
#  print(f"Distance {k} is {v}")

print(f"Sum is {sum(D.values())}")


