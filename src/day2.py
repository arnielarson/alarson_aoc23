#!/usr/bin/python3
import re

print("hello day 2")

# Goal is simply to process strings and determine if game is valid
rmax = 12
gmax = 13
bmax = 14

sum=0
with open("../data/day2.txt") as f:
  for line in f.readlines():
    # assume valid, if counter example found, set to invalid and break from inner loop
    valid=True
    print(f"{line.strip()}")
    s = re.sub("[:,;]","",line.strip())

    t = s.split() 
    # assumes specific indexing, no error handling
    for i in range(2,len(t),2):
      if t[i+1] == 'blue':
        if int(t[i]) > bmax:
          valid=False
          break
      if t[i+1] == 'red':
        if int(t[i]) > rmax:
          valid=False
          break
      if t[i+1] == 'green':
        if int(t[i]) > gmax:
          valid=False
          break
    print(f"Checking: {s} valid: {valid}")
    if valid:
      sum+=int(t[1])


print(f"\nSum is {sum}")
      
       





