#!/usr/bin/python
"""
  Part 1, is INC or DEC (by 1 to 3)
  Part 2, is INC or DEC but allow 1 error..
"""

import math

def valid(d):
  return inc(d) or dec(d)
"""
  Enable a SINGLE skip..
  if one bad row is removed.. 
"""

def inc(row):
  e=0
  p=row[0]
  m= len(row)   # max index
  i=1
  while i< m:
    if row[i]>p and row[i]<(p+4):
      p=row[i]
    elif e is 0:
      e+=1
      i+=1
      # this should check the skip row
      if row[i]>p and row[i]<(p+4):
        p=row[i]
    else:
        return False
    i+=1
  return True
    

def dec(d):
  e=0
  p=row[0]
  m=len(row)
  i=1
  while i < m:
    if row[i]<p and row[i]>(p-4):
      p=row[i]
    elif e is 0:
      e+=1
      i+=1
      if row[i]<p and row[i]>(p-4):
        p=row[i]
    else:
      return False
    i+=1
  return True

i="2a.txt"
j=f"data/{i}"
with open(j) as f:
  d=[x.strip().split() for x in f.readlines()]
  d=[[int(x) for x in l] for l in d]



t=0
for row in d:
  v=valid(row)
  t+=1 if v else 0 
  print(f"Row is valid: {v}")
print(f"Total: {t}")



