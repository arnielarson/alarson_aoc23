#!/usr/bin/python3
import sys
import heapq
from functools import total_ordering

print("hello day 17")

lines = open("../data/" + sys.argv[1]).read().strip().split("\n")
grid = [[int(x) for x in line] for line in lines]

#for g in grid:
#  print(g)
NC=len(grid[0])
NR=len(grid)
ei=NR-1; ej=NC-1



""" 
  Moving through grid, minimizing "loss" (heat loss) subject to constraints..
  Idea - class, while loop, keep frontier ordered by total
  Constarints 
    - can only move in a straight line for 3 moves in a row
    - can not reverse direction.. (not that you ever would..)
    - to enforce one, sort of need to maintain some cahces?
    - not sure what the optimal strategy is.

  Obviously, want to use a heap with this problem to keep the output nodes in order
  Originally I just kept the frontier in a list and sorted it each time..

  Part 1 - constraint can move at most 3 times in a row
  Part 2 - constraint is that must move at least 4 times, and at most 10 times in a row
         - second constraing is that it needs to STOP at end point, meaning that it has to 
           be at 4 through 10

  Changes:
    - Used the heapq Python implementation
    - Used @total_ordering decorator and just implemented __lt__(self,obj)
    - Realized that a better constraint for this graph search is direction and n
      Makes the caching stragety a bit more straighforward
    - Made the mapping form direction to branches a bit cleaner
"""
 
# Move map
M = {}
M['r'] = ['r','u','d']
M['l'] = ['l','u','d']
M['u'] = ['u','r','l']
M['d'] = ['d','r','l']

@total_ordering
class Node:
  
  """
    (i,j) position on board
    x = heuristic to minimize the search space
    h = heat value of position
    s = sum # sorting condition
    CHANGE d = history of last three moves [l3, l2, l1]
    d = direction ['u','d','l','r']
    hm = history hash map of (i,j)'s
  """
  def __init__(self, i, j, s, d, n, ei=ei,ej=ej):

    self.i=i
    self.j=j
    self.s=s
    # cost = sum to this point + remaining distance
    self.c=self.s + (ei-self.i) + (ej-self.j)
    self.d=d #'r','l','u','d'
    self.n=n # 
    self.end=False

  def __lt__(self, other):
    return self.c < other.c
  
  def get_next(self, fend, part1=True):
  
    # Part 2 - min 4 in a row, max 10 in a row
    # update set of available next moves based on d[2], the last move
    if part1:
      if self.n == 3:  # must turn, skip first move in Move Mapping
        cs = M[self.d].copy()[1:]
      else:
        cs = M[self.d]
    else:
      if self.n < 4:  # must continue in direction
        cs = [self.d]
      elif self.n == 10:  # must turn, skip first move in Move Mapping
        cs = M[self.d].copy()[1:]
      else:
        cs = M[self.d]

    for d in cs:
      if d== 'r':
        if (self.j+1)==NC:
          #print(f"at boundary j:{NC}, skipping")
          pass
        else:
          h=grid[self.i][self.j+1] # grid heat cost
          if d != self.d:
            n=1
          else:
            n=self.n+1

          if (self.i,self.j+1,d,n) not in visited:
            n=Node(self.i, self.j+1,self.s+h,d,n)
            visited.add((n.i,n.j,n.d,n.n))
            heapq.heappush(F, (n.c, n)) 
            if fend(n.i,n.j):
              v= n.n>=4
              print(f"[n:{n.n} valid:{v}, end reached {n.i}, {n.j},  sum: {n.s}")
              self.end=True
      if d== 'd':
        if (self.i+1)==NR:
          #print(f"at boundary i:{NR}, skipping")
          pass
        else:
          h=grid[self.i+1][self.j]
          if d != self.d:
            n=1
          else:
            n=self.n+1
          
          if (self.i+1,self.j,d,n) not in visited: 
            n=Node(self.i+1, self.j,self.s+h,d,n)
            visited.add((n.i,n.j,n.d,n.n))
            heapq.heappush(F, (n.c,n))
            # check the node here for if it's an end node
            if fend(n.i,n.j):
              v= n.n>=4
              print(f"[n:{n.n} valid:{v}, end reached {n.i}, {n.j},  sum: {n.s}")
              self.end=True
      if d== 'l':
        if (self.j-1)==-1:
          #print(f"at boundary j:{self.j-1}, skipping")
          pass
        else:  # don't need to check end cond from left
          #if fend(self.i+1,self.j):
          #  print(f"Found end, sum={self.s+h})"
          #  self.end=True
          if d != self.d:
            n=1
          else:
            n=self.n+1
          h=grid[self.i][self.j-1]
          
          if (self.i,self.j-1,d,n) not in visited:
            n=Node(self.i, self.j-1,self.s+h,d,n)
            visited.add((n.i,n.j,n.d,n.n))
            heapq.heappush(F, (n.c,n))
      if d== 'u':
        if self.i-1==-1:
          pass
        else:  # don't need to check end cond from left
          #if fend(self.i+1,self.j):
          #  print(f"Found end, sum={self.s+h})"
          #  self.end=True
          if d != self.d:
            n=1
          else:
            n=self.n+1
          h=grid[self.i-1][self.j]
          
          if (self.i-1,self.j,d,n) not in visited:
            n=Node(self.i-1, self.j,self.s+h,d,n)
            visited.add((n.i,n.j,n.d,n.n))
            heapq.heappush(F, (n.c, n))
      
"""
  Sort - if we always sort the candidates by their total..  Then if we get to 
  the goal, this implies that we've found the correct path and can quit our search
"""

print(f"Grid has dim NC:{len(grid[0])}, NR:{len(grid)}")
GO=True
## Cached points
#  - each path has a history to avoid repeasts (hm)
#  - a global visited list (i,j,d[0],d[1],d[2])
hm=set((0,0))
# Node (i,j,h,s,d,n)
S1=Node(0,0,0,'r',0) # this will continue in r direction
S2=Node(0,0,0,'d',0) # this will continue in d direction

# how do I deal with this constraint??
# since path can continue in 3 directions.. unique key to check is (i, j, d)
# Nope - need to consider history, last three moves? [l3,l2,l1] last 3 are needed 
# to make a unique key for considering frontier nodes
# Nope - search space still too big.  Need to use heurisitc like A* w manhattan distance?
#      - or maintain history hash map??
#      - yes, in this case, no path should go back to 0,0
# Also, need heuristic, search key should be node.sum - node.manhattan_distance
# 
# And eventually realized that (i,j,d,n) is better, (d is direction and n is repeat number)

visited=set()
# I think the starting nodes, given the algorithm, needs to have the direction..
visited.add((0,0,'r',1))
visited.add((0,0,'d',1))

def fend(i,j):
  global ei; global ij
  return i==ei and j==ej

# Frontier of nodes to check, keep in heap..
# (sum + distance to end, Node)
F = []
heapq.heappush(F, (ei+ej,S1))
heapq.heappush(F, (ei+ej,S2))
c=1
while GO:
#for i in range(40):
  (j,n) = heapq.heappop(F)
  n.get_next(fend,False)
  #print(f"Pop node: {n.i}, {n.j}, {n.d}, {n.n}")
  if len(F)==0:
    GO=False
  
  
  


