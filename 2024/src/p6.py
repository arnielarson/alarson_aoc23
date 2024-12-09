#!/usr/bin/python
"""
  
  Another Grid problem.. 
  Reusing Grid class, with boundary checking
  
  self.grid[i][j]   
  N rows, M Cols
  0 . . . -> M-1
  .
  .
  .
  |
  v
  N-1


  Part 1 - easy enough - follows a deterministic Path
  Part 2 - Find all possible paths that a SINGLE obstruction would cause a loop to occur??
  I'm sure there's a trick?  Brute force, try every open square, add an obstruction.  Run teh 
  siulation and see if a loop occurs or if the guard leaves the board..

"""

#d="../data/6a.txt"
d="../data/6b.txt"

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


  # match a string to the grid 
  # expects coordinates as a list([i,j,v])
  def smatch(self, d):
    #print(f"Data to smatch: {d}")
    return 1 if all(list(map(self.match, d))) else 0


G = Grid(grid)
#G.print()

def part1():
  start = G.find_not()
  G.set(start[0],start[1],".")
  dirs = [(-1,0),(0,1),(1,0),(0,-1)]; tdx=0

  print(f"Start is at {start[0]},{start[1]}, sym is {start[2]}")
  loc=(start[0],start[1])
  elems = set(); elems.add(loc)
  c=0
  while True:
    c+=1
    if c>10000:
      print("counter berak")
      break
    next = G.get(loc[0]+dirs[tdx][0], loc[1]+dirs[tdx][1])
    if next == ".":  
      loc=(loc[0]+dirs[tdx][0] , loc[1]+dirs[tdx][1])
      elems.add(loc)
    elif next == "#":
      tdx=(tdx+1)%4 
    else: 
      break
  print(f"Finished at Location {loc[0]},{loc[1]}")
  print(f"Counter: {c}, squares: {len(elems)}")

  # algo is, collect locations that pass.  Always make a right

def part2():
  start = G.find_not()
  G.set(start[0],start[1],".")
  dirs = [(-1,0),(0,1),(1,0),(0,-1)]; tdx=0
  print(f"Start is at {start[0]},{start[1]}, sym is {start[2]}")

  
  t=0
  cy=0
  for i in range(G.n):
    for j in range(G.m): 
      if i==start[0] and j==start[1]:
        print(f"At start, skip")
        pass
      elif G.get(i,j)==".":
        t+=1
        tdx=0
        c=True
        G.set(i,j,"#")
        loc=(start[0],start[1])
        elems = set(); elems.add((loc[0],loc[1],dirs[tdx]))
        while c:
          cur = (loc[0],loc[1],tdx)
          if cur in elems:
            print(f"Found Cycle at {i},{j}") 
            c=False
            cy+=1
          else:
            elems.add(cur)
            next = G.get(loc[0]+dirs[tdx][0], loc[1]+dirs[tdx][1])
            if next == ".":  
              loc=(loc[0]+dirs[tdx][0] , loc[1]+dirs[tdx][1])
            elif next == "#":
              tdx=(tdx+1)%4 
            else: 
              #print(f"Path ends without a cycle")
              c=False
        G.set(i,j,".")
  print(f"Tested {t} objects")
  print(f"Found {cy} cycles")


part2()

    





