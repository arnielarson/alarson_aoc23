#!python
"""
  Interesting, somewhat fun..  rules apply to "stone" objects, (so lets make objects)
  Preserve order?  Count the total number of stones.
  Transform 25 times.. count the stones

  Part b:
  Transfrom 75 times.. my initial (fun) strategy doesn't work here, so need to capture
  some of the redundancy..

  Looked at a couple of solutions:
  1. Traverse the tree, and maintain a cache
  2. Just maintain a dict.. as a Counter
  3. Also could probably use a defaultdict(int), also good for counting..
  
  Takeaway, ok pretty straightforward implementation with a defaultdict
"""
from collections import Counter
from collections import defaultdict

d0="125 17"
d1="2701 64945 0 9959979 93 781524 620 1"

stones = defaultdict(int)
for v in [int(x) for x in d1.split()]:
  stones[v]=1


for v,n in stones.items():
  print(v, type(v) ,n)
print(sum(stones.values()))

def blink(stones, blinks=6):
  # return the value and cardinality in the collection
  for i in range(blinks):
    s=defaultdict(int)
    for v,n in stones.items():
      if v==0:
        s[1]+=n
      elif len(str(v))%2==0:
        sv=str(v)
        v1=sv[:len(sv)//2]
        v2=sv[len(sv)//2:]
        s[int(v1)]+=n
        s[int(v2)]+=n
      else:
        s[v*2024]+=n
    stones=s
  print(f"After {blinks} there are {sum(stones.values())} stones")  
  #for v,n in stones.items():
  #  print(f"Stone {v} has {n} items")
  
blink(stones, 75)
      
  



