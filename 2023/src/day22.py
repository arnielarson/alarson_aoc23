#!/usr/bin/python3
import sys
import heapq
from functools import total_ordering

print("hello day 22")
"""
  Day 22 - Basically represents bricks in 3d space.
         - First the bricks settle in the z direction, without changing orientation
         - Then determine how many bricks can be removed, e.g. are 
"""

lines = open("../data/" + sys.argv[1]).read().strip().split("\n")
bricks = {}
bid=1
for line in lines:
  b=line.split("~")
  bricks[bid]=[bid,[int(x) for x in b[0].split(",")],[int(x) for x in b[1].split(",")]]
  bid+=1
  

XR=[0,0]
YR=[0,0]
ZR=[0,0]
# Brick helper functions
def get_xyz(brick):
  x1=brick[1][0]
  x2=brick[2][0]
  y1=brick[1][1]
  y2=brick[2][1]
  z1=brick[1][2]
  z2=brick[2][2]
  return (x1,x2,y1,y2,z1,z2)
def get_minz(brick):
  return min(brick[1][2],brick[2][2])

# check range of x, y, z
for k in bricks.keys():
  brick = bricks[k]
  x1,x2,y1,y2,z1,z2 = get_xyz(brick)
  #print(f"brick: {brick}")
  if x1 < XR[0]: XR[0]=x1
  if x2 < XR[0]: XR[0]=x2
  if x1 > XR[1]: XR[1]=x1
  if x2 > XR[1]: XR[1]=x2
  if y1 < YR[0]: YR[0]=y1
  if y2 < YR[0]: YR[0]=y2
  if y1 > YR[1]: YR[1]=y1
  if y2 > YR[1]: YR[1]=y2
  if z1 < ZR[0]: ZR[0]=z1
  if z2 < ZR[0]: ZR[0]=z2
  if z1 > ZR[1]: ZR[1]=z1
  if z2 > ZR[1]: ZR[1]=z2
    

print(f"Grid Dims: XR: {XR}, YR: {YR}, ZR: {ZR}")

# grid, fill in with 0's, then fill in the bricks..
grid = []
for i in range(XR[0],XR[1]+1):
  grid.append([])
  for j in range(YR[0],YR[1]+1):
    z=[0]*(ZR[1]+1)
    grid[i].append(z)


# Sanity checking grid
#print(f"grid[0][0][0] = {grid[0][0][0]}")
#print(f"grid[2][0][0] = {grid[2][0][0]}")
#print(f"grid[0][2][8] = {grid[0][2][9]}")


# Set up the grid
for k in bricks.keys():
  brick = bricks[k]
  x1,x2,y1,y2,z1,z2 = get_xyz(brick)
  #print(f"brick: {brick}")
  if x1 != x2:
    for x in range(min(x1,x2),max(x1,x2)+1):
      grid[x][y1][z1]=brick[0]
      #print(f"\tAdding brick {brick[0]} at {x},{y1},{z1}")
  elif y1 != y2:
    for y in range(min(y1,y2),max(y1,y2)+1):
      grid[x1][y][z1]=brick[0]
      #print(f"\tAdding brick {brick[0]} at {x1},{y},{z1}")
  elif z1 != z2:
    for z in range(min(z1,z2),max(z1,z2)+1):
      grid[x1][y1][z]=brick[0]
      #print(f"\tAdding brick {brick[0]} at {x1},{y1},{z}")

def print_grid():
  for g in grid:
    print(g)
#print_grid()

# Set up bricks to sort / sift
sift = []
for k in bricks.keys():
  z=get_minz(bricks[k])
  heapq.heappush(sift,(z,k)) 

