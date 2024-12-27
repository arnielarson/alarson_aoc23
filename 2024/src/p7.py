#!/usr/bin/python

import re
from itertools import product

da="data/6a.txt"
db="data/6b.txt"
"""
  input has values and number
  line: value: n1 n2 n3 ...
  2 operators: (+) (*)
  combine line in all perutations (2^(N-1))
  the data is not quite big enough to be a problem to just brute force... for part 1
  
  However - Part 2?  I almost guarantee it will require dynamic programming..
  part 2 just adds an operatore (||) concatenate
"""

r= [y.split(":") for y in open(db, 'r').read().strip().split("\n")]
r=[(int(x[0]), list(map(int, re.findall(r"\d+", x[1])))) for x in r]

# rules r[i][0] before r[i][1] <= how to store and execute the rules?


"""
  Boolean, check if applying rules = value..
  Lets not optimize, as there could be a zero which resets the application
  e.g. lets assume application of rules is not monotonic
  Also - this could maybe be done in a reduce from functools
"""
def apply(rules, e, value):
  v=e[0]
  i=1
  for rule in rules:
    if rule == 'm':
      v*=e[i]
    elif rule == 'a':
      v+=e[i]
    elif rule == 'p':
      v=int(str(v)+str(e[i]))
    i+=1
  return v==value

def gen_perms(m,l=None):
  # for each m
  perms=[]
  for i in m:
    for j in m:
      for k in m:
        perms.append([i,j,k])
  return perms
  


"""
  Part 1, for each line, generate rules permutations, and apply them to all elements..
  Part 2, just adds one more 
"""
def part1(r):
  c=0
  for x,y in r:
    print(f"Testing {x}: {y}")
    for rule in product('amp', repeat=(len(y)-1)):

      if apply(rule, y, x):
        print(f"{x} is valid")
        c+=x
        break
  print(f"Total calibration: {c}")

part1(r)

