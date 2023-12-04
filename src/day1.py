#!/usr/bin/python3

print("hello day 1")

txt = "../data/day1.txt"

sum=0
with open(txt, 'r') as f:
  for line in f.readlines():
    ints = []
    for c in line.strip():
      if c.isnumeric():
        ints.append(c)
    tmp = int(f"{ints[0]}{ints[-1]}")
    print(f"{line.strip()} : {tmp}")
    sum+=tmp

print(f"Sum: {sum}\nGoodbye")






