#!/usr/bin/python3
import sys
import time
import heapq
import random
from collections import defaultdict 
from copy import deepcopy
from functools import total_ordering

print("hello day 25")
"""
  Rats   - My two naive brute force graph algorithms did not work..  Problem is 
           a find the min cut in the graph w 3500 edges, choosing 3 edges..
           I was not able to solve it!


  Day 25 - Snow overload - need to clip 3 wires, (sort of like Die Hard?)
           Given a graph, which 3 edges can be removed to create 2 seperate graphs
           And what is the number when you multiply the cardinality of these two 
           disperate subgraphs together.. 

  Implementation - Ok so input is has nodes and edges, e.g. A : B, C, D.  Want to 
           represent that as two way mapping E {A:B, B:A, ... }
           Want to be able to "snip" edges.  To do that, need an enumeration of the 
           set of edges and then enumerate (i,j,k) to check all snips..

  Graph Traversal - Just BFS with a set of visited nodes?
           For the input set - 1500 Nodes, 3400 Edges, That's more than 10B sets of 
           edges to check.. yargh.  I can't think of any obvious heuristic to trim
           the search space at the moment..

  Epiphany - In my naive algorithm, looking for a subgraph, at each trial I do a full 
           graph traversal..   a better algorithm might be, find a path from A to B.
           For every path (longer than X) update a histogram of nodes traversed.  The
           nodes that show up the most should be the ones that are needed to get to
           either side of the subgraphs..  a lot of work but might lead to a solution
           more quickly..

  Second Epihany - my naive probabilistic algorithm probably doesn't quite get to the 
           heart of things.  Because I'm just getting one path.  And so of the 500 or 
           edges in the path, many are being repeated and the search space is still too
           bit.  So, for a few big paths (>520?)  If we assume these pass through the 
           "choke point" and we enumerate all paths between nodes, than a histogram of 
           these edges should push the relevant min cuts to the top..
"""

# bidirectional edges.. 
E = defaultdict(list)

##
#  How many nodes are reachable??
##
def traverse(E,A):
  c=1
  F=[x for x in E[A]]
  V=set([A])
  while len(F) > 0:
    e=F.pop()
    if e in V:
      continue
    c+=1
    V.add(e)
    for f in E[e]:
      if f not in V:
        F.append(f)
  #print(f"traversed {c} nodes")
  return c

##
#  Plan B - find paths to get heuristic
#  BFS, need to branch for each new node..
#  Maintain a list of lists..
##
def find_path(E,A,B):
  
  P=[[x] for x in E[A]]
  V=set(A)
  end=False
  while not end and len(P)>0:
    p=P.pop()  # p is a path list
    n=p[-1]   # n is last node in the path
    #print(f"At Node: {n}")
    for c in E[n]:
      if c==B:
        # End condition - 
        p.append(c)
        return p
      elif c in V:
        continue
      else:
        V.add(c)
        p2=p.copy()
        p2.append(c)
        P.append(p2)
  return []
  
  
##
#  Helper functions
##
def add(E,A,B):
  E[A].append(B)
  E[B].append(A)

def snip(E,A,B):
  E[A].remove(B)
  E[B].remove(A)
  
def edgeset(E):
  ES=set()
  for k in E.keys():
    for v in E[k]:
      ES.add((k,v)) if k < v else ES.add((v,k))
  return list(ES)

for line in open("../data/" + sys.argv[1]).read().strip().split("\n"):
  a=line.split(":")[0]
  b=line.split(":")[1].split()
  for e in b:
    E[a].append(e)
    E[e].append(a)

#for k in E.keys():
#  print(f"Graph {k} => {E[k]}")
  
N=list(E.keys())
ES=edgeset(E)
print(f"Size of graph: {len(N)}") 
print(f"Num edges: {len(ES)}")


## TODO
## Track edges in paths..
## 


#  Strategy 2
#  Look at random set of paths
#  1. Set up counters
#  2. Count Path lengths..   (400 is big?)
#  3. Count Common nodes..
#  4. Use common nodes as inputs to search
##
def z():
  return 0
c=defaultdict(z)
LTEST=540
C=0


for i in range(50000):
  n1=random.randint(0,len(N)-1)
  n2=random.randint(0,len(N)-1)
  #print(f"Trial {i} n1:{n1},n2:{n2},with N:{len(N)}")
  if n1!=n2:
    #print(f"Searching for path from {N[n1]} to {N[n2]}")
    p=find_path(E,N[n1],N[n2])
    if len(p)> LTEST:
      C+=1
      #print(f"Found path with length {len(p)}")
      #print(f"\tStart: {p[:6]}, End: {p[-6:]}")
      for i in range(len(p)-1):
        e=(p[i],p[i+1]) if p[i]>p[i+1] else (p[i+1],p[i])
        c[e]+=1

print(f"Found {C} lists with length > {LTEST}")


# Now need to sort..
hist = [(k,v) for k, v in c.items()]
hist.sort(reverse=True, key=lambda x: x[1])
print(f"Max frequency is: {hist[0][1]}\n\nFirst few edges of trimmed set:")
mf=hist[0][1]
trim=[x for x in hist if x[1]<=(mf//2)]
for (e,f) in trim[:15]:
  print(f"edge: {e} freq: {f}")

# Hypothesis: edges that appear in every list can't be the min cuts
# Filter out the  



# Ok - now for the meat and potatoes, snip three edeges
# M edges, choose 3

ES_=list(map(lambda x: x[0], trim[:120]))
M=len(ES_)

L=traverse(E,N[0])
print(f"Graphs has size: {L}")

#for (e,f) in hist[:100]:
#  print(f"edge: {e} freq: {f}")

print(f"Length of TRIMMED edge set is {M}\n\nSTARTING BRUTE FORCE")


t1=time.time()
END=False
for i in range(M-2):
  e1=ES_[i]
  snip(E,e1[0],e1[1])
  for j in range(i+1,M-1):
    e2=ES_[j]
    snip(E,e2[0],e2[1])
    for k in range(j+1,M):
      e3=ES_[k]
      snip(E,e3[0],e3[1])
      L=traverse(E,N[0])
      if L != len(N): 
        END=True
        print(f"Found subgraph with {L} nodes")
      add(E,e3[0],e3[1])
      if END:
        break
    add(E,e2[0],e2[1])
    if END:
      break
  print(f"Completed search with i={e1}")
  add(E,e1[0],e1[1])
  if END:
    break
t2=time.time()
print(f"took time: {t2-t1} s")
