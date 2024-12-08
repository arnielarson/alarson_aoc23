#!/usr/bin/python3
import re
from functools import reduce
from collections import defaultdict
import sys

print("hello day 18")

data = open("../data/" + sys.argv[1]).read().strip().split("\n")
data = map(lambda x: x.split(), data)
# part 1
# inst = list(map(lambda x: [x[0],int(x[1]),x[2].lstrip("(").rstrip(")")],data))
# part 2
inst2 = list(map(lambda s: [s[-1],s[:-1]] , map(lambda x: x[2].lstrip("(#").rstrip(")"),data)  ))

for i in inst2:
  print( i[0],int(i[1],16) )

# Instruction set are 2d directions
M={}
M['3']=[-1,0]
M['1']=[1,0]
M['2']=[0,-1]
M['0']=[0,1]

# BEGIN PART 2
S=[0,0]
V=[]
B=0   # maintain length of boundary
for i,l in inst2:
  D=M[i]
  L=int(l,16)
  B+=L
  S[0]+=D[0]*L
  S[1]+=D[1]*L
  V.append(S.copy())


for v in V:
  print(v)


A=0; L=len(V);
for i in range(L):
  i2=(i+1)%L
  A+=(V[i][1] - V[i2][1])*(V[i][0] + V[i2][0])
  
print(f"Computing sum: {A}")
print(f"Computing shoelace: {A//2}")
print(f"Computing total points A + b/2 + 1: {A//2 + B//2 + 1}")
# END PART2 
exit()
  
  
  

"""
  Part 1 - Sum the interior + boundary created by the instruction set
         - [R|L|U|D] N #COLOR
         - Following intructions creates a boundary
  
  Couldn't think of a neat or easy way to find the interior points
  I tried to run passes horizontal and vertical until I realized it just
  wasn't going to work.  So I came up with another generative strategy.

  Strategy - Generate the boundary points (i,j) (count boundary nodes
           - Find a left line, and mark the right side as Interior
           - Use this point as the start index
           - determine the direction of the next node
           - traverse the boundary adding points on the interior.  
           - from this set of interior points should be able to expand out into space
           - runs pretty quickly for part 1

  Part 2 - My first solution will not work, (enumerating each point)  
           In part 2 the instructions are to move a 5 digit hex number of spaces.  So there will 
           be a humungous number of interior points, and boundary points
           Solution I believe is to use geometry, something called the shoelace theorem..

           https://en.wikipedia.org/wiki/Shoelace_formula

"""
# start: 0,0
i=0; j=0
def emp():
  return []
B=defaultdict(emp)

S=[0,0] # arbitrary start location..
R=[0,0] # track the row dimensions..
C=[0,0] # track the col dimensions
V=[]    # track the vertices (path) 
O=[]    # track the initial set of interior points


for line in inst:
  c=0
  while c < line[1]:
    d=M[line[0]]  # update space
    S[0]+=d[0]; S[1]+=d[1] # pt 2 use the second code in hex
    V.append(S.copy())
    c+=1
    R[0]=min(R[0],S[0])
    R[1]=max(R[1],S[0])
    C[0]=min(C[0],S[1])
    C[1]=max(C[1],S[1])

    
NR=R[1]-R[0]+1
NC=C[1]-C[0]+1

print(f"R: {R} NR: {NR};  C: {C}, NC: {NC}, grid points: {NR*NC}")
for i in range(10):
  print(f"Looking at vertices: {V[i][0]}, {V[i][1]}")
exit()



grid=[]
for r in range(NR):
  grid.append(['.']*NC)


# map v to grid coords..
V=[[x[0]-R[0],x[1]-C[0]] for x in V]


for v in V:
  #i=v[0]-R[0]; j=v[1]-C[0]
  i=v[0]; j=v[1]
  grid[i][j]='#'
  
def print_grid():
  for g in grid:
    #print(g)
    row="".join(g)
    print(row)

"""
  - find a possible start node
  - get index for that node
  - get direction of the first move
"""
def get_start():
  for i in range(1,NR-1):
    for j in range(NC):
      if grid[i][j]=='#' and grid[i][j+1]=='.':
        return [i,j]

def get_start_idx(s):
  for i in range(len(V)):
    if V[i]==s:
      return i


