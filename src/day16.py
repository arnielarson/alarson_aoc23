#!/usr/bin/python3
import sys

print("hello day 16")

lines = open("../data/" + sys.argv[1]).read().strip().split("\n")
grid = [[x for x in line] for line in lines]


"""
  A beam is passing through the grid, it can continue, reflect or split!
  . is empty space
  \ and / are mirrors changing the direction
  | and - are splitters, splitting the beam in two at 90 deg angle from direction
    or allowing it to pass through along the direction of travel.
 
  Find how many tiles are energized.. that is the number of tiles that are covered
  for the grid configuration and initial starting conditions, e.g 0,0 moving right (0,1)
  
  B is set of points e.g. answer
  BE is set of point + direction so we don't create infintie number of beams..
  
  Part 2 just checked for the best configuration, starting the beam at any 
  point on the perimiter 
"""

class Beam:
  def __init__(self, i,j,vi,vj,valid=True):
    self.i=i
    self.j=j
    self.vi=vi
    self.vj=vj
    self.s=0  # maintain steps to exit out of a endless loop?
    self.valid=valid


E=set()
BE=set()
# each beam has a location/direction
B = Beam(0,0,0,1)

NR=len(grid)
NC=len(grid[0])
## Need to track the beams
Beams=[B]


def check(Beams):
  GO=True
  while GO:
  #for i in range(35):
    New=[]
    checked=0

    #print(f" Begin: {len(Beams)} in set")
    for B in Beams:

      #print(f"Checking Beam at: {B.i}, {B.j} valid: {B.valid}")
      # check for in grid
      if not B.valid:
        continue
      if B.i<0 or B.i>=NR or B.j<0 or B.j>=NC:
        #print(f"Beam: {B.i}, {B.j} being set to invalid:")
        B.valid=False
        continue
      #if B.s > NR*NC:
      #  B.valid=False
      #  continue
  
      key = (B.i,B.j,B.vi,B.vj)
      if key in BE:
        B.valid=False # we've already hit this point from this direction
        continue
      BE.add(key)
      E.add((B.i,B.j))
  
      checked+=1
     
      c=grid[B.i][B.j]
  
      if c=='.':
        B.i+=B.vi; B.j+=B.vj
  
      elif c=='|':
        if B.vj:
          #print("Splitting |")
          C=Beam(B.i,B.j,B.vi,B.vj)
          B.vi=1; B.vj=0;
          B.i+=B.vi
          C.vi=-1; C.vj=0;
          C.i+=C.vi
          New.append(C)
        else:
          B.i+=B.vi 
          
      elif c=='-':
        if B.vi:
          #print("Splitting -")
          C=Beam(B.i,B.j,B.vi,B.vj)
          B.vj=1; B.vi=0
          B.j+=B.vj
          C.vj=-1; C.vi=0
          C.j+=C.vj 
          New.append(C)
        else:
          B.j+=B.vj
      elif c=='\\':
        #print(f"Mirror {c}") 
        if B.vi==0:
          vi=1 if B.vj==1 else -1
          B.vj=0
          B.vi=vi
          B.i+=B.vi
  
        else: # vj==0
          vj=1 if B.vi==1 else -1
          B.vi=0
          B.vj=vj
          B.j+=B.vj
      elif c=='/':
        #print(f"Mirror {c}") 
        if B.vi==0:
          vi=-1 if B.vj==1 else 1
          B.vj=0
          B.vi=vi
          B.i+=B.vi
        else: # vj==0
          vj=-1 if B.vi==1 else 1
          B.vi=0
          B.vj=vj
          B.j+=B.vj
      else:
        B.i+=B.vi; B.j+=B.vj
  
    #print(f"Checked {checked} beams")
    if checked==0:
      GO=False
    Beams+=New
      
  
    
# Part 1    
check(Beams)
print(f"E = {len(E)}")

size=0
# Part 2:
for i in range(NR):
  E.clear()
  BE.clear()
  # each beam has a location/direction
  B = Beam(i,0,0,1)
  ## Need to track the beams
  Beams=[B]
  check(Beams)
  if len(E) > size:
    size=len(E)
  E.clear()
  BE.clear()
  # each beam has a location/direction
  B = Beam(i,NC-1,0,-1)
  ## Need to track the beams
  Beams=[B]
  check(Beams)
  if len(E) > size:
    size=len(E)
    
for j in range(NC):
  E.clear()
  BE.clear()
  # each beam has a location/direction
  B = Beam(0,j,1,0)
  ## Need to track the beams
  Beams=[B]
  check(Beams)
  if len(E) > size:
    size=len(E)
  E.clear()
  BE.clear()
  # each beam has a location/direction
  B = Beam(NR-1,j,-1,0)
  ## Need to track the beams
  Beams=[B]
  check(Beams)
  if len(E) > size:
    size=len(E)
    
print(f"Size is now: {size}")






    

