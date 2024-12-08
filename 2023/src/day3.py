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
def get_num(i,j):
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
      

  if (i,jx) in nums:
    print(f"number at ({i},{jx}) already added, skipping..")
    return 0
  else:
    nums.add((i,jx))
    num=""
    cont = True
    while cont:
        
      c= data[i][jx]
      if c.isnumeric():
        num+=c
        jx+=1
        if jx==len(data[i]):  # conditino where number has reached end of line
          cont=False
      else:
        cont=False
    print(f"Adding {num} to sum")
    sum += int(num)
      


# get adjacent numbers
# not maximally efficient.. but shouldn't double count anything
# 8 cases
def find(i,j):
  print(f"  checking idx: ({i},{j}), val: {data[i][j]}")
  # check above left
  if i>0 and j>0:
    if data[i-1][j-1].isnumeric():
      get_num(i-1,j-1)
  
  # check above 
  if i>0:
    if data[i-1][j].isnumeric():
      get_num(i-1,j)

  # check above right
  if i>0 and (j+1)<(len(data[i-1])-1):
    if data[i-1][j+1].isnumeric():
      get_num(i-1,j+1)

  # check left
  if j>0:
    if data[i][j-1].isnumeric():
      get_num(i,j-1)

  # check right
  if j<len(data[i]):
    if data[i][j+1].isnumeric():
      get_num(i,j+1)

  # check below left
  if i<(len(data)-1) and j>0:
    if data[i+1][j-1].isnumeric():
      get_num(i+1,j-1)

  # check below
  if i<(len(data)-1):
    if data[i+1][j].isnumeric():
      get_num(i+1,j)

  # check below right  
  if i<(len(data)-1) and j < (len(data[i])-1):
    if data[i+1][j+1].isnumeric():
      get_num(i+1,j+1)



row = 0
data=[]

with open("../data/day3.txt") as f:
  for line in f.readlines():
    s=line.strip()
    s = re.sub("[\+#$&=\%\-/@]","*",s)
    data.append(s)
    for c in s:
      syms.add(c)

L=len(data)
for i in range(L):
  
  idx = 0 
  while idx >= 0:
    if idx>0: # subsequent searches
      idx=data[i].find("*", idx+1)
    else:
      idx=data[i].find("*")
    #print(f"Data: {data[i]}")
    #print(f"Row {i} found {data[i][idx]} at idx {idx}")
    if idx >= 0:
      find(i,idx)
    
    

    
print(f"Syms: {syms}")

print(f"Sum: {sum}")