# Couldn't think of a better way to maintain direction of interior
# Obviously I should be using matrices here.. probably would have
# taken far less time than this monstrosity
# return direction of new location to check
def rotate(d1,d2,c):
  if d1==(-1,0) and d2==(0,1) and c == (0,1):  return (1,0)      # U-> R; R-> D (R)
  elif d1==(-1,0) and d2==(0,1) and c == (0,-1):  return (-1,0)  # U-> R; L-> U (R)
  elif d1==(-1,0) and d2==(0,-1) and c == (0,1):  return (-1,0)  # U-> L; R-> U (L)
  elif d1==(-1,0) and d2==(0,-1) and c == (0,-1):  return (1,0)  # U-> L; L-> D (L)
  #
  elif d1==(1,0) and d2==(0,1) and c == (0,1):  return (-1,0)    # D-> R; R-> U (L)
  elif d1==(1,0) and d2==(0,1) and c == (0,-1):  return (1,0)    # D-> R; L-> D (L)
  elif d1==(1,0) and d2==(0,-1) and c == (0,1):  return (1,0)    # D-> L; R-> D (R)
  elif d1==(1,0) and d2==(0,-1) and c == (0,-1):  return (-1,0)  # D-> L; L-> U (R)
  #
  elif d1==(0,1) and d2==(1,0) and c == (1,0):  return (0,-1)    # R-> D; D-> L (R)
  elif d1==(0,1) and d2==(1,0) and c == (-1,0):  return (0,1)    # R-> D; U-> R (R)
  elif d1==(0,1) and d2==(-1,0) and c == (1,0):  return (0,1)    # R-> U; D-> R (L)
  elif d1==(0,1) and d2==(-1,0) and c == (-1,0):  return (0,-1)  # R-> U; U-> L (L)
  #
  elif d1==(0,-1) and d2==(-1,0) and c == (-1,0):  return (0,1)  # L-> U; U-> R (R)
  elif d1==(0,-1) and d2==(-1,0) and c == (1,0):  return (0,-1)  # L-> U; D-> L (R)
  elif d1==(0,-1) and d2==(1,0) and c == (-1,0):  return (0,-1)  # L-> D; U-> L (L)
  elif d1==(0,-1) and d2==(1,0) and c == (1,0):  return (0,1)    # L-> D; D-> R (L)

# Updates the grid, and updates list O
def update(c):
  if grid[c[0]][c[1]]=='.':
    grid[c[0]][c[1]]='o'
    O.append([c[0],c[1]])
    

def traverse():
  s=get_start()
  print(f"Start node: {s}")
  i=get_start_idx(s)
  print(f"Idx: {i}")
  i+=1
  n=V[i]
  # start with direction and check direction
  d=(n[0]-s[0],n[1]-s[1])
  c=(0,1) if d==(-1,0) else (0,-1)
  L=len(V)
  print(f"Start index: {i}, v:{s} and next:{n}, dir:{d}")
  #exit()
  for t in range(L-1):
    i+=1
    s=n
    n=V[i%L]
    nd=(n[0]-s[0],n[1]-s[1])
    if d!=nd:   # continue
      c2=rotate(d,nd,c)
      #print(f"dir change from {d} to {nd}")
      #print(f"rotate from {c} to {c2}") 
      c=c2
    update([n[0]+c[0],n[1]+c[1]])
    d=nd
    #print(f"Start index: {i%L}, v:{s} and next:{n}, dir:{d}")
      

def fill():
  c=1; N=10
  nO=[]
  for o in O:
    F=[o]
    while len(F) > 0:
      v=F.pop()  # removes last element "efficiently"
      if v[0]>0:
        if grid[v[0]-1][v[1]]=='.':
          grid[v[0]-1][v[1]]='o'
          F.append([v[0]-1,v[1]])
          nO.append([v[0]-1,v[1]])
      if v[0]<NR-1:
        if grid[v[0]+1][v[1]]=='.':
          grid[v[0]+1][v[1]]='o'
          F.append([v[0]+1,v[1]])
          nO.append([v[0]+1,v[1]])
      if v[1]>0:
        if grid[v[0]][v[1]-1]=='.':
          grid[v[0]][v[1]-1]='o'
          F.append([v[0],v[1]-1])
          nO.append([v[0],v[1]-1])
      if v[1]<NC-1:
        if grid[v[0]][v[1]+1]=='.':
          grid[v[0]][v[1]+1]='o'
          F.append([v[0],v[1]+1])
          nO.append([v[0],v[1]+1])
      if c%N==0:
        N*=10
        print(f"Filling, i:{i}, len(O):{len(O)}")
      c+=1
  return nO
          

    
    
traverse()
print(f"Boundary sizes: {len(V)}, O size: {len(O)}")
O+=fill()
s=len(V)+len(O)
print(f"Filled, sum:{s} = {len(V)} + {len(O)}")
print_grid()


