#!/usr/bin/python
"""
  Oh boy - some sort of expansion problem?  

  Lets at least maybe learn how to use array.array better?

  Input:  12345
  1 block file, 2 blocks free, 3 block file, 4 blocks free, 5 block file..
  IDs are incremental
  
  Note - Array and List have a extend() method which makes making the expansion more straightforward.
         np.array operators make the checksum more straighforward..
  
  Part2 - try to move (in order of ID number decreasing, the entire block to the left)
         alorithm is now O(n*m)
         Brute force would be:
              0. Loop to get the free space and block spaces
              1. Get the last block ID and size and idx
              2. Search form the left for a spot for it up to idx
              3. Move idx of the first free space block to the right..
              3. Repeat. 

         Could get a List[(width, idx) .. so would be searching through this 
         Could also generate a List[(id, idx, width)]
"""

import numpy as np

#d="2333133121414131402"
#with open("../data/9.txt",'r') as f:
#  d=f.read().strip()
d="2333133121414131402"
 


def process(s, pr=True):
  """
    Unpack the string to compress..
    
  """
  if pr: print(s)
  u=[]
  id=0; fs=False

  for c in s:
    if not fs:
      u.extend([id]*int(c))
      id+=1; fs=True
    else:
      u.extend([-1]*int(c))
      fs=False
  if pr: print(f"processed: {u}")
  return u

def pack(s, pr=True):
  """
    Perform the packing algorithm..
  """
  idx=0; edx=len(s)-1
  while idx < edx:
    if s[edx]==-1:
      edx-=1
    elif s[idx]==-1:
      s[idx]=s[edx]
      s[edx]=-1
      edx-=1; idx+=1
    else:
      idx+=1
  if pr:  print(f"packed: {s}")
  return s

"""
  Part 2 - Need to loop once to get the openings and the data 
"""
def pack2(s, pr=True):
  if pr: print(f"expanded: {s}")

  fs=[] # track blank spaces: idx, width
  blocks=[] # track ids: id, idx, width 
  # Get the id list:
  ids=0
  idx=1
  l=1
  v=s[ids]
  while idx < len(s):
    n=s[idx]
    if n==v and idx!=(len(s)-1):
      l+=1
    else:  
      if v==-1:
        fs.append((ids,l))
      else:
        blocks.append((v,ids,l))
      v=n; ids=idx; l=1
    idx+=1
  # Need include the end of the loop as well
  #if v==-1: fs.append((ids,l))
  #else:  blocks.append((v,ids,l))

  print(f"fs: {fs}")
  print(f"blocks: {blocks}")
  
  # Ok now, look at blocks in reverse, and see if they can be moved to a free location..
  # If so, move them, update the current free ptr, and swap..
  fidx=0
  idx=fs[fidx][0]
  for e in blocks[::-1]:
    if e[2]<= fs[fidx][1]:
      print(f"Can update {e[0]}")
     
    





  
def chksum(a):
  #print(f"Input to checksum: {a}")
  m=a.index(-1)
  
  d=np.array(a[:m])
  #print(f"Trun: {a[:]}")
  #print(f"Idx: {list(range(m))}")
 
  c=sum(d*np.array(range(m)))
  print(f"checksum: {c}")

#chksum(pack(process(d)))
pack2(process(d))
    
    
    
    
