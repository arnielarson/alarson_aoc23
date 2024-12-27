#!python
"""
  Another map problem...
  Find the regions..
  
  Part1: Solution is sum(area(region)*perimeter(region) for all regions
  Part2: Oh boy, now need to think about the perimeter a little more deeply,
         In part 2, only the straight edges need to be counted.  So an improved concept of tracking edges in necessary
  Another interesting solution https://www.youtube.com/watch?v=glNiVe_Rztg 
  
  Again variant of breadth first search, however, I looked at some solutions and found a pretty 
  awesome video by "hyperneutrino" - explaining floodfill.  This is an algorithm I've encountered and 
  have coded as part of AoC - but was cool to see and revisit appraoch from somone else.
  https://www.youtube.com/watch?v=KXwKGWSQvS0


  Of note - 
  Flood Fill - maintain seen entries and each region is explored in full.  Accumulate the answer..
  Area - is just the size of the region.
  Perimeter - For each element in region, check the number of adjacent elements.  (Basically each 
              element will contrinute uniquely to the number of perimeter edges)
  Also explict labeling of rows and cols makes the code much easier to read (and mentally map)
  Separately - saw an interesting solution using networkx and maintaining the grid as a complex number..
"""
from collections import deque

#d="../data/12a.txt"
d="../data/12b.txt"

grid = open(d).read()
#grid=[[s for s in g] for g in open(d).read().strip().split("\n")]

class Grid():
  """
    N cols, M rows
    match((i,j,v)) i is row (-y); j is col (x)
  """
  def __init__(self, blob):
    self.blob = blob
    self.grid = [[s for s in g] for g in blob.strip().split("\n")]
    self.cols=len(self.grid[0])
    self.rows=len(self.grid)

  def print(self, raw=False):
    if raw:
      print(self.blob)
    else:
      for row in self.grid:
        print(row)

  def val(self, i, j):
    if i<0 or i>=self.rows:
      return None
    elif j<0 or j>=self.cols:
      return None 
    return self.grid[i][j]
    

  def match(self, args):
    """
      Match i is row, j is col
    """
    i=args[0]; j=args[1]; v=args[2]
    if i<0 or i>=self.rows:
      return False
    elif j<0 or j>=self.cols:
      return False
    return self.grid[i][j]==v

  # match a string to the grid 
  # expects coordinates as a list([i,j,v])
  def smatch(self, d):
    #print(f"Data to smatch: {d}")
    return 1 if all(list(map(self.match, d))) else 0

  def findall(self, v):
    """
      Find all matches
    """
    coords = []
    for i in range(self.rows):     # rows
      for j in range(self.cols):   # cols
        if self.match((i,j,v)):
          coords.append((i,j))
    return coords
        

G = Grid(grid)
G.print(raw=True)

visited=set()
score=0
for i in range(G.rows):
  for j in range(G.cols):
    if (i,j) in visited:
      continue
    #visited.add((i,j))
    v = G.val(i,j)
    d = deque()
    d.append((i,j))       # Search space - check all region neighbors
    region=set()          # Region
    #region.add((i,j))
    #print(f"starting search for {v} at {i},{j}")
    while d:
      # dumb?  using i,j?
      (ii,jj) = d.pop()
      if (ii,jj) not in region:
        # a new region can not be already visited
        region.add((ii,jj))
        visited.add((ii,jj))
      else:
        # already included, skip
        continue

      for (di,dj) in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (ii+di,jj+dj) not in region and G.match((ii+di,jj+dj,v)):
          d.append((ii+di,jj+dj))
   
    # get perimeter
    p=0
    for (ii,jj) in region:
      # just count the number of edges that are on the permimeter..
      for (di,dj) in [(1,0),(-1,0),(0,1),(0,-1)]:
        if not G.match((ii+di, jj+dj, v)):
          p+=1
    print(f"Region {v} with size {len(region)} and perim {p}")
    score+=len(region)*p
      

print(f"Score is: {score}")
    


          
      
    
