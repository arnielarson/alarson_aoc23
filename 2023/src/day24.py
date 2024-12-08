#!/usr/bin/python3
import sys
import heapq
from copy import deepcopy
from functools import total_ordering

print("hello day 24")
"""
  Day 24 - Hailstones (x1,x2,x3,v1,v2,v3) find if paths intersect within boundary..
         - Part 1 - check for path intersection in (x,y) plane
         - Very naive algorithm:  O(N^2) to check all combinations
           For each combination, check two see if their paths intersect,
           and also check that the collision is forwards in time and 
           that the collision occurs within a bounding box.

  Part 2 - If you make a "magical" throw at an integer position with integer
           velocity you can collide with every hailstone in the set.
           This could be a search problem in a space with 6 degrees of freedom
           But there's probably a way to solve this with linear algebra..
        
"""

lines = open("../data/" + sys.argv[1]).read().strip().split("\n")

Dmin=int(sys.argv[2]) if len(sys.argv)>2 else 7
Dmax=int(sys.argv[3]) if len(sys.argv)>2 else 27
print(f"Part1 - test area min: {Dmin}, max: {Dmax}")

def tostone(line):
  d=line.split("@")
  return d[0].split(",")+d[1].split(",")

stones = [[int(x) for x in tostone(line)] for line in lines]

#for hs in stones:
#  print(hs)

##
#  Basic geomerty?  to get intersection between two lines (in xy plane)
#  Get intersection point between two lines y = mx + b
#  Convert lines to mx + b, find intersection
#
#  Next
#    - test if within bounds..
#    - test if forward in time..
##
def geti(m1,b1,m2,b2):
  if m1==m2:
    return False
  assert m1!=m2
  x=(1/m1)*(b2-b1)/(1-m2/m1)
  y=m1*x + b1
  return (x,y)

def mxpb(x0,y0,v0x,v0y):
  tb=-x0/v0x
  b=y0+v0y*tb
  m=v0y/v0x
  return (m,b)

def get_stone(i):
  s=stones[i]
  return (s[0],s[1],s[3],s[4])

def is_forward(x0,v0,x1,v1,p):
  t1= (p-x0)/v0
  t2= (p-x1)/v1
  return (t1>0 and t2>0)

def in_box(px,py,Dmin,Dmax):
  return (px<Dmax and px > Dmin) and (py<Dmax and py>Dmin)

## 
#  Tests
#    - m=1, b=0 (line up and right) x m=-1, b=4 (line up and left)
#    - same with x0,y0,vx0,vy0
##
print(f"Testing interstion (should be 2,2): {geti(1,0,-1,4)}")
print(f"Same test starting from iniital conditions")
(m1,b1)=mxpb(0,0,1,1)
(m2,b2)=mxpb(4,0,-1,1)
print(f"Testing (same) interstion (should be 2,2): {geti(m1,b1,m2,b2)}")


## 
#  Part 1
#    - for each pair, get intersection 
#    - and test if it's in the bounding box..
#    - and test that it's forward in time..
#    - count intersections
##
count=0
for i in range(len(stones)-1):
  for j in range(i+1,len(stones)):
    print(i,j)
    x1,y1,vx1,vy1=get_stone(i)
    x2,y2,vx2,vy2=get_stone(j)
    (m1,b1)=mxpb(x1,y1,vx1,vy1)
    (m2,b2)=mxpb(x2,y2,vx2,vy2)
    if m1!=m2:
      px,py=geti(m1,b1,m2,b2)
      # test fowar
      f=is_forward(x1,vx1,x2,vx2,px)
      print(f"Intersection found, forward in time: {f}")
      v=in_box(px,py,Dmin,Dmax)  # box is symmetric in x,y
      print(f"Intersection found, in box: {v}")
      print(f"{i},{j} intersetc at({px},{py})")
      if f and v:
        count+=1
    else:
      print(f"{i},{j} do not intersect")

print(f"Count of valid intersections: {count}")
      


