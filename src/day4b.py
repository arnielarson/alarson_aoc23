#!/usr/bin/python3

print("hello day 4")

test = "../data/day4_test2.txt"
data = "../data/day4.txt"


def update(score):
  if score==0:
    return 1
  else:
    return 2*score

with open(data) as f:
  grid = f.readlines()


# Now we have a grid, and copies of each "card", 
# numbers will be a [[[winners],[ours]],.. ] structure

copies = [1]*len(grid)
total = sum(copies)
print(f"starting cards: {total}")
numbers = []

for line in grid:
  winners = [int(x) for x in line.strip().split("|")[0].split()[2:]]
  ours = [int(x) for x in line.strip().split("|")[1].split()]
  numbers.append([winners,ours])

# for each card, check score, and add scores at idx+1
for idx in range(len(copies)):
  matches = 0
  for o in numbers[idx][1]:
    if o in numbers[idx][0]:
      matches+=1
  #print(f"Card {idx} has matches {matches}")
  # Add new cards at idx
  for j in range(copies[idx]):
    for s in range(1,matches+1):
      #print(f"\tAdding 1 at idx {idx+s}")
      if idx+s < len(copies):
        copies[idx+s]+=1
      

print(f"(copy array: {copies}")

print(f"ending cards: {sum(copies)}")



