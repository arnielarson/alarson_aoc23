#!python
"""
  Is a hiking map..  0's are trail head starts, and 9's are trail head end points.
  Find all the perfect trails, (0 to 9) ascending in order.
  For a trail (a 0), score is the number of 9's that are reachable 
  
  Grid: rows (down), cols (accross)
  fn search(p, i, j, slns) <- if p+1 = 9, copy soln, if valid, continue
  
  Part1: Find the number of trails (distinct 9's reachable by 0)
  Part2: Find the number of distinct paths (distnct paths reaching 9 from a 0)
  
  Simple Breadth First Search
"""

#d="../data/10a.txt"
d="../data/10b.txt"

grid=[[s for s in g] for g in open(d).read().strip().split("\n")]

class Grid():
  """
    N cols, M rows
    match((i,j,v)) i is row (-y); j is col (x)
  """
  def __init__(self, grid):
    self.grid=grid
    self.n=len(grid[0])
    self.m=len(grid)
  def print(self):
    print(self.grid)

  def match(self, args):
    """
      Match i is row, j is col
    """
    i=args[0]; j=args[1]; v=args[2]
    if i<0 or i>=self.m:
      return False
    elif j<0 or j>=self.n:
      return False
    return self.grid[i][j]==v

  # match a string to the grid 
  # expects coordinates as a list([i,j,v])
  def smatch(self, d):
    #print(f"Data to smatch: {d}")
    return 1 if all(list(map(self.match, d))) else 0

  def find(self, v):
    coords = []
    for i in range(self.m):     # rows
      for j in range(self.n):   # cols
        if self.match((i,j,v)):
          coords.append((i,j))
    return coords
        

G = Grid(grid)
G.print()
coords = G.find('0')
print(f"\nCoords: {coords}")

def search(p, i, j, s):
 if not G.match((i,j,str(p))):
   
   return
   
 # if at 9, halt, else, continue in each of 4 directions
 if p==9:   
   s.append((i,j))  
 else:
   search(p+1, i+1, j, s)
   search(p+1, i-1, j, s)
   search(p+1, i, j+1, s)
   search(p+1, i, j-1, s)

th=[]

for c in coords:
  i=c[0]; j=c[1]
  print(f"for coord: {c} i:{i}, j:{j}")
  
  s=[]
  search(1,i+1,j,s)
  search(1,i-1,j,s)
  search(1,i,j+1,s)
  search(1,i,j-1,s)
  print(f"for coord: {c} found {len(set(s))} 9s")
  th.append(len(s))
print(f"Sum of scores: {sum(th)}")
     








