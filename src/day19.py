#!/usr/bin/python3
import sys
import re

print("hello day 19")
"""
  Process "workflows"

  Workflow: <in> <op> <val> : <to>

  Part2
  Now need to check all possible workflows:
  (x1..x2,m1..m2,a1..a2,s1..s2)
 
"""

D = open("../data/" + sys.argv[1]).read().strip().split("\n\n")

g=0

# Part2, index to r[0]
dm={}; dm['x']=0; dm['m']=1; dm['a']=2; dm['s']=3;

class WF:
  def __init__(self,ops=[]):
    self.ops=ops

  ## Process ranges
  #  need to mutate data and continue processing..
  def prange(self,d):

    # process ranges [r1:r2)
    for op in self.ops:
      if len(op)==1:
        W[op[0]].prange(d)
        return # workflow ends..
      else:
        i=dm[op[0]]*2  # index to first part of range
        if op[1]=='<':
          if d[i+1]<=op[2]:  # process full range, return
            W[op[3]].prange(d)
            return
          elif d[i]<op[2]:  # split range, pass on part, keep part
            d1=d.copy()
            d1[i+1]=op[2]
            d[i]=op[2]
            W[op[3]].prange(d1)
          else:  # noop - continue
            pass

        elif op[1]=='>':
          if d[i] > op[2]: # whole range passed on, exit this workflow
            W[op[3]].prange(d)
            return
          elif d[i+1] > op[2]:  # split
            d1=d.copy()
            d1[i]=op[2]+1
            d[i+1]=op[2]+1
            W[op[3]].prange(d1)
          else:  # range is under, noop, continue
            pass
  
  def process(self, d):
    for op in self.ops:
      if len(op)==1:
        #print(f"m: {op[0]}, d:{d}")
        W[op[0]].process(d)
        return
      else:
        i=dm[op[0]]
        #print(f"idx: {i}, m:{op[3]}, d:{d}")
        if op[1]=='<' and d[i] < op[2]:
          W[op[3]].process(d)
          return
        elif op[1]=='>' and d[i] > op[2]:
          W[op[3]].process(d)
          return
                 
# Add up ranges.. to sum
class A2(WF):
  def prange(self, d):
    global g  
    print(f"Part range: {d} accepted")
    x=(d[1]-d[0])
    m=(d[3]-d[2])
    a=(d[5]-d[4])
    s=(d[7]-d[6])
    g+=x*m*a*s

class R2(WF):
  def prange(self, d):
    print(f"Part range: {d} rejected")
  
        
class A(WF):
  def process(self, d):
    global g
    print(f"Part: {d} accepted")
    g+=d[0]+d[1]+d[2]+d[3]

class R(WF):
  def process(self, d):
    print(f"Part: {d} rejected")
  
#a=A(); r=R();
a2=A2(); r2=R2();
W={}; W['A']=a2; W['R']=r2;


def procw(e):
  m = re.search("([<>])",e)
  if m:
    p1=e.split(m[0])
    p2=p1[1].split(":")
    return [p1[0],m[0],int(p2[0]),p2[1]] # operation
  else:
    return [e]  # noop, mapping
      
      
    
# Process all the workflows
# str => [ops] which define a workflow
def proc(w):
  for line in w.strip().split("\n"):
    w1=line.split("{")
    k=w1[0]
    w2=w1[1].rstrip("}").split(",")
    ops=list(map(procw,w2))
    W[w1[0]]=WF(ops)

# Part 1
# data input parsing
def procdata(line):
  d=line.lstrip("{").rstrip("}").split(",")
  x=int(d[0].split("=")[1])
  m=int(d[1].split("=")[1])
  a=int(d[2].split("=")[1])
  s=int(d[3].split("=")[1])
  return (x,m,a,s)


# test workflow
def t1():
  t="{x=787,m=2655,a=1222,s=2876}"
  d=procdata(t)
  print(d)
  W['in'].process(d)

# set up the workflows..
proc(D[0])
# Part1 parse the data
#for line in D[1].strip().split("\n"):
#  d=procdata(line)
#  W['in'].process(d)

#Part2 maintain ranges of data?
# pass on list of ranges??
# ranges are left inclusive [a1,a2)
d=[1,4001,1,4001,1,4001,1,4001]
W['in'].prange(d)

print(f"Sum of accepted: {g}")


# test workflow  
#t1()





  

