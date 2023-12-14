#!/usr/bin/python3
import sys

# generate permutations of say 'AAABBBB'
# N=7, M=3

def swap(t,i,j):
  l=[x for x in t]
  print(f"Swaping {l} on {i},{j}")
  e=l[j]
  l[j]=l[i]
  l[i]=e
  return l 

# permutations of length N with M 'C's and N-M D's
def perms(p,N,M,res, C='A',D='B'):
  # print(f"perms {N},{M} {p}")
  assert N>=0
  assert N>=M
  # N==0 is end condition, accumulate
  if N==0 and M==0:
    for i in range(len(p)):
      #p[i]+=D
      res.append(p[i])
  elif N==0 and M==1:
    for i in range(len(p)):
      #p[i]+=C
      res.append(p[i])
  elif M==0:
    if p:  
      for i in range(len(p)):
        p[i]+=D
    else:  # edge condition if initial M = 0
      p.append(D)
    perms(p,N-1,M,res,C,D)
  elif N==M:
    if p:
      for i in range(len(p)):
        p[i]+=C
    else:  # edge condition if initial M = N
      p.append(C)
    perms(p,N-1,M-1,res,C,D)
  else:  # double p
    L=[]
    R=[]
    if p:
      for i in range(len(p)):
        L.append(p[i]+C)
        R.append(p[i]+D)
    else:
      L.append(C)
      R.append(D)
    perms(L,N-1,M-1,res,C,D)
    perms(R,N-1,M,res,C,D)
  

if __name__=='__main__':
  if len(sys.argv) < 3:
    print("Usage: ./perms.py <n> <m>")
    exit() 
  
  N=int(sys.argv[1])
  M=int(sys.argv[2])
  print(f"Permutations with N={N}, M={M}")
  output=[]
  perms([],N,M,output)
  
  for e in output:
    print(e)
  
