#!/usr/bin/python
from itertools import combinations

"""
  
  A cool looking Grid problem.. 
  Part 1 - Find antinodes, find number of unique anti nodes

  In grid - each group of antennas (with common char)
  Will create two anti nodes..
  
  Part 1 - Find the number of antinodes?
  Part 2 - Multiple antinodes - so, just need to extend the creation of antinodes, and include the antenna pos 

"""

#d="../data/8a.txt"
d="../data/8b.txt"

grid=[[s for s in g] for g in open(d).read().strip().split("\n")]


class Grid():
  """
    Reusable Grid like class..
  """
  def __init__(self, grid):
    self.grid=grid
    self.n=len(grid)
    self.m=len(grid[0])

  def print(self):
    for r in self.grid:
      print(f"{''.join(r)}")
 
  """
    Find location of not chars
    return first non-conforming char
  """
  def find_not(self, c=['.','#']):  
    for i in range(self.n):
      for j  in range(self.m):
        if self.get(i,j) not in c:
          return (i,j,self.get(i,j))
    return None
   

  """ 
    Find location of char c
  """
  def find(self, c):  
    for i in range(self.n):
      for j  in range(self.m):
        if c==self.get(i,j):
          return (i,j)
    return (-1,-1)


  def match(self, args):
    i=args[0]; j=args[1]; v=args[2]
    if i<0 or i>=self.n:
      return False
    elif j<0 or j>=self.m:
      return False
    return self.grid[i][j]==v
 
  def set(self,i,j,e):
    if i<0 or i>=self.n:
      return False
    elif j<0 or j>=self.m:
      return False
    self.grid[i][j]=e
    return True
    
  def get(self,i,j):
    if i<0 or i>=self.n:
      return False
    elif j<0 or j>=self.m:
      return False
    return self.grid[i][j]

  def get_batches(self, ignore=['.']):
    """  
      Get the unique chars in the grid, return as a 
      dictionary with elems : [(x,y) .. ]
    """
    r={}
    for i in range(self.n):
      for j in range(self.m):
        e=self.get(i,j)
        if e not in ignore:
          if e in r:
            r[e].append((i,j))
          else:
            r[e]=[(i,j)]
    return r


  # match a string to the grid 
  # expects coordinates as a list([i,j,v])
  def smatch(self, d):
    #print(f"Data to smatch: {d}")
    return 1 if all(list(map(self.match, d))) else 0


G = Grid(grid)
G.print()

def get_nodes(a):
  n=[]
  for (i,j) in combinations(list(range(len(a))),2):
    dx=a[j][0]-a[i][0]
    dy=a[j][1]-a[i][1]
    n.append((a[i][0]-dx,a[i][1]-dy))
    n.append((a[j][0]+dx,a[j][1]+dy))

  return n

def get_nodes2(a):
  n=[]
  for (i,j) in combinations(list(range(len(a))),2):
    dx=a[j][0]-a[i][0]
    dy=a[j][1]-a[i][1]
    # Add the nodes until out of bounds..
    k=0
    while True:
      if not G.get(a[i][0]-k*dx,a[i][1]-k*dy):
        break
      n.append((a[i][0]-k*dx,a[i][1]-k*dy))
      k+=1
      
    k=0
    while True:
      if not G.get(a[j][0]+k*dx,a[j][1]+k*dy):
        break
      n.append((a[j][0]+k*dx,a[j][1]+k*dy))
      k+=1
      
  return n

def viz_nodes(n):
  for (i,j) in n:
    G.set(i,j,"#")
  G.print()

def part1():
  """
    antennas, create anti nodes..
  """
  an=[]
  a=G.get_batches()
  print(a)
  for k,v in a.items():
    an+=get_nodes2(v)
  
  viz_nodes(an)
  
  s=set(filter(lambda x: G.get(x[0],x[1]), [ x for x in an ]))
  #for (i,j) in s:
  #  print(f"Node: {i},{j}")
  print(f"Num nodes: {len(s)}")

  

part1()

