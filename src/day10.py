#!/usr/bin/python3
import re
from functools import reduce
import sys

print("hello day 10")
print("max recursion: ",sys.getrecursionlimit())
sys.setrecursionlimit(10000)


grid = open("../data/" + sys.argv[1]).read().strip().split("\n")

# fudge the boundaries
grid = ["*" + g + "*" for g in grid]
n = len(grid)
m = len(grid[0])
print(f"Now grid has dims {n} rows x {m} cols")

z = "*"*len(grid[0])
grid = [z] + grid + [z]
n = len(grid)
m = len(grid[0])
print(f"Now grid has dims {n} rows x {m} cols")



"""
  Grid is a graph of directions.  Path is a 1d "pipe" and each direction
  deterministically moves to next point.
  Pt1 find longest distance from 'S'

  Pt2 find the amount of area enclosed by the loop..
  Strategy, multi pass, ..
"""
 
print(f"grid has {len(grid)} and {len(grid[0])} cols")

class Node:
  def __init__(self, i=0,j=0,c='',d=0):
    self.i=i
    self.j=j
    self.c=c
    self.d=d
  

S = Node()
V = set()  # Pt 2 these will be the pipe nodes
E = set()  # Pt 2 I also really need the edges, (i1,j1,i2,j2)
for i in range(len(grid)):
  for j in range(len(grid[0])):
    #print(f"grid is {grid[i][j]} at row {i} col {j}")
    
    if grid[i][j]=='S':
      print(f"grid S at row {i} col {j}")
      S.i=i
      S.j=j
      S.c='S'
      break
V.add((S.i,S.j))
T=[]
# find the To set, note hand coding?  because need to use each rule baically..
if grid[S.i][S.j-1] in '-FL':
  T.append(Node(S.i,S.j-1,grid[S.i][S.j-1],1))
if grid[S.i][S.j+1] in '-J7':
  T.append(Node(S.i,S.j+1,grid[S.i][S.j+1],1))
if grid[S.i-1][S.j] in '|F7':
  T.append(Node(S.i-1,S.j,grid[S.i-1][S.j],1))
if grid[S.i+1][S.j] in '|JL':
  T.append(Node(S.i+1,S.j,grid[S.i+1][S.j],1))

print(f"Start node {S.i}, {S.j}")
for t in T:
  print("To node: ", t.i, t.j, t.c, ' distance: ',t.d)
    
D=0
# VIM hack, recall, global replace over lines is :lnN,lnMs/foo/bar/g  to fix multiple lines
# simultaneously follow pipe in each direction..
# for each to node, determine what the next node should be, should just be a single direciton
# 
def move(fr, to):
  end = False
  n=[]
  assert len(fr) == len(to)
  for i in range(len(fr)):
    E.add((fr[i].i, fr[i].j, to[i].i, to[i].j))
    
    V.add((to[i].i,to[i].j))
    #print(f"To idx: {i}, loc:  {to[i].i},{to[i].j}, distance: {to[i].d}")
    if to[i].j > fr[i].j:  # right '-J7
      if to[i].c == '-':      # right
        n.append(Node(to[i].i, to[i].j+1, grid[to[i].i][to[i].j+1], to[i].d+1))
      elif to[i].c == 'J':    # up
        n.append(Node(to[i].i-1, to[i].j, grid[to[i].i-1][to[i].j], to[i].d+1))
      elif to[i].c == '7':    # down
        n.append(Node(to[i].i+1, to[i].j, grid[to[i].i+1][to[i].j], to[i].d+1))
    elif to[i].j < fr[i].j:  # left '-FL'
      if to[i].c == '-':      # left
        n.append(Node(to[i].i, to[i].j-1, grid[to[i].i][to[i].j-1], to[i].d+1))
      elif to[i].c == 'L':    # up
        n.append(Node(to[i].i-1, to[i].j, grid[to[i].i-1][to[i].j], to[i].d+1))
      elif to[i].c == 'F':    # down
        n.append(Node(to[i].i+1, to[i].j, grid[to[i].i+1][to[i].j], to[i].d+1))
      
    elif to[i].i > fr[i].i:  # down '|F7'
      if to[i].c == '|':      # down (i++)
        n.append(Node(to[i].i+1, to[i].j, grid[to[i].i+1][to[i].j], to[i].d+1))
      elif to[i].c == 'L':    # right
        n.append(Node(to[i].i, to[i].j+1, grid[to[i].i][to[i].j+1], to[i].d+1))
      elif to[i].c == 'J':    # left
        n.append(Node(to[i].i, to[i].j-1, grid[to[i].i][to[i].j-1], to[i].d+1))
    else:  # up
      if to[i].c == '|':      # up (i--)
        n.append(Node(to[i].i-1, to[i].j, grid[to[i].i-1][to[i].j], to[i].d+1))
      elif to[i].c == 'F':    # right
        n.append(Node(to[i].i, to[i].j+1, grid[to[i].i][to[i].j+1], to[i].d+1))
      elif to[i].c == '7':    # left
        n.append(Node(to[i].i, to[i].j-1, grid[to[i].i][to[i].j-1], to[i].d+1))
    

  # end if already visited
  assert len(to) == len(n)
  for node in n:
    if (node.i,node.j) in V:
      # Max distance is node.d - 1, as should have exited before adding this node
      print(f"finished {node.i},{node.j} with distance {node.d}")
      # get the last edges
      end=True
  if end:
    for i in range(len(to)):
      E.add((to[i].i,to[i].j, n[i].i,n[i].j))
      return 0
  move(to,n)


