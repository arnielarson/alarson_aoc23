#!/usr/bin/python3
import re
import sys

print("hello day 5")

debug=True
if debug: print("Debug Mode: ON")

# Parse seeds, create maps
data = open("../data/" + sys.argv[1]).readlines()

# keep mappings list of lists
m=[]
idx=0
# keep seed ranges as [start, end] (exclusive on end
sr=[]

for line in data:
  if line.startswith("seeds"):
    seeds=[int(x) for x in line.split()[1:]]
    for i in range(0,len(seeds),2):
      #print(f"adding seed start {seeds[i]} to += {seeds[i+1]}")
      sr.append([seeds[i],seeds[i]+seeds[i+1]])
      
  elif line.find("map") > 1:
    #print(f"map {line.find('map')}")
    m.append([])

  elif line.strip() == "":
    #print("empty line")
    if len(m) > 0:
      idx+=1
  else: # generate the mapping
    nm = [int(x) for x in line.split()]
    m[idx].append(nm)
 
    """ NOPE
    d = [int(x) for x in line.split()]
    dst=d[0]
    for i in range(d[1] , d[1]+d[2]):
      m[idx][i]=dst
      dst+=1
    """
#print("Seed ranges:")
print("Seed ranges:")
print(sr)

# process seeds
"""
for s in seeds:
  l=s 
  print(f"Seeds {s}")
  for mx in m:
    for mn in mx:
      if l>= mn[1] and l< mn[1]+mn[2]:  # found, now map
        l=mn[0] + l - mn[1]
        break
  print(f"Location of {s} is {l}")
  locs.append(l)
"""
  
"""
# process seeds part b
for i in range(0, len(seeds),2):
  for s in range(seeds[i],seeds[i]+seeds[i+1]):
    l = s
    for mx in m:
      for mn in mx:
        if l>= mn[1] and l< mn[1]+mn[2]:  # found, now map
          l=mn[0] + l - mn[1]
          break
    if l < mseed:
      mseed = l
print(mseed)
"""

# need to do inverse mapping from location to start
# start given location find seed.  If seed in seed ranges, return
# first one we find is lowest..
m.reverse()



# Input Format:
# dst src rng



# look through all locations..
# for i in range(0,100):
i=0
while True:
  i+=1
  l = i
  # reverse map
  for mx in m:
    for mn in mx:
     # between destination and destination + range
     if l >= mn[0] and l < mn[0]+mn[2]:
       l = mn[1] + l - mn[0]
       break
  #print(f"Location {i} maps to seed {l}")
  
  # sr is the list of ranges end is exclusive
  for j in range(0,len(sr)):
    if l >= sr[j][0] and l < sr[j][1]:
      print(f"found seed at loc {i} between {sr[j][0]} and {sr[j][0] + sr[j][1]}")
      exit()
  


