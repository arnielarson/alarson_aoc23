#!/usr/bin/python3
import re

print("hello day 3")


syms = set()
nums = set()
parts = []
sum = 0


# given coordinate, move left and get largest valid number
# keep track of numbers in a global set
# i is row, j is column, so move columns to the left
def get_num_coord(i,j):
  global sum
  jx=j
  cont = True
  while cont:
    if jx==0:
      cont=False
    elif data[i][jx-1].isnumeric():
      jx+=-1
    else:  # we have found left most valid number (i,jx)
      cont=False
  return (i,jx)     

# Assumes we've already found the set of starting coords, so this just plucks off the number
def get_num(coords):
  i=coords[0]
  jx=coords[1]
  num=""
  cont = True
  while cont:
    c= data[i][jx]
    if c.isnumeric():
      num+=c
      jx+=1
      if jx==len(data[i]):  # condition where number has reached end of line
        cont=False
    else:
      cont=False
  return int(num)
      


# a gear is a * pattern with exactly two adjacent numbers
# adds n1*n2 to the sum of gear ratios..
# keeps a local dictionary to check for correct number
def find_gear(i,j):
  global sum
  nums = set()
  print(f"  checking idx: ({i},{j}), val: {data[i][j]}")
  # check above left
  if i>0 and j>0:
    if data[i-1][j-1].isnumeric():
      nums.add(get_num_coord(i-1,j-1))
  
  # check above 
  if i>0:
    if data[i-1][j].isnumeric():
      nums.add(get_num_coord(i-1,j))

  # check above right
  if i>0 and (j+1)<(len(data[i-1])-1):
    if data[i-1][j+1].isnumeric():
      nums.add(get_num_coord(i-1,j+1))

  # check left
  if j>0:
    if data[i][j-1].isnumeric():
      nums.add(get_num_coord(i,j-1))

  # check right
  if j<len(data[i]):
    if data[i][j+1].isnumeric():
      nums.add(get_num_coord(i,j+1))

  # check below left
  if i<(len(data)-1) and j>0:
    if data[i+1][j-1].isnumeric():
      nums.add(get_num_coord(i+1,j-1))

  # check below
  if i<(len(data)-1):
    if data[i+1][j].isnumeric():
      nums.add(get_num_coord(i+1,j))

  # check below right  
  if i<(len(data)-1) and j < (len(data[i])-1):
    if data[i+1][j+1].isnumeric():
      nums.add(get_num_coord(i+1,j+1))

  if len(nums)==2:
    a = get_num(nums.pop())
    b = get_num(nums.pop())
    val = a * b
    print(f"found gear with {a} {b}, adding value {val}")   
    sum += val



row = 0
data=[]

with open("../data/day3.txt") as f:
  for line in f.readlines():
    # looking for * patterns
    #s = re.sub("[\+#$&=\%\-/@]","*",s)
    data.append(line.strip())

L=len(data)
for i in range(L):
  
  idx = 0 
  while idx >= 0:
    if idx>0: # subsequent searches
      idx=data[i].find("*", idx+1)
    else:
      idx=data[i].find("*")

    if idx >= 0:
      find_gear(i,idx)
    
    

print(f"Gear ratios: {sum}")

