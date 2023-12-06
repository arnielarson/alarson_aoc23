#!/usr/bin/python3
import re
from functools import reduce
import sys

print("hello day 6")

Time= [46 ,80 ,78 ,66]
Distance=[214 ,1177,1402,1024]
#Time= [7 ,15, 30]
#Distance=[9, 40, 200]
#Time=[46807866]
#Distance=[214117714021024]
#Time=[71530]
#Distance=[940200]


# Time and distance are all of the digits in the list put together
# input is list of time/distance pairs 
def p1(ti, di):
  print(f"Finding distances for times {ti} and prev best distance {di}")
  r=0
  for i in range(len(ti)):
    T=ti[i]
    print(f"time: {T}")

    for h in range(T+1):
      d=h*(T - h)
      if d>di[i]:
        r+=1
  print(r)


ti = [int(reduce(lambda a, b: a+b, [str(t) for t in Time]))] 
di = [int(reduce(lambda a, b: a+b, [str(d) for d in Distance]))] 


p1(Time,Distance)
p1(ti,di)
