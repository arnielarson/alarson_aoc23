#!/usr/bin/python3
import re
from functools import reduce
import sys


## example p1 = 6440

print("hello day 7")


data = open("../data/" + sys.argv[1]).readlines()

hands = []
for d in data:
  x=d.strip().split()
  hands.append([x[0],x[1]])


# debug take first 100
#hands = hands[:100]

def mh(d):
  r=[]
  for val in d:
    if val=='A':
      r.append(14)
    elif val=='K':
      r.append(13)
    elif val=='Q':
      r.append(12)
    elif val=='J':
      r.append(11)
    elif val=='T':
      r.append(10)
    else:
      r.append(int(val))
  return r

# Ooops, just need to compare cards in original order to break ties???
# [str, bid, int_orig, rank, ..
# Ooooops, missed the sentance where J is no lowest order in the ranking..
def cmp2(h1,h2):
  if h1[4] > h2[4]:
    return 1
  elif h1[4] < h2[4]:
    return -1
  else:
    for i in range(len(h1[2])):
      if h1[2][i] > h2[2][i]:
        return 1
      elif h1[2][i] < h2[2][i]:
        return -1
  return 0
    
  
# apply the jack..
# 
def aj(h1):
  nj=0
  h={}
  r=[]
  for c in h1:
    if c == 11:
      nj+=1
    elif c in h:
      h[c]+=1
    else:  
      h[c] = 1
  # check size, 5, 4, 3
  if nj == 5:
    r=[14]*5
  elif nj == 4: # make 5 of a kind..
    r=[a for a in h.keys()]*5
  elif nj == 3: # make into 4 of a kind.. (or 5)
    if len(h)==1:
      r=[a for a in h.keys()]*5
    else:
      r = [max(h.keys())]*4
      r = r + [min(h.keys())]
  elif nj == 2: # 3 cases xxx, xxy, xyz
    if len(h)==1:
      r=[max(h.keys())]*5
    elif len(h)==2:
      hc=0; lc=0;
      for x,y in h.items():
        if y==2:
          hc=x
        else:
          lc=x   
      r=[hc]*4 + [lc]
    else:
      c=[a for a in h.keys()]
      c.sort(reverse=True)
      r=[max(c),max(c)] + c
  elif nj==1: # 5 cases, xxxx, xxxy, xxyz, xxyy, xyzw
    if len(h)==4:
      c=[a for a in h.keys()]
      c.sort(reverse=True)
      r=[max(c)] + c
    elif len(h) == 3:
      hc=[]; lc=[];
      for x,y in h.items():
        if y==2:
          hc=[x,x,x]
        else:
          lc.append(x)
      r=hc+lc
    elif len(h)==2:
      p1=[]
      t1=[]; lc=[]
      for x,y in h.items():
        if y==2:
          p1=p1+[x,x]
          
        elif y==3:
          t1=[x,x,x,x]
        else:
          lc.append(x)
      if p1:
        hc=max(p1)
        p1.sort(reverse=True)
        r = [hc] + p1
      else:
        r=t1 + lc
    else:  # 4 of kind + J
      r=[max(h.keys())]*5
      
  else:
    r=h1
  return r
      
    
       
  

#now need to order hands return > 0 for h1, < 0 for h2, 0 for =
# [ hand, bid, representation, rnk, o_rep]
# check rank, check first
def cmp(h1,h2):
  if h1[3] > h2[3]:
    return 1
  elif h1[3] < h2[3]:
    return -1
  else:  # rnk is same.. now need algo to check order
    if h1[3]==6 or h1[3]==5:  # 5's or 4's
      if h1[4][0] > h2[4][0]:
        return 1
      elif h1[4][0] < h2[4][0]:
        return -1
      elif h1[4][4] > h2[4][4]:
        return 1
      elif h1[4][4] < h2[4][4]:
        return -1
      else:
        return 0
    elif h1[3] == 4: # FH
      if h1[4][0] > h2[4][0]:
        return 1
      elif h1[4][0] < h2[4][0]:
        return -1
      if h1[4][3] > h2[4][3]:
        return 1
      elif h1[4][3] < h2[4][3]:
        return -1
      else:
        return 0
    elif h1[3]==3: # trips
      if h1[4][0] > h2[4][0]:
        return 1
      elif h1[4][0] < h2[4][0]:
        return -1
      if h1[4][3] > h2[4][3]:
        return 1
      elif h1[4][3] < h2[4][3]:
        return -1
      elif h1[4][4] > h2[4][4]:
        return 1
      else:
        return -1
    elif h1[3] == 2:  # two pair
      if h1[4][0] > h2[4][0]:
        return 1
      elif h1[4][0] < h2[4][0]:
        return -1
      elif h1[4][2] > h2[4][2]:
        return 1
      elif h1[4][2] < h2[4][2]:
        return -1
      elif h1[4][4] > h2[4][4]:
        return 1
      else:
        return -1
    elif h1[3] == 1:  # one pair
      if h1[4][0] > h2[4][0]:
        return 1
      elif h1[4][0] < h2[4][0]:
        return -1
      elif h1[4][2] > h2[4][2]:
        return 1
      elif h1[4][2] < h2[4][2]:
        return -1
      elif h1[4][3] > h2[4][3]:
        return 1
      elif h1[4][3] < h2[4][3]:
        return -1
      elif h1[4][4] > h2[4][4]:
        return 1
      else:
        return -1
    else: # no pair, no ties?? shouldn't matter
      for i in range(0,5):
        if h1[4][i] > h2[4][i]:
          return 1
        elif h1[4][i] < h2[4][i]:
          return -1
      return 1
    rnk= h1[3]
    hnd1 = h1[4] 
    hnd2 = h2[4] 
    print(f"huh? rnk: {rnk}, hnd1: {hnd1}, hnd2: {hnd2}")
    return 0


