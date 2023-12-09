#!/usr/bin/python3
import re
from functools import reduce
import sys

print("hello day 9")

seqs = open("../data/" + sys.argv[1]).read().strip().split("\n")

data = [[int(d) for d in s.split()] for s in seqs]
 
# Keep track of differences and original sequence here, ptr is book keeping for 
# the indices of the original sequence when applying the prediciton
d = []
ptr = []

# p1 aim is to look at sequences, and collect the right most values: sum
idx=0
for s in data:
  go=True
  d.append(s)
  ptr.append(idx)
  idx+=1
  while go:
    idx+=1
    seq = d[-1]   
    diff = []
    for i in range(len(seq)-1):
      diff.append(seq[i+1] - seq[i])
    d.append(diff)
    
    if sum(diff) == 0:
      go=False

for seq in d:
   print(f"Seqs: {seq}")

# now need to add right most value
# I guess go from bottom to top?
# Part 2, insert at beginning of list.. 
idx = len(d)-1
while idx > 0:
  bot = d[idx]
  top = d[idx-1]
  bf = bot[0]
  tf = top[0]
  #if tf != 0: # handle transitions between sequences..
  if idx in ptr: # handle transitions pt 2
    pass
  else:
    top.insert(0, tf - bf)
  idx -=1

#for seq in d:
#  print(f"Predictions: {seq}")
#exit()
  
# Get scores  
predictions = []
for i in ptr:
  predictions.append(d[i][0])

for p in predictions:
  print(f"Prediction: {p}")

print(f"Sum predictions: {sum(predictions)}")
