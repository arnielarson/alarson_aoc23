#!/usr/bin/python3
import sys

print("hello day 13")

patterns = open("../data/" + sys.argv[1]).read().strip().split("\n\n")

#grid = [[x for x in line] for y in line.split("\n") for line in patterns]
#ogrid = [[s for s in line ] for line] in [x.split("\n") for x in patterns]]

grid = [line.split("\n") for line in patterns]

# transform list of strings to list of lists
for g in grid:
  for i in range(len(g)):
    g[i] = [s for s in g[i]]


"""
  Looking for reflections.. horizontal or vertical
  In data / patterns
 
  Part 2 - fix a "smudge" exacly 1 '.' '#' should be swapped 
  to generate a new reflection..
  
  Strategy:  Brute force?
  Also need to do some data manipulation, put the grid into 
  a matrix form rather than a list of strings.  
  Strings are immutable in Python
  
  Need to ignore the original reflection, so track that too
  
"""

# check for vertical reflection 
# NC = number of columns
# Need to check each of the NC-1 col boundaries for reflection
# ignore old reflections ignore = (v,h)
def v(grid, ignore):
  
 
  NR=len(grid); NC=len(grid[0])
  C=0
  for r in range(1,NC): # also the scoring value, num columns left of reflection
    
    # print(f"checking col {r} for reflection")
    m=True
    o=0
    # offset condion..   boundaries and "continue"
    while ((r-o-1)>=0 and (r+o)<NC and m):
      assert (r-o-1) >= 0
      assert r+o <= (NC -1)
      for i in range(NR): # check a column of values
        #print(f"checking i:{i},o:{o},r:{r},NC:{NC}")
        if grid[i][r-o-1]!=grid[i][r+o]:
          m=False
          break
      o+=1
  
    if m and r!=ignore[0]:
      C=r
    #print(f"At col {r} reflecting = {m}")
  return C


  
# check for horizontal reflection
# ignore original refleciton..
def h(grid, ignore):
  
  NR=len(grid); NC=len(grid[0])
  R=0
  for r in range(1,NR): # also the scoring value, num columns left of reflection
    
    # print(f"checking col {r} for reflection")
    m=True
    o=0
    # offset condion..   boundaries and "continue"
    while ((r-o-1)>=0 and (r+o)<NR and m):
      assert (r-o-1) >= 0
      assert r+o <= (NR -1)
      for i in range(NC): # check a row of values
        #print(f"checking i:{i},o:{o},r:{r},NC:{NC}")
        if grid[r-o-1][i]!=grid[r+o][i]:
          m=False
          break
      o+=1

    if m and r!=ignore[1]:
      R=r
    #print(f"At row {r} reflecting = {m}")
  return R

# Part 1
P1={}
score=0
for i, g in enumerate(grid):
  vs=v(g,(-1,-1)); hs=h(g,(-1,-1));
  print(f"Pattern {i} has reflections v:{vs} and h:{hs}")
  score+=vs
  score+=100*hs
  P1[i]=(vs,hs)
print(f"Part 1 Score: {score}")


# Part 2
score=0
for p, g in enumerate(grid):

  # brute force try smudges until we find one
  i=0; j=0;
  NC=len(g[0]); NR=len(g)
  hs=0; vs=0;
  c=0
  
  while (i < len(g) and hs==0 and vs==0):       # NR  
    j=0
    while (j < len(g[0]) and hs==0 and vs==0):  # NC
      # try swap
      if g[i][j] == '.':
        g[i][j] = '#'
      else:
        g[i][j] = '.'
      vs=v(g,P1[p])
      hs=h(g,P1[p])
        
      # swap back
      if g[i][j] == '.':
        g[i][j] = '#'
      else:
        g[i][j] = '.'

      j+=1
      c+=1
    i+=1
      
      
  print(f"Pattern {p} tried {c} smudges, has NEW reflections v:{vs} and h:{hs}")
  score+=vs
  score+=100*hs
print(f"Part 2 Score: {score}")

