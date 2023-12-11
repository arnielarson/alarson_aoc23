#!/usr/bin/python3
import re
from functools import reduce
import sys

print("hello day 11")


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


print("expansion rows: ",re)
print("expansion cols: ",ce)

offset=0
for i in re:
  s=i+offset
  grid=grid[:s] + [['.']*len(grid[0])] + grid[s:]
  offset+=1

offset=0
for j in ce:
  s=j+offset
  for i in range(len(grid)):
    grid[i].insert(s,".")
  offset+=1


# Ok, now need to find the Manhattan distance between all galaxiy pairs..
# probably a BFS problem?
# First populate the galaxies with numbers..

G={}   # {g: (i,j)}
GN=[]  # [g]
D={}   # distances: {(g1,g2):d}

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
def addf(i,j):
  
  nodes = []
  if i>0:
    nodes.append((i-1,j))
  if i<(NR-1):
    nodes.append((i+1,j))
  if j>0:
    nodes.append((i,j-1))
  if j<(NC-1):
    nodes.append((i,j+1))
  return nodes

print("Galaxies: ")
for g,k in G.items():
  print(f"\t{g} , {k}")

# BFS - foreach g in G
# for g in GN:  # 1 to (N-1)
def getd(g):
  # find g-1 distances
  ig=G[str(g)][0]
  jg=G[str(g)][1]
  f=0
  d=1
  searched = set(); searched.add((ig,jg))
  #print(f"searched set = {searched}")
  frontier = set()
  for (i,j) in addf(ig,jg):
    #print(f"G {g} at {G[str(g)][0]},{G[str(g)][1]}, add node {i},{j}")
    frontier.add((i,j))
  #print(f"initial frontier is: {frontier}")
  
  
  # continue until found between 
  while f < len(GN)-g:
    candidates = set()
    for idx in range(len(frontier)):
      n = frontier.pop()
      key = grid[n[0]][n[1]] 
      if key in G.keys():
        gkey=(str(g),key) if int(g) < int(key) else (key,str(g))
        #print(f"Checking galaxy {gkey} at {n[0]},{n[1]}")
        if gkey in D.keys():  # already found
          if D[gkey] > d:
            D[gkey]=d  # possible 
        else:  # found distance
          f+=1
          #print(f"Found {f}th distance {d} from {g} to {key}")
          D[gkey]=d
      for c in addf(n[0],n[1]):
        candidates.add(c)
      searched.add(n)
    # move on to next frontier, increment distance stpes
    d+=1
    for c in candidates:
      if c not in searched:
        frontier.add(c)
    #for n in frontier:
    #  print(f"Frontier d:{d}, {n}")

for g in GN:
  getd(g)
  # getd(8)  ## can debug with just 1



for k,v in D.items():
  print(f"Distance {k} is {v}")

print(f"Sum is {sum(D.values())}")


