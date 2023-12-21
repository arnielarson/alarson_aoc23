#!/usr/bin/python3
import sys

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
"""

class Node:
  """
    (i,j) position on board
    x = heuristic to minimize the search space
    h = heat value of position
    s = sum # sorting condition
    d = history of last three moves [l3, l2, l1]
    hm = history hash map of (i,j)'s
  """
  def __init__(self, i, j, h, s, d, ei=ei,ej=ej):

    self.i=i
    self.j=j
    
    self.h=h
    self.s=s
    self.x=self.s + (ei-self.i) + (ej-self.j)
    self.d=d #'r','l','u','d'
    #self.hm=hm.copy()  
    #self.hm.add((i,j))
    self.end=False
    
  
  def get_next(self, fend):
  
    nodes=[]
    cs = set( ['r','d','l','u'])
    # update set of available next moves based on d[2], the last move
    if self.d[2]=='r':
      cs.remove('l')
    elif self.d[2]=='l':
      cs.remove('r')
    elif self.d[2]=='u':
      cs.remove('d')
    elif self.d[2]=='d':
      cs.remove('u')
    # disallow 3 + in a row
    lm = self.d[2]
    if lm in cs and self.d[1]==self.d[0] and lm==self.d[0]:
      cs.remove(lm) 

    for c in cs:
      if c== 'r':
        if (self.j+1)==NC:
          #print(f"at boundary j:{NC}, skipping")
          pass
        #elif (self.i,self.j+1) in self.hm:
        #  pass
        else:
          h=grid[self.i][self.j+1]
          if fend(self.i,self.j+1):
            print(f" End found {self.i}, {self.j+1},  sum: {self.s+h}")
            self.end=True
          d=[self.d[1],self.d[2],c]
          if (self.i,self.j+1,d[0],d[1],d[2]) not in visited:
            n=Node(self.i, self.j+1,h,self.s+h,d)
            visited.add((n.i,n.j,n.d[0],n.d[1],n.d[2]))
            nodes.append(n)
      if c== 'd':
        if (self.i+1)==NR:
          #print(f"at boundary i:{NR}, skipping")
          pass
        #elif (self.i+1,self.j) in self.hm:  # local path check?
        #  pass
        else:
          h=grid[self.i+1][self.j]
          if fend(self.i+1,self.j):
            print(f" End found {self.i+1}, {self.j}, sum: {self.s+h}")
            self.end=True
          d=[self.d[1],self.d[2],c]
          if (self.i+1,self.j,d[0],d[1],d[2]) not in visited: #  global path check
            n=Node(self.i+1, self.j,h,self.s+h,d)
            visited.add((n.i,n.j,n.d[0],n.d[1],n.d[2]))
            nodes.append(n)
      if c== 'l':
        if (self.j-1)==-1:
          #print(f"at boundary j:{self.j-1}, skipping")
          pass
        #elif (self.i,self.j-1) in self.hm:
        #  pass
        else:  # don't need to check end cond from left
          #if fend(self.i+1,self.j):
          #  print(f"Found end, sum={self.s+h})"
          #  self.end=True
          h=grid[self.i][self.j-1]
          d=[self.d[1],self.d[2],c]
          if (self.i,self.j-1,d[0],d[1],d[2]) not in visited:
            n=Node(self.i, self.j-1,h,self.s+h,d)
            visited.add((n.i,n.j,n.d[0],n.d[1],n.d[2]))
            nodes.append(n)
      if c== 'u':
        if self.i-1==-1:
          pass
        #elif (self.i-1,self.j) in self.hm:
        #  pass
        else:  # don't need to check end cond from left
          #if fend(self.i+1,self.j):
          #  print(f"Found end, sum={self.s+h})"
          #  self.end=True
          h=grid[self.i-1][self.j]
          d=[self.d[1],self.d[2],c]
          if (self.i-1,self.j,d[0],d[1],d[2]) not in visited:
            n=Node(self.i-1, self.j,h,self.s+h,d)
            visited.add((n.i,n.j,n.d[0],n.d[1],n.d[2]))
            nodes.append(n)
    return nodes 
      
"""
  Sort - if we always sort the candidates by their total..  Then if we get to 
  the goal, this implies that we've found the correct path and can quit our search
"""

print(f"Grid has dim NC:{len(grid[0])}, NR:{len(grid)}")
GO=True
d=['','','']
## Cached points
#  - each path has a history to avoid repeasts (hm)
#  - a global visited list (i,j,d[0],d[1],d[2])
hm=set((0,0))
S=Node(0,0,grid[0][0],0,d)

# how do I deal with this constraint??
# since path can continue in 3 directions.. unique key to check is (i, j, d)
# Nope - need to consider history, last three moves? [l3,l2,l1] last 3 are needed 
# to make a unique key for considering frontier nodes
# Nope - search space still too big.  Need to use heurisitc like A* w manhattan distance?
#      - or maintain history hash map??
#      - yes, in this case, no path should go back to 0,0
# Also, need heuristic, search key should be node.sum - node.manhattan_distance

visited=set()
visited.add((0,0,'','',''))

def fend(i,j):
  global ei; global ij
  return i==ei and j==ej

l = [S]
c=1
while GO:
#for i in range(1000):
  N=l.pop()
  l=l+N.get_next(fend)
  if len(l)==0:
    GO=False
  else:
    l.sort(key=lambda q: q.x, reverse=True)
  
  
  


