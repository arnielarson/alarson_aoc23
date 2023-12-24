#!/usr/bin/python3
import sys
import re
import queue

print("hello day 20")
"""
  Pulses between comms modules..
 
  Part1 Objective is to count all the pulses

  Problem is to figure out how to propagate data in the 
  network.  Settling on a strategy of (pulse, to_id, from_id)
  Only conjunciton modules will care about the from_id

  Part2 Find when module rx get's pulsed low... 
  Naive solution didn't finish (in 12 hours), so..
  Appears need a trick to find.
  rx is connected to tg.
  tg is fed by ln, db, vq, tf...
  rx will be pulsed low when tg is pulsed high w/ all other inputs high
  so finding cylces for inputs to tg will find the answer
 
"""



# Manage the pusles between modules
q=queue.Queue()
# Ok - track modules, 1 broadcaster + flip flops and conjunction modules
m={}

# Output class, is a noop
class OUT:
  def __init__(self,sid):
    self.sid=sid

  def add_con(self,con):
    pass
  # this module doesn't care about input id, so noop to keep code symmetric..
  def add_input(self,c):
    pass
  # just to track the pulses..
  def pulse(self, p):
    return p[0]
  


# Flip flop, one input one output
class FF:
  def __init__(self,sid,on=False):
    self.sid=sid
    self.on=on
    self.dest=[]

  def add_con(self,con):
    self.dest.append(con)
  # this module doesn't care about input id, so noop to keep code symmetric..
  def add_input(self,c):
    pass

  # on low pulse, flips state and sends a high pulse if it was off, low pulse if it was on
  def pulse(self,p):
    if p[0]==0:
      self.on= not self.on
      if self.on: # send high
        for d in self.dest:
          q.put((1,d,self.sid))
      else:  # it was on now is off, send low
        for d in self.dest:
          q.put((0,d,self.sid))
    return p[0]
        

# Conjunction, multi input/output
class CNJ:
  
  def __init__(self,sid):
    self.sid=sid
    self.inputs={}
    self.dest=[]

  def add_input(self,c):
    self.inputs[c]=0

  # this is an output
  def add_con(self,c):
    self.dest.append(c)
    
  # update input pulse, then send output pulses
  def pulse(self,p):
    self.inputs[p[2]]=p[0]
    val=1
    for k in self.inputs.keys():
      val*=self.inputs[k]
    if val:
      for v in self.dest:
        q.put((0,v,self.sid))
    else:
      for v in self.dest:
        q.put((1,v,self.sid))
    return p[0]
      
      
# Broadcast module, sends output to each of it's outputs
class BRO:
  # input is a list of ids
  def __init__(self,vals=[]):
    self.vals=vals
  def add_con(self, v):
    self.vals.append(v)
  def count_low_pulses(self):
    return len(self.vals)

  def push_button(self):
    for v in self.vals:
      q.put((0,v,None))


"""
  First get all the labeled modules
  Then second pass to create all the connections
"""
def parse_input(D):
  for line in D:
    d = line.split("->")
    if d[0].strip() == 'broadcaster':
      #print("adding broadcaster")
      b=BRO()
      for v in d[1].split(","):
        b.add_con(v.strip())
    elif d[0][0]=='%':
      s=d[0].strip()[1:]
      #print(f"adding flip flop {s}")
      m[s]=FF(s)
    elif d[0][0]=='&':
      s=d[0].strip()[1:]
      #print(f"adding conj mod {s}")
      m[s]=CNJ(s)
  # Now add connections
  for line in D:
    d = line.split("->")
    if d[0][0]=='%' or d[0][0]=='&':
      k=d[0].strip()[1:]
      for v in d[1].split(","):
        v=v.strip()
        if v not in m:
          m[v]=OUT(v)
        m[k].add_con(v)
        m[v].add_input(k) # needed for conj
      
  return b
      

       



if __name__=='__main__':
  if len(sys.argv)==1:
    fname="d20.txt"
  elif sys.argv[1]=='t1':
    fname="d20t1.txt"
  elif sys.argv[1]=='t2':
    fname="d20t2.txt"
  D = open("../data/" + fname).read().strip().split("\n")
  b=parse_input(D)


  lp=0
  hp=0
  # start the algorithm by pushing the button...
  # part 1 - add up the high and low pulses
  # part 2 find when rx gets a 0?
  #        search for cycles for the module tg inputs which 
  #        outputs to rx; inputs to tg: {ln, db, vq, tf}
  i=0
  while i > -1:
    i+=1
    #lp+=1
    b.push_button()
    while q.qsize() > 0:
      p=q.get()
      if p[0]==1 and p[1]=='tg' and p[2]=='tf':
        print(f"press {i}, order {j}, Pulsing:  {p}")
        
      #print(f"Pulse: {p}")
      m[p[1]].pulse(p)
      j+=1
      #  hp+=1
      #else:
      #  lp+=1
  print(f"low pulses:   {lp}\nhigh pulses: {hp}")
  print(f"lp*hp:  {lp*hp}")






