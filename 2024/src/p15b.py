#!python
"""
   More robots!

   These can push around objects..  
   # boundary
   . open space
   0 boxes (which can move..
   @ the robot..
  
   Given the instructions.. move the robot
   at the end, cacluate the score sum(100*by)

   First part - straightforward, fun.  
   Second part - map the map!
   Each # -> ##
   Each . -> ..
   Each @ -> @.
   Each O -> []   The boxes now take up two spaces and move as a unit!   So this will add a bunch of logic to the code...

   [] move as a unit -> ^ <- v
   <> need to just check a single row..
   ^v need to check conditionally two. 
  

"""
from collections import defaultdict


d="../data/15b.txt"

with open(d) as f:
  (b,i) = f.read().strip().split("\n\n")
b=[[c for c in l] for l in b.split("\n")]
rows=len(b)
cols=len(b[0])
print(b)

class Robot:
  
  def __init__(self, b, i, rows, cols):
    self.b=b
    self.i=i
    self.rows=rows
    self.cols=cols
    self.r=self.getrobot()
    self.k=defaultdict(str)
    self.k['>']=(0,1)
    self.k['<']=(0,-1)
    self.k['v']=(1,0)
    self.k['^']=(-1,0)
    if not self.r:
      print("invalid board, good bye")
      exit()
    
  def show(self):
    for l in self.b:
      print("".join(l))
  
  def getrobot(self, R='@'):
    for c in range(self.cols):
      for r in range(self.rows):
        if self.b[r][c]==R:
          return [r,c]
    return None

  def update(self, rc, c):
    if rc[0]<0 or rc[1]>=self.rows or rc[1]<0 or rc[1]>=self.cols:
      pass
    else:
      self.b[rc[0]][rc[1]]=c
    

  def move(self, r,m,p):
    """
       r=current spot
       r+m=spot to move to
       if can move:
         set current spot to p

    """
    row=r[0]+m[0]
    col=r[1]+m[1]
    cp=self.b[row][col]
    if row<0 or row>=self.rows or col<0 or col>=self.cols:
      return False
    if self.b[row][col]=='#':
      return False
    elif self.b[row][col]=='.':
      self.b[row][col]=p
      return True
    else:
      if self.move((row,col), m, cp):
        self.b[row][col]=p
        return True
      else:
        return False

  def move_robot(self, c):
    m=self.get_move(c)
    cr=self.r
    if m and self.move(self.r, m, '@'):
      self.update(cr,'.')      # robot always leaves an empty space
      self.r[0]+=m[0]   
      self.r[1]+=m[1]   

  def get_move(self, c):
    return self.k[c]

  def get_sum(self):
    """
       for each box, return 100*r+c
    """
    s=0
    for r in range(self.rows):
      for c in range(self.cols):
        if self.b[r][c]=='O':
          s+=100*r+c
    return s
  
 

def play(R):
  R.show()
  while True:
    p=input("Press < v > ^ or q to quit\n")
    if p.lower()=='q':
      break
    else:
      # If board changes, update state and board..
      m=R.get_move(p)
      tr=R.r
      if m and R.move(R.r, m, '@'):
        R.update(tr,'.')
        R.r[0]+=m[0]
        R.r[1]+=m[1]
        R.show()
  print(f"gps sum: {R.get_sum()}")
      

R=Robot(b,i,rows,cols)
R.show()
#play(R)

for inst in i:
  R.move_robot(inst)

R.show()
print(f"score: {R.get_sum()}")

