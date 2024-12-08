#!/usr/bin/python

import re

da="data/5a.txt"
db="data/5b.txt"
i=open(db, 'r').read().strip().split("\n\n")

# rules r[i][0] before r[i][1] <= how to store and execute the rules?

rules=[[int(y) for y in re.findall(r"\d+", x)] for x in i[0].split("\n")]
inst=[[int(y) for y in re.findall(r"\d+",x)] for x in i[1].split("\n")]



# part 1 - are the inputs in the right order?
# for each correct input, collect the middle element and sum

# Strategy - total orderng..   (NOPE!)
# take the rules and make an ordered list..
# take the instruction and verify that the indexes within the total ordering are monotonic increasing..
# Strategy 2 - just check ALL the rules..  should be easy enough


"""
lr= [x[0] for x in r]
lr=[(v,lr.count(v)) for v in ls]
lr.sort(key=lambda x: x[1], reverse=True) # highest count starts first.. 
print(f"to: {lr}")
#to=[x[0] for x in lr]+[end]
to=[x[0] for x in lr]
print(f"to: {to}")
exit()
"""

def correct(i):
  return all([((ru[0] not in i or ru[1] not in i) or (i.index(ru[0])<i.index(ru[1]))) for ru in rules])

def score(inst):
  return inst[int(len(inst)/2)]

"""
  Kind of a bubble sort - but might not be deterministic?  Might want to also 
  order the rules..

"""
def reorder(i):
  idx=0
  c=True
  while c and idx<1000:
    idx+=1
    for ru in rules:
      if (ru[0] in i and ru[1] in i and (i.index(ru[0]) > i.index(ru[1]))):
        i1=i.index(ru[0]); i2=i.index(ru[1])
        t=i[i1]
        i[i1]=i[i2] 
        i[i2]=t
    if correct(i):
      print(f"Fixed {i} in {idx}")
      c=False
  return score(i)
    

def part1():
  s=0
  for i in inst:
    if all([((ru[0] not in i or ru[1] not in i) or (i.index(ru[0])<i.index(ru[1]))) for ru in rules]):
      print("{i} is valid")
      s+=i[int(len(i)/2)]
    else:
      print("{i} is not valid")
  print(s)

def part2():
  s=0
  for i in inst:
    if not correct(i):
      s+=reorder(i)
    else:
      print(f"{i} already correct")
  print(f"Score now: {s}")

#part1()
part2()
