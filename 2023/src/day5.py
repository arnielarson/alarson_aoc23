#!/usr/bin/python3
import re
import sys

print("hello day 5")

# Parse seeds, create maps
data = open("../data/" + sys.argv[1]).readlines()

# keep mappings keep them as raw
m=[]
idx=0


for line in data:
  if line.startswith("seeds"):
    seeds=[int(x) for x in line.split()[1:]]
        
  elif line.find("map") > 1:
    print(f"map:  {line[:line.find('map')]}")
    m.append([])

  elif line.strip() == "":
    if len(m) > 0:
      idx+=1
  else: # generate and add the mapping
    nm = [int(x) for x in line.split()]
    m[idx].append(nm)
 
    """ NOPE
    d = [int(x) for x in line.split()]
    dst=d[0]
    for i in range(d[1] , d[1]+d[2]):
      m[idx][i]=dst
      dst+=1
    """

locs = []
# process seeds (forward map)
# now test seeds
for s in seeds:
  l=s 
  for mx in m:
    for mn in mx:
      if l>= mn[1] and l< mn[1]+mn[2]:  # found, now map
        l=mn[0] + l - mn[1]
        break

  print(f"Location of seed {s} is {l}")
  locs.append(l)
  
locs.sort()
print(locs)
print(f"Lowest location is {locs[0]}")






