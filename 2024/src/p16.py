#!python
"""
   Maze problem..  Reindeer maze - find the shortest path..
  
   At each juncture, cost = 100 to turn, 1 to move forward 1 space

   Great problem to test impl in:
   - Simple Dykstra w heapq
   - Use networkx!

   Hyperneutrino, great explanations of Dykstra and Backtracking: https://www.youtube.com/watch?v=BJhpteqlVPM
   Also this: Use networkx: https://github.com/fuglede/adventofcode/blob/master/2024/day16/solutions.py


"""
import heapq

d="../data/16c.txt"

with open(d) as f:
  m=f.read().strip()

print(m)
grid=[[s for s in g] for g in m.split("\n")]

S=E=None
rows=len(grid)
cols=len(grid[0])
print(f"cols: {cols}, rows: {rows}")
for r in range(rows):
  for c in range(cols):
    if grid[r][c]=='S':
      S=(r,c)
    elif grid[r][c]=='E':
      E=(r,c)
print(f"Start: {S}, End: {E}")



# Find the shortest path..
# Explore the possible  paths, lowest cost first, (cost, x, y, dx, dy)
# update the search space with increased cost.  90 turn +=100, forward move +=1
# Note directions (-y,x)   so (0,1) is East, or facing right.  
# Turning right -> South or (1,0), swap the dx and -dy     R = 0 -1    L = 0 1
# Turning left -> North or (-1,0), swap with -dx and dy        1  0       -1 0
# Part 2 -> keep track of number of moves for the best path(s)?

s=(0,set(),S[0],S[1],0,1)
q=[s]
v=set()
m=set()
mc=-1
t=0
while q:
  cost, path, r, c, dy, dx = heapq.heappop(q)
  # print(f"checking {r},{c}, path: {path}")
  # check for End
  # add to visited
  # add to the queue
  if grid[r][c]=="E":
    if mc==-1:
      mc=cost
      m=path   
    elif mc==cost:
      m=m|path
    else:
      break
    print(f"found E, cost: {cost}, path size {len(path)}")
    t+=1
      
  path.add((r,c))
  v.add((r,c,dy,dx))
  for ncost,rr,cc,ddy,ddx in [(cost+1,r+dy,c+dx,dy,dx),(cost+1000,r,c,-dx,dy),(cost+1000,r,c,dx,-dy)]:
    
    #print(f"Checking {rr},{cc},{ddy},{ddx},cost: {ncost}")
    if grid[rr][cc]=='#':
      continue
    elif (rr,cc,ddy,ddx) in v:
      continue
    else:
      #print(f"Adding {rr},{cc},{ddy},{ddx},cost: {ncost}, path: {path}")
      heapq.heappush(q,(ncost,path.copy(),rr,cc,ddy,ddx))

print(f"elements in min path(s): {len(m)}, total paths: {t}")
