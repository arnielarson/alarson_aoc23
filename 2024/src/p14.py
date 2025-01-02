#!python
"""
   Oh my gosh robots!  

   Given px,py and vx,vy..  evolve in time!
   px (cols from left)
   py (rows from top)

   Board is 101 tiles wide and 103 tiles tall..
  
   Parsing - note need to include the minus signs!

   Fun - part 2, find when the robots make a Christmas Tree easter egg?  (WTF!)

   My initial idea was basically correct, look for the minimal safety factor..

   Meh - so.. actually, a better idea is to find the maximum number of adjacent robots..


"""
import re
from functools import reduce
import time


#d="../data/14a.txt"
d="../data/14b.txt"

with open(d) as f:
  robots = [list(map(int, re.findall(r"-?\d+", x))) for x in f.read().strip().split("\n")]

#for r in robots:
#  print(f"px,py;vx,vy: {r}")


w=101; h=103
#w=31; h=41
#w=11; h=7
"""
   In this case 
     c:[0:10] q[0:4]; [6:10] 
     r:[0:6]
   
"""
board = {
  (r,c) : [] for r in range(h) for c in range(w)
}

def update(board, robots):
  # Reset the board, then add in the robots..
  for r in range(h):
    for c in range(w):
      board[(r,c)]=[]
  for r in robots:
    board[(r[1],r[0])].append(1)

def show(board, robots,reset=False):
  if reset:
    update(board, robots)
  for r in range(h):
    s=" ".join(["." if len(board[(r,c)])==0 else str(len(board[(r,c)])) for c in range(w)])
    print(s)
      
def evolve(robots, t=1):
  for idx in range(len(robots)):
    r=robots[idx]
    px=(r[0]+t*r[2])%w
    py=(r[1]+t*r[3])%h
    robots[idx][0]=px
    robots[idx][1]=py
  return robots


def calc_board(board, robots, w, h):
  # look at four quadrants..
  q=[0]*4
  update(board, robots)
  #print(f"Q1: C:0:{w//2}, H:0:{h//2}")
  #print(f"Q2: C:{w//2+1}:{w}, H:0:{h//2}")
  #print(f"Q3: C:{w//2+1}:{w}, H:{h//2+1}:{h}")
  #print(f"Q4: C:0:{w//2}, H:{h//2+1}:{h}")
  for c in range(0,w//2):
    for r in range(0,h//2):
      if board[(r,c)]:
        #print(f"1robot! r:{r}, c:{c}")
        q[0]=q[0]+len(board[(r,c)])    
  for c in range(w//2+1,w):
    for r in range(0,h//2):
      if board[(r,c)]:
        #print(f"2robot! r:{r}, c:{c}")
        q[1]=q[1]+len(board[(r,c)])    
  for c in range(0,w//2):
    for r in range(h//2+1,h):
      if board[(r,c)]:
        #print(f"3robot! r:{r}, c:{c}")
        q[2]=q[2]+len(board[(r,c)])    
  for c in range(w//2+1,w):
    for r in range(h//2+1,h):
      if board[(r,c)]:
        #print(f"4robot! r:{r}, c:{c}")
        q[3]=q[3]+len(board[(r,c)])    
  return reduce(lambda x,y: x*y, q)

def null_right(board,w,h,n=10):
  update(board, robots)
  total=0
  for c in range(w-n, w):
    for r in range(0,h):
      if board[(r,c)]:
        total+=len(board[(r,c)])
  return total

def maybe_tree(board,robots,w,h):
  update(board, robots)
  """
     Meh - saw someone elses solution, definitely easiest thing is probably going to be 
     to just look for most adjacent robots..
  """
  nn=0
  for r in range(h):
    
    prev=False
    n=0
    for c in range(w):
      if board[(r,c)]:      # robot at (r,c)
        if prev:
          n+=1
        else:
          n=1
          prev=True
      elif prev:            # reset prev flag
        if n>nn:
          nn=n              # found new most nearest neighbors
        prev=False
        n=0
    if prev:
      if n>nn:
        nn=n
  return nn
        
        
      
   
  
      



# Print the initial configurations (quadrant score)
t=0; cont=True
qs=calc_board(board, robots, w, h)
print(f"t={t}; Initial score: {qs}")
show(board, robots, True)
nn=0
# evolve robots 1s at a time, check for most nearest neghbors
while cont:
  evolve(robots)
  t+=1
  n=maybe_tree(board, robots, w, h)
  if n>nn:
    print(f"t={t}; new nn: {n}")
    nn=n
    show(board, robots, True)
    print(f"t={t}; new nn: {n}")
    c=input("Press q to quit\n")
    if c.lower()=='q':
      cont=False
    



