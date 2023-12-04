#!/usr/bin/python3

print("hello day 1b")

txt = "../data/day1.txt"
replaces = [
  ["one",1],
  ["two",2],
  ["three",3],
  ["four",4],
  ["five",5],
  ["six",6],
  ["seven",7],
  ["eight",8],
  ["nine",9]
]
"""
  Now need to also check for the words "one,two,.." in program
"""
def brute_check(s):
  for x in replaces:
    if s.startswith(x[0]):
      return x[1]
  return -1
  

sum=0

with open(txt, 'r') as f:
  for line in f.readlines():

    s = line.strip()
    ints = []
    # go through by index, check for digit, then check for word at idx
    for idx in range(len(s)):
      if s[idx].isnumeric():
        ints.append(s[idx])
      else:   # check if it's spelled 
        r = brute_check(s[idx:])
        if r > 0:
          ints.append(r)
    tmp = int(f"{ints[0]}{ints[-1]}")
    print(f"{line.strip()} : {tmp}")
    sum+=tmp

print(f"Sum: {sum}\nGoodbye")






