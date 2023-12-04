#!/usr/bin/python3
import re

print("hello day 2")

# Goal is simply to process strings and determine if game is 
rmax = 12
gmax = 13
bmax = 14

# New goal is to multiply the minimal number of cubes required
max=20

sum=0
with open("../data/day2.txt") as f:
  for line in f.readlines():
    
    rmin=bmin=gmin=0
    s = re.sub("[:,;]","",line.strip())

    t = s.split() 
    # assumes specific indexing, no error handling
    for i in range(2,len(t),2):
      if t[i+1] == 'blue':
        if int(t[i]) > bmin:
          bmin = int(t[i])
      if t[i+1] == 'red':
        if int(t[i]) > rmin:
          rmin = int(t[i])
      if t[i+1] == 'green':
        if int(t[i]) > gmin:
          gmin = int(t[i])

    
    power = rmin*bmin*gmin
    print(f"{s}, Power {power}")
    sum+=power


print(f"\nSum is {sum}")
      
       





