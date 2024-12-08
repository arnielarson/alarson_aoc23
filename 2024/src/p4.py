#!/usr/bin/python
"""
  Let's take a second to try to remember if I can make stuff somewhat clever..
  Creating a grid with multiple lines of text

  Testing boundaries of a grid..  (n rows, m cols)

"""

#d="data/4a.txt"
d="data/4b.txt"

grid=[[s for s in g] for g in open(d).read().strip().split("\n")]


class Grid():
  def __init__(self, grid):
    self.grid=grid
    self.n=len(grid[0])
    self.m=len(grid)
  def print(self):
    print(self.grid)

  def match(self, args):
    i=args[0]; j=args[1]; v=args[2]
    if i<0 or i>=self.n:
      return False
    elif j<0 or j>=self.m:
      return False
    return self.grid[i][j]==v

  # match a string to the grid 
  # expects coordinates as a list([i,j,v])
  def smatch(self, d):
    #print(f"Data to smatch: {d}")
    return 1 if all(list(map(self.match, d))) else 0

G = Grid(grid)
#G.print()
print(G.match((3,4,'X')))
print(G.match((0,5,'X')))
print(all(list(map(G.match, [(1,1,'M'),(1,2,'X')]))))


# Part 2 - looking for 2 diagonal MAS matches..
def matchd(i,j,s="MAS"):
  s=[x for x in s]
  d=[-1,0,1]
  i=[i]*3; j=[j]*3
  yd = [a+b for a,b in zip(i,d)]
  xr = [a+b for a,b in zip(j,d)]
  D1= any([G.smatch(list(zip(yd,xr,s))), 
           G.smatch(list(zip(yd[::-1],xr[::-1],s)))]) 
  D2= any([G.smatch(list(zip(yd[::-1],xr,s))), 
           G.smatch(list(zip(yd,xr[::-1],s)))]) 
  return 1 if D1 and D2 else 0

# Part 1
def matches(i,j,s="XMAS"):
  s=[x for x in s]
  t=0
  d=[0,1,2,3]
  i=[i]*4; j=[j]*4  # i is rows (up/down) j is cols (left/right)
  yd = [a+b for a,b in zip(i,d)]
  yu = [a-b for a,b in zip(i,d)]
  xl = [a-b for a,b in zip(j,d)]
  xr = [a+b for a,b in zip(j,d)]
  # combinations: 8, 
  t+=G.smatch(list(zip(i,xr,s)))
  t+=G.smatch(list(zip(i,xl,s)))
  t+=G.smatch(list(zip(yu,j,s)))
  t+=G.smatch(list(zip(yd,j,s)))
  t+=G.smatch(list(zip(yu,xr,s)))
  t+=G.smatch(list(zip(yd,xr,s)))
  t+=G.smatch(list(zip(yu,xl,s)))
  t+=G.smatch(list(zip(yd,xl,s)))
  return t
  
total=0
for i in range(G.n):
  for j in range(G.m):
    total+=matchd(i,j)
print(total)
    
