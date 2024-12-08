#!/usr/bin/python3
import re
from functools import reduce
import sys


## example p1 = 6440

print("hello day 8")

data = open("../data/" + sys.argv[1]).read().split("\n\n")

inst = data[0]
raw = data[1].strip().split("\n")
print(f"Inst: {inst}\n\n Parsing raw: \n")
print(raw)
k = []
g = {}

for r in raw:
  row = r.split("=")
  k=row[0].strip()
  s=row[1].lstrip(" (").rstrip(")").split(", ")
  g[k] = s

"""
  Graph traversal from AAA to ZZZ
  Representats:
    inst = LRLR...
    A => (B, C)
  Cycles though inst to choose L/R mapping
"""

start="AAA"
end="ZZZ"
steps=0
go=True
idx=0


while go:
  steps +=1
  if idx == len(inst):
    idx=0
  l=inst[idx]=='L'
  idx+=1
  midx=0 if l else 1
  #print(f"Left: {l}")

  nxt = g[start][midx]
  #print(f"map {start} to {nxt}")
  start = nxt
  if start==end:
    print(f"start == end, steps: {steps}")
    go = False
