#!python
"""
   Part 1: Find the cheapest ways to beat the claw machine.  Moving in dx, dy with costs
           1. Are there solutions?
           2. Find the cheapest solution.

       X    Y
   A: +94, +34
   B: +22, +67
      8400,5400
   
   Solutions are mA(dx1) + mB(dx2)=8400
                 mA(dy1) + mB(dy2)=5400        
   2 equations, 2 unknowns

   Cost C=4*mA + mB
   Need to minimize cost
 
   Hah - Brute Force solution, why not?  (always going to the right.. )
   https://www.youtube.com/watch?v=-5J-DAsWuJc

   Using numpy, becaue why not?  np.linalg.solve(M,B)
   But, then validating the solutions is integer...
   Rouding errors galore.
   Solution:  Validate that the int vals are a solution..

   Note - really wanted to use round(X), int will truncate a number like 40 when rep is 39.99999999
   Took a ton of tried to get this fully right..

"""
import re
import numpy as np


games = open("../data/13b.txt").read().strip().split("\n\n")

tokens=0
# Note easier way to parse the board, take the 3 lines, and parse and assign to variables..
# ax, ay, bx, by, A, B = map(int, re.findall(r"\d+", game)):
for game in games:
  r=game.split("\n")
  # Solution is just if there are integer A and B..
  r1=[np.int64(x) for x in re.findall(r"\d+",r[0])]
  r2=[np.int64(x) for x in re.findall(r"\d+",r[1])]
  B=np.array([np.int64(x) for x in re.findall(r"\d+",r[2])])
  B+=10000000000000
  M=np.array([[r1[0], r2[0]],[r1[1],r2[1]]])
  X=np.linalg.solve(M,B)
  X[0]=round(X[0])
  X[1]=round(X[1])

  print(f"Solution: A:{X[0]:.10f}; B:{X[1]:.10f}  for X,Y: {B}")
  print(f"Checking solution for A={r1[0]*round(X[0])+r2[0]*round(X[1])} and B={r1[1]*round(X[0])+r2[1]*round(X[1])}")

  if (B[0]==(r1[0]*round(X[0])+r2[0]*round(X[1]))) and (B[1]==(r1[1]*round(X[0])+r2[1]*round(X[1]))):
  
    print(f"adding solution")
    tokens+=int(3*X[0] + X[1])

print(f"Tokens: {tokens}")
  
  
  


