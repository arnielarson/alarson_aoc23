#!/usr/bin/python3
import re
import sys

with open("day3.txt") as f:
  grid = f.readlines()

# grid has n rows m cols
n = len(grid)
m = len(grid[0])
print(f"grid has dims {n} x {m}")


