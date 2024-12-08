#!/usr/bin/python

import re

i="data/3a.txt"
with open(i) as f:
  d=f.read()

t="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
t2="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
#print(f"Test: {t}")

i=re.findall(r"mul\(\d+,\d+\)",t)
#n=re.findall(r"don\'t.*mul\(\d+,\d+\)",t)

# need to get sums for sequences
def sum_str(s):
  print(f"sum_str: {s}")
  return sum([m(x) for x in re.findall(r"mul\(\d+,\d+\)",s)])

def sum_seq(s):
  print(f"sum_seq: {s}")
  val= sum([sum_str(str) for str in s])
  print(f"val of sum is {val}")
  return val

# get sum for mul instruction
def m(s):
  a = list(map(int, re.findall("\d+",s)))
  return a[0]*a[1]

print(sum(list(map(m, i))))


# Part 2 - "don't()" disables instructions, "do()" re-enables instructions.."
# Strategy - split on "don't()".  
# For all segments, look for the first do()
# Only add the parts after the first do()

v = re.split(r"don't\(\)",d )
a=sum_str(v[0])
print(f"First sum: {a}")
for e in v[1:]:
  g=re.split(r"do\(\)",e)
  if len(g) > 1:
    a+=sum_seq(g[1:])

print(a)

  




