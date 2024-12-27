#!python
"""
  Another map problem...
  Find the regions..
  
  Part1: Solution is sum(area(region)*perimeter(region) for all regions
  Part2: Oh boy, now need to think about the perimeter a little more deeply,
         In part 2, only the straight edges need to be counted.  So an improved concept of tracking edges in necessary
  Another interesting solution https://www.youtube.com/watch?v=glNiVe_Rztg 
  
  Again variant of breadth first search, however, I looked at some solutions and found a pretty 
  awesome video by "hyperneutrino" - explaining floodfill.  This is an algorithm I've encountered and 
  have coded as part of AoC - but was cool to see and revisit appraoch from somone else.
  https://www.youtube.com/watch?v=KXwKGWSQvS0


  Of note - 
  Flood Fill - maintain seen entries and each region is explored in full.  Accumulate the answer..
  Area - is just the size of the region.
  Perimeter - For each element in region, check the number of adjacent elements.  (Basically each 
              element will contrinute uniquely to the number of perimeter edges)
  Also explict labeling of rows and cols makes the code much easier to read (and mentally map)
  Separately - saw an interesting solution using networkx and maintaining the grid as a complex number..

  Can I explore networkx for this?
"""
import networkx as nx

d="../data/12a.txt"
#d="../data/12b.txt"

with open(d) as f:
  board=[[s for s in g] for g in open(d).read().strip().split("\n")]