move([S,S],T)

# Pt 2 - now we have the pipe coords, need to find number of interior points
# however, treated like a maze, topologically interior points, off top of head
# this adds a ton of complexity and exterior stuff to track, 
# Including:
#  - Edges to determine topology
#  - midpoints - convenience representation to check edge boundaries?
#  - Interior points
#  - Interior midpoints

n=len(grid)     # num rows
m=len(grid[0])  # num cols
grid2=[]        # rows of strings

#print(f"creating grid with {n} rows {m} cols")

for i in range(n):
  grid2.append(['*']*m)
for c in V:
  grid2[c[0]][c[1]]='O'
  
# seems I have to pass left right to get candidates.. then pass up down to add to total..
# NOPE, this is treated like a maze, topologically, so for each interior candidate
# I somehow need to determine if it is fully blocked in..  
# To sort of check the topology, I'm going to keep the existing grid layout, and infer
# midpoints on the grid with the values m1,m2 = (i+1/2, j+1/2)
C = set()
IM = set()
EM = set()
IP = set()



for i in range(n):
  rb=0
  lb=0
  j=m-1
  while j > 0:
    if grid2[i][j]=='O': 
      rb=j
      break
    j-=1
  j=0
  while j < m:
    if grid2[i][j]=='O': 
      lb=j
      break
    j+=1
  # set interior candidates..
  for j in range(lb+1,rb):
    if grid2[i][j]=='*':
      grid2[i][j] = '.'
      C.add((i,j))

# visualize the set up now?  Next need to check interior points..
#for row in grid2:
#   print("".join(row))

# exterior if at boundary, or adjacent to exterior (will shorten search..)
# midpoint(m1,m2), has vertices (m1,m2), (m1+1,m2), (m1,m2+1),(m1+1,m2+1)
def is_exterior(m1,m2):
  if (m1,m2) in EM:
    return True
  if grid2[m1][m2]=='*':
    EM.add((m1,m2))
    return True 
  if grid2[m1+1][m2]=='*':
    EM.add((m1,m2))
    return True 
  if grid2[m1+1][m2+1]=='*':
    EM.add((m1,m2))
    return True 
  if grid2[m1][m2+1]=='*':
    EM.add((m1,m2))
    return True 
  return False

def is_interior(m1,m2):
  if (m1,m2) in IM:
    return True
  return False

# explore possible adjacent midpoints, check edge boundaries
# check T,B,L,R
def get_adj(m1,m2): 
  m=[]
  # top
  if ((m1,m2,m1,m2+1) not in E) and ((m1,m2+1,m1,m2) not in E):
    m.append((m1-1,m2))
  # botom
  if ((m1+1,m2,m1+1,m2+1) not in E) and ((m1+1,m2+1,m1+1,m2) not in E):
    m.append((m1+1,m2))
  # left
  if ((m1,m2,m1+1,m2) not in E) and ((m1+1,m2,m1,m2) not in E): 
    m.append((m1,m2-1))
  # right
  if ((m1,m2+1,m1+1,m2+1) not in E) and ((m1+1,m2+1,m1,m2+1) not in E):
    m.append((m1,m2+1))
  return m
  
  
def mps(c1,c2):
  return set([(c1-1,c2-1),(c1-1,c2),(c1,c2-1),(c1,c2)])
  
#for (i1,j1,i2,j2) in E:
#  print(f" Edge: {i1},{j1}  {i2},{j2}")

for (i,j) in C:
  #print(f"Need to check interior point {i},{j}")
  # 
  # for each midpoint: 
  #   - check if it's interior
  #     Y: all midpoints are interior
  #   - check if it's exterior
  #     Y: all midpoints are exteriors
  #   - else check adjacent midpoints
 
  exterior=False
  n=0

  b=mps(i,j)
  c=set()
  while len(b) > 0:
    n+=1
    mp = b.pop()
    c.add(mp)
    if is_exterior(mp[0],mp[1]):
      exterior=True
    else:
    
      for x in get_adj(mp[0],mp[1]):
        #print(f"Found adjacent midpoint: {x}")
        if x not in c:
          b.add(x)
  #print(f"Point {i},{j} is ext {exterior}, checked {n} midpoints")
  if exterior:
    #print(f"Point {i},{j} is exterior")
    for mp in c:
      EM.add(mp)
  else:
    print(f"Point {i},{j} is interior")
    IP.add((i,j))
    for mp in c:
      IM.add(mp)

print(f"Found {len(IP)} interior points:\n")
  
    
        
        








