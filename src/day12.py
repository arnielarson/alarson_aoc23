#!/usr/bin/python3
import re
from functools import reduce
from itertools import permutations
import perms
import sys
from math import factorial

print("hello day 12")
"""
  Day 12, there are a bunch of ?s in the data, and need to 
  determine number of permutations that fit a pattern.
  Pattern defined as n,m,o.p..  at end of data
"""

lines = open("../data/" + sys.argv[1]).read().strip().split("\n")


"""
  Given n ?'s and m #'s and pattern with N #'s.
  M ?'s
  Sum(P)-N #'s
  Determine what permutations of solutions work
"""
total=0
for line in lines:
  S=0
  d=line.split()

  #d[0]="?".join([d[0]]*5)
  data=[x for x in d[0]]
  #d[1]=",".join([d[1]]*5)
  p=[int(x) for x in d[1].split(",")]
  # N = number of replacements '?'
  # T = number of '#'s already used
  # M = number of '#'s to apply  
  N=len([x for x in filter(lambda y: y=='?', d[0])])
  T=len([x for x in filter(lambda y: y=='#', d[0])])
  M=sum(p)-T
  #M=N-T
  E=factorial(N)//(factorial(M)*factorial(N-M))
  print(f"line: {d[0]}, N={N}, M={M}, finding permutations") 
  print(f" [ expect {E} permutations ]")
  output=[]
  perms.perms([],N,M,output,'#','.')
  print(f"line: {line}, found {len(output)} permutations") 
  #perms = set(permutations('#'*T+'.'*Q))
  #print(f"line: {line}, {M} unknowns with {T} #'s, {Q} .'s and {len(perms)} permutations")
  for perm in output:
    t=[x for x in data]
    i=0; idx=0
    while i < len(perm):
      if t[idx]=='?':
        t[idx]=perm[i]
        i+=1
      idx+=1
    # compare with pattern.. first map to ["##","###",...] then to lengths
    p2=[len(x) for x in re.findall("#+","".join(t))]

    if len(p)==len(p2):
      m=True
      for b in [x[0]==x[1] for x in zip(p,p2)]:
        m = m and b
    else:
      m=False
    #print(f"perm {perm} comapring {p2} to {p}, matches: {m}")
    if m:
      S+=1
  print(f"line {line} had {S} matches")
  total+=S

print(f"Total is {total}")

    
    
      
      
  
  
 
