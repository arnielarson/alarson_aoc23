#!/usr/bin/python3
import re
import sys

print("hello day 5")

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
      


t = sum( [x[1]-x[0] for x in sr])
print(f"Total number of seeds: {t}") 


