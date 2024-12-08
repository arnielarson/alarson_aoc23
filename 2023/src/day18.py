#!/usr/bin/python3
import re
from functools import reduce
from collections import defaultdict
import sys

print("hello day 18")

data = open("../data/" + sys.argv[1]).read().strip().split("\n")
data = map(lambda x: x.split(), data)
data = map(lambda x: [x[0],int(x[1]),x[2].lstrip("(").rstrip(")")],data)

"""
  Part 1 - Sum the interior + boundary created by the instruction set
         - [R|L|U|D] N #COLOR
         - Following intructions creates a boundary

  Strategy - Generate the boundary points (i,j)
           - Cache the points:  i: [j1,j2,j3,j4,j5,j6,..]
           - Cases, adjacent, (skip, this is the boundary_
  
  Nope - throwing that out..  I did a recursive soln, but won't work for Part 2
       - Need to use the shoelace formula as someone posted
  
  Shoelace gives area, Picks formula gives area in terms of interior + boundary points on discrete grid:
       - Pick's theorem: A = i + b/2 -1
       - Then number of points is i + b => = A + b/2 + 1

"""

def sl(V):
  t=0
  L=len(V)
  for i in range(L): 
    i2=(i+1)%L
    t+=(V[i][0]+V[i2][0])*(V[i][1]-V[i2][1])
  t=t//2
  return t

S=[0,0]

M={}
M['U']=[-1,0]
M['D']=[1,0]
M['L']=[0,-1]
M['R']=[0,1]

V=[]
# maintain the size of the boundary
B=0

# Adds vertex points, 
for e in data:
  d=M[e[0]]
  B+=e[1]
  S[0]+=d[0]*e[1]; S[1]+=d[1]*e[1]
  V.append(S.copy())
  #print(f"Instruction: {e[0]}, {e[1]}")

for v in V:
  print(f"V: {v}")


print(f"shoelace area(V): {sl(V)}")
NT=sl(V) + B//2 + 1
print(f"num points A + b/2 + 1: {NT}")






