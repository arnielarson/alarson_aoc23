#!/usr/bin/python3
import re
import sys

"""
   Grab input as string blob
   Parse lines into a list
   Data now has n rows and m cols (m chars per line)
"""
data = open("../data/" + sys.argv[1]).read()

print(f"type of data: {type(data)}")
grid = data.split("\n")

print(f"type of grid: {type(grid)}")
n = len(grid)
m = len(grid[0])
print(f"grid has dims {n} rows x {m} cols")

# fudge the boundaries
grid = ["." + g + "." for g in grid]
n = len(grid)
m = len(grid[0])
print(f"Now grid has dims {n} rows x {m} cols")

z = "."*len(grid[0])
grid = [z] + grid + [z]
n = len(grid)
m = len(grid[0])
print(f"Now grid has dims {n} rows x {m} cols")


