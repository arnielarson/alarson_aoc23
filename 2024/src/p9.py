#!python
"""
  Oh boy - some sort of expansion problem?  

  Lets at least maybe learn how to use array.array better?

  Input:  12345
  1 block file, 2 blocks free, 3 block file, 4 blocks free, 5 block file..
  IDs are incremental
  
  Note - Array and List have a extend() method which makes making the expansion more straightforward.
         np.array operators make the checksum more straighforward..
  
  Part2 - try to move (in order of ID number decreasing, the entire block to the left)
         algorithm is now O(n*m)
         Brute force would be:
              0. Loop to get the free space and block spaces
              1. Get the last block ID and size and idx
              2. Search form the left for a spot for it up to idx
              3. Move idx of the first free space block to the right..
              3. Repeat. 

         Could get a List[(width, idx) .. so would be searching through this 
         Could also generate a List[(id, idx, width)]
"""
from dataclasses import dataclass
import numpy as np

#d="2333133121414131402"
with open("../data/9.txt",'r') as f:
  d=f.read().strip()
#d="2333133121414131402"
 


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


@dataclass
class fsblock:
  idx: int
  len: int
  avail: bool

@dataclass
class idblock:
  idx: int
  id: int
  len: int

"""
  Part 2 - Need to loop once to get the openings and the data 
           s is an array of ints with [id] or [-1] for empty
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
    if n==v: # and idx!=(len(s)-1):
      l+=1
    else:  
      if v==-1:
        fs.append(fsblock(ids,l,True))
      else:
        blocks.append(idblock(ids,v,l))
      v=n; ids=idx; l=1
    idx+=1
  # Need include the end of the loop as well
  if v==-1: fs.append(fsblock(ids,l,True))
  else:  blocks.append(idblock(ids,v,l))

  if pr:
    print(f"fs blocks: {fs}")
    print(f"blocks: {blocks}")
  #return [1,2]
 
  # Ok now, look at blocks in reverse, and see if they can be moved to a free location..
  # If so, move them, update the current free ptr, and swap..
  # update:  update the fs block OR move the fs pointer up one
  # Oops: I misread the goal, try each block, exactly once, from the front

  
  for e in blocks[::-1]:
    if pr: print(f"checking block: {e.id}")

    # need to check all available ranges
    for fsb in [x for x in fs if x.avail]:
      if e.idx < fsb.idx:
        if pr: print(f"break: block idx {e.idx} less than fs idx {fsb.idx}")
        break
      # check length (id block and fs block)
      

      # found match
      if e.len<=fsb.len:
        
        for sdx in range(fsb.idx, fsb.idx+e.len):
          s[sdx]=e.id
        for bdx in range(e.idx, e.idx + e.len):
          s[bdx]=-1
      
        if e.len==fsb.len:
          fsb.avail=False
        elif e.len<fsb.len:
          fsb.idx+=e.len
          fsb.len-=e.len
        break
    if pr: print(f"Now s: {s}")
     
      
   
  if pr: print(f"Now s: {s}")
  return s
      
      
  
"""
   Checksum:  V1: find the first -1  sum(idx * a[idx])
              V2: block is not quite fully compacted, -1 are still used, so
                  first just swap the -1 with 0's
"""
def chksum(a, p2=True):
  if not p2:
    m=a.index(-1)
    d=np.array(a[:m])
    c=sum(d*np.array(range(m)))
    print(f"checksum: {c}")
  else:
    for i in range(len(a)):
      if a[i]==-1:
        a[i]=0
    
    d=np.array(a)
    c=sum(d*np.array(range(len(a))))
    print(f"checksum: {c}")

#chksum(pack(process(d)))
chksum(pack2(process(d, pr=False), pr=False))
#print(process(d))
#chksum(process(d))


