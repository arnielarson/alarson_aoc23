#!python
"""
  Interesting, somewhat fun..  rules apply to "stone" objects, (so lets make objects)
  Preserve order?  Count the total number of stones.
  Transform 25 times.. count the stones
  Rules are 0=>1; num_digits%2==0 => split into 2; *=2024
  Creating a tree structure..

  So 25 times results in 55000 for 2 stones, for 7, much larger.  
  Strategy to keep the Stones in memory doesn't scale super far..
 
  Need to do somesort of dynamic programing and/or memoisation
  Strategy seen in solutions:  
    Recursive, get next.. 
    Once get to the bottome, (no more steps), return the value, add the value to a cache
    Now always first check the cache, (v,s)  v is the Stone value, and s is the steps..
    With so many, will be tons of redundant values.. 

  Similar - can use a collections.Counter which sort of acts like a dictionary..  
  So again..  don't store redundant objects in memory...
  
  Since I liked my initial implementaiont, coying to a 11b.py to try w a counter

"""

d0="125 17"
d1="2701 64945 0 9959979 93 781524 620 1"


class Stone:
  
  def __init__(self, v):
    self.v=v
    self.n=[]  # in theory, should preserve order, so if do append, the order would really be self.n[::-1]
 
  def blink(self):
    n=None
    if self.v==0:
      self.v=1   
    elif len(str(self.v))%2==0:
      s=str(self.v)
      l=len(s)
      self.v=int(s[:int(l/2)])
      n=Stone(int(s[int(l/2):]))
      #print(f"splitting value {s} into {self.v} and {int(s[int(l/2):])}") 
    else:
      self.v*=2024
   
    for s in self.n:
      s.blink()
    if n:
      self.n.append(n)

  def count(self):
    if len(self.n)==0:
      return 1 
    c=1
    for s in self.n:
      c=c+s.count()
    return c


  def print(self):
    p=f"{self.v} "
    if len(self.n)==0:
      return p 
    
    for s in self.n[::-1]:
      p=p+s.print()
    return p
      
def test3():
  s=Stone(0)
  print(s.print())
  s.blink()
  print(s.print())
  s.blink()
  print(s.print())
  s.blink()
  print(s.print())
  s.blink()
  print(s.print())
  s.blink()
  print(s.print())
  print(f"Count: {s.count()}")

def part1(d, blinks=6):
  stones=[]
  for s in d.split():
    stones.append(Stone(int(s)))

  for i in range(blinks):
    for s in stones:
      s.blink()

  c=0
  for s in stones:
    c+=s.count()
  print(f"Stones: {c}")

  

part1("1", 40)

