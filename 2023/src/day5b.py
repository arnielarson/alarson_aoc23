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
    print(f"map {line.find('map')}")
    m.append([])

  elif line.strip() == "":
    print("empty line")
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
mseed = seeds[0]
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






