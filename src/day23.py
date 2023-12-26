#!/usr/bin/python3
import sys
import heapq
from copy import deepcopy
from functools import total_ordering

print("hello day 22")
"""
  Day 23 - Find the longest possible path??
         - Contraint is >^<v
  
  Part1 - find *longest* path - probably need to try all..
        - paths can't cross - obv, but, needs to be considered
        - seems they make this tractable with a judicious choice
          of initial map
   
"""

lines = open("../data/" + sys.argv[1]).read().strip().split("\n")
grid = [[x for x in line] for line in lines]
NR=len(grid)
NC=len(grid[0])
print(f"grid has rows: {NR} and cols: {NC}")

def print_grid():
  for g in grid:
    print (g)

#print_grid()

class Path:
  def __init__(self,i,j,moves=None):
    self.i=i
    self.j=j
    self.moves = moves.copy() if moves else set()
    self.moves.add((i,j))
    self.cont = True
    

  def move(self, PL, L):
    i=self.i; j=self.j; n=0
    move=None
    #print(f"Move: ({i},{j})")
    #if ((i+1,j) not in self.moves) and ( grid[i+1][j]=='.' or grid[i+1][j]=='v'):
    if (i+1,j) not in self.moves and  grid[i+1][j]!='#':
      n+=1
      move=(1,0)
    if ((i-1,j) not in self.moves) and grid[i-1][j]!='#':
      n+=1
      if n>1:
        p=Path(i-1,j,self.moves) ## will copy moves and add cur move
        PL.append(p)
      else:
        move=(-1,0)
    if ((i,j+1) not in self.moves) and grid[i][j+1]!='#':
      n+=1
      if n>1:
        p=Path(i,j+1,self.moves)
        PL.append(p)
      else:
        move=(0,1)
    if ((i,j-1) not in self.moves) and grid[i][j-1]!='#':
      n+=1
      if n>1:
        p=Path(i,j-1, self.moves)
        PL.append(p)
      else:
        move=(0,-1)

    if n==0:
      #print(f"stuck at {i},{j}")
      self.cont=False
    else:  # update current move at end so other paths are correct
      self.i+=move[0]
      self.j+=move[1]
      self.moves.add((self.i,self.j))

    if self.i==(NR-1):
      #print(f"Found end, {self.i},{self.j};  len: {len(self.moves)}")
      L.append(len(self.moves))
      self.cont=False

# Start is  0,1,  end is row=NR-1
S=Path(0,1)
P=[S]
L=[]

while len(P) > 0:
  p=P.pop()
  while p.cont:
    p.move(P,L)

# account for Start
print(f"Max length is: {max(L)-1}")
