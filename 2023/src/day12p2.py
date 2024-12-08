#!/usr/bin/python3
import re
import sys

print("hello day 12")
"""
  Day 12, there are a bunch of ?s in the data, and need to 
  determine number of permutations that fit a pattern.
  Pattern defined as n,m,o.p..  at end of data

  Ok - so I was able to generate all the permutations, 
  but brute force does not work for part 2.

  Permutations are N!/(M!*(N-M)!)

  Had to look at someones solution.  So basically can 
  just iterate left to right, and recursively check solutions.
  Can also add caching..   
  Iterate through text from index 0
  States to try '.' and '#' and '?' can branch to two tries
"""


total=0
#
# txt = "..??##.."..
# b = [1,2,3,..]
# i = index to txt
# bi = index to b
# bii = index to b[bi]
# Advances next solution if current solution is valid.  
CACHE = {}
def gen(txt, b, i, bi, bii):
  ckey=(i,bi,bii)  # if we generate an answer for this state, then we don't need to recompute it..
  if ckey in CACHE:
    return  CACHE[ckey]

  # end conditions correct if traversed bi of the blocks, and not in a current block
  if i==len(txt):
    #print(f"End cond met, i:{i}, bi:{bi}, bii:{bii}")
    if bi==len(b) and bii==0:
      return 1
    elif bi==(len(b)-1) and bii==b[bi]: #  edge case, last block is met
      return 1
    else:
      return 0
  
  # now for state machine logic
  # case '.' => either finished block or move i
  # case '#' => advance block count bii
  # case '?' => either '.' or '#'
  ans = 0
  c = txt[i]
  #print(f"gen c:{c}")
  if c==".":
    if bii>0 and bi<len(b) and bii==b[bi]:       # found a block advance bi and reset bii
      #print(f".block met at {i}, {bi}")
      ans += gen(txt, b, i+1, bi+1,0)
    elif bii==0:                   # not in the middle of a block, which will not match 
      ans += gen(txt, b, i+1, bi, 0)
  elif c=='#':                     # in a block
    if bi < len(b) and bii < b[bi]:                # advance bii, (condition unnecessary?)
      ans += gen(txt, b, i+1, bi,bii+1)
  elif c=='?':                     # 2 need to generate both cases, first two valid '.', second valid '#'
    if bii>0 and bi<len(b) and bii==b[bi]:  # 
      #print(f"?block met at {i}, {bi}")
      ans += gen(txt, b, i+1, bi+1, 0)    # start new block
    elif bii==0:
      ans += gen(txt, b, i+1, bi, 0)      # try non block
      ans += gen(txt, b, i+1, bi, bii+1)  # try start block

    elif bi < len(b) and bii < b[bi]:
      ans += gen(txt, b, i+1, bi, bii+1)  # continue block, if 

  #print(f"Ans for i {i} bi {bi} bii {bii} is {ans}")
  CACHE[ckey]=ans
  return ans
  




lines = open("../data/" + sys.argv[1]).read().strip().split("\n")

total=0
for line in lines:
  S=0
  d=line.split()
  txt="?".join([d[0]]*5)
  #d[0]="?".join([d[0]]*5)
  
  # blocks
  b=[int(x) for x in d[1].split(",")]
  b=b*5
  print(f"calling with txt: {txt}, b: {b}")
  
  a = gen(txt,b,0,0,0)
  print(f"got ans: {a}")
  total += a
  CACHE.clear()

  

print(f"Total is {total}")

    
    
      
      
  
  
 