# input [a,b,c,d,e] 2-14
# return rank, [ordered hand]
def getrnk(h):
  m = {}
  for x in h:
    if x in m:
      m[x]+=1
    else:
      m[x]=1
  if len(m) == 1:
    return 6, h
  if len(m) == 2:  # 4 or FH => (ttt,oo)
    s=0
    r=[]
    for k,v in m.items():
      if v==1:
        r = r + [k]
        s = 5
      elif v==2:
        r = r + [k, k]   
        s = 4
      elif v==3:
        r=[k,k,k]+r
        s = 4
      elif v==4:
        r = [k, k, k, k] + r
        s = 5
      else:
        print("wtf?")
    return s,r
      
  if len(m) == 3: # 3 or 2,2
  # need to either swap pairs, or swap singles on end.. for ordering
    s = 0
    r = []
    for k,v in m.items():
      if v==3:  # in this case, dealing with trips
        s = 3
        r = [k, k, k] + r
      elif v==2:  # in this case, dealing with two pair
        s = 2
        r = [k, k] + r
      else:
        r = r + [k]
    if s == 3:  
      y = r[3:]
      y.sort(reverse=True)
      r[3:] = y
    elif r[0] < r[2]:
      a = r[0]
      b = r[2]
      r = [b, b, a, a, r[4]]
    return s,r
      
   
  if len(m) == 4: # a pair

    r = []; l = []
    for k,v in m.items():
      if v == 2:
        r = [k,k] 
      else:
        l.append(k)
    l.sort(reverse=True)
    r = r + l
    return 1, r
  else:  # hand should be sorted, so just return 5 card hand
    return 0, h 

# part 1, apply rank, 
#for hand in hands:
#  hand.append(mh(hand[0]))
#  rnk,ohnd = getrnk(hand[2])
#  hand.append(rnk)
#  hand.append(ohnd)


# part 2, apply jokers to hand, get rank, convert jokers to 1 in representation
# for the purposes of compaing..
for hand in hands:
  hand.append(mh(hand[0])) # converts to numeric representation
  # apply jokers.. hand[2]
  hand.append(aj(hand[2]))
  for idx in range(len(hand[2])):
    if hand[2][idx] == 11:
      hand[2][idx] = 1 # set J to lowest number
      
  # aplly rank and order hand [3,4]
  # I went out of my way to sort the hand *ohnd*  but was not needed.. 
  rnk,ohnd = getrnk(hand[3]) 
  hand.append(rnk)
  hand.append(ohnd)

#for h in hands:
#  print(h)




  
# [chr, bid, map(int), rnk, ord_map(int)]
#print(hands)

# now sort em'
# hands = [[hand, rep, bid, rnk, ord_rep]]
#print(hands)
#for h in hands:
#  print(h)



go = True
end = len(hands)
while go:
  t=0
  for i in range(len(hands) -1):
    c = cmp2(hands[i],hands[i+1])
    if c < 0: # cmp returns negative, swap..
      #print(f"cmp {c}, swapping rnk: {hands[i][3]}:{hands[i][4]} with rnk: {hands[i+1][3]}:{hands[i+1][4]}")
      t1 = hands[i]
      t2 = hands[i+1] 
      hands[i]=t2
      hands[i+1]=t1
      #print(f"Swapped {i} and {i+1}")
      t+=1
  #print(f"completed iteration swaps = {t}")
  if t==0:
    go=False
     
# Debug - print the applied hands
# what is my order?
#for i in range(40):
#  print( hands[i] )
m=len(hands)
for h in hands:
  h.append(m)
  m-=1

for h in hands:
  print(f"{h[6]}, {h[:-1]}")
  


# get score: Sum(rank*bid)
m = len(hands)
score=0
for i in range(len(hands)):
  score+=m*int(hands[i][1])
  m-=1


print(f"Score: {score}")