##
# Sorting/Sifting Brick
#   - sort by z in heapq (lowest pops first)
#   - drop in z
#
# check if can drop the brick.  If so, drop, return True
def drop(brick):
  x1,x2,y1,y2,z1,z2 = get_xyz(brick)
  if min(z1,z2)==1: # already at bottom
    return False

  if x1!=x2:
    for x in range(min(x1,x2),max(x1,x2)+1):
      if grid[x][y1][z1-1]!=0:
        return False
    for x in range(min(x1,x2),max(x1,x2)+1):
      grid[x][y1][z1-1]=brick[0]
      grid[x][y1][z1]=0
    brick[1][2]=z1-1
    brick[2][2]=z1-1
    return True
  elif y1!=y2:
    for y in range(min(y1,y2),max(y1,y2)+1):
      if grid[x1][y][z1-1]!=0:
        return False
    for y in range(min(y1,y2),max(y1,y2)+1):
      grid[x1][y][z1-1]=brick[0]
      grid[x1][y][z1]=0
    brick[1][2]=z1-1
    brick[2][2]=z1-1
    return True
  else: # z
    z0=min(z1,z2)
    if grid[x1][y1][z0-1]!=0:
      return False
    else:
      zm=max(z1,z2)
      grid[x1][y1][z0-1]=brick[0]
      grid[x1][y1][zm]=0
      brick[1][2]=z1-1
      brick[2][2]=z2-1
      return True
  print("drop [INVALID STATE]")
  return False
    
  
# Sort / sift bricks - if nothing under, move down (to z=1)
while len(sift)>0:
  b=heapq.heappop(sift)
  brick=bricks[b[1]]
  while drop(brick):
    pass


#print("Sorted bricks")
#for k in bricks.keys():
#  print(f"Brick now: {bricks[k]}")

#print_bricks()

S={}
##
# Ok now determine how many can be "disintegrated"
# Track which bricks support which
# S: [set(supporting), set(supported by)]
# 
# Can delete brick if 
#  - not supporting any bricks
#  - each brick that it is supporting is also being supported by another brick..
##
for k in bricks.keys():
  brick = bricks[k]
  x1,x2,y1,y2,z1,z2 = get_xyz(brick)
  ss=[set(),set()]
  S[brick[0]]=ss
  if x1!=x2: 
    for x in range(min(x1,x2),max(x1,x2)+1):
      g=grid[x][y1][z1+1]
      if g!=0:
        print(f"\tbrick {brick[0]} supporting {g}")
        ss[0].add(g)
    if z1!=1:  # not at bottom
      for x in range(min(x1,x2),max(x1,x2)+1):
        g=grid[x][y1][z1-1]
        if g!=0:
          ss[1].add(g)
        print(f"\tbrick {brick[0]} supported by {g}")
  elif y1!=y2: 
    for y in range(min(y1,y2),max(y1,y2)+1):
      g=grid[x1][y][z1+1]
      if g!=0:
        print(f"\tbrick {brick[0]} supporting {g}")
        ss[0].add(g)
    if z1!=1:  # not at bottom
      for y in range(min(y1,y2),max(y1,y2)+1):
        g=grid[x1][y][z1-1]
        if g!=0:
          ss[1].add(g)
          print(f"\tbrick {brick[0]} supported by {g}")
  else:  # check z
    if z1!=1:
      g=grid[x1][y1][z1-1]
      print(f"\tbrick {brick[0]} supported by {g}")
      ss[1].add(g)
    g=grid[x1][y1][z2+1]
    if g!=0:
      print(f"\tbrick {brick[0]} supporting {g}")
      ss[0].add(g)
    
## Part 2 - which bricks would cause a chain reaction..
# T is set of bricks which cause topples..
T=set()
DD=0
for k in bricks.keys():
  ss = S[k]
  print(f"checking brick {k}")
  discard=True
  for s in ss[0]:
    if len(S[s][1])==1:
      discard=False
      T.add(k)
      print(f"brick {k} is only brick supporting brick {s}")
  print(f"brick {k} discardable:{discard}")
  if discard:
    DD+=1

print(f"Part1 discrable: {DD}")

##
#  Part 2 - Determine which brick will have the most destruction if pulled
#
      
  
      



