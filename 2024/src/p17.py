#!python
"""
   A computer problem!

   3 bit instructions..  
   3 bit operands
   Registers...
 
   Need to just implement fn(inst, op)
   There is also an instruction pointer, which by default will go up by 2

   Reminders on binary math (on integers, representations in binary)
   a|b  -> OR
   a^b  -> XOR : a or b but not both..
   a&b  -> AND 
   a>>2 -> right shift by 2..  N->divide by 2**N, dropping remainder
   a<<2 -> left shift by 2..   N->multipley by 2**N


"""
import re

d="../data/17b.txt"
with open(d) as f:
  inst = f.read().strip().split("\n\n")

reg=list(map(int, re.findall(r"\d+",inst[0],flags=re.DOTALL)))
inst=list(map(int,re.findall(r"\d+",inst[1])))
print(reg)
print(inst)


def combo(op):
  if op < 4:
    return op
  elif op < 7:
    return reg[op-4]
  else:  # 7 is invald
    print(f"WARNING: Invalid opcode {op}")

# read op code, read operand, return new value of instruction pointer
def proc(idx, inst, reg, output):
  op=inst[idx]
  #print(f"Op is {op}")
  if op==0:     # adv
    reg[0] = int(reg[0]/2**combo(inst[idx+1]))
  elif op==1:   # bxl
    reg[1] = reg[1]^inst[idx+1]
  elif op==2:   # bst
    reg[1] = combo(inst[idx+1])%8
  elif op==3:   # jnz
    if reg[0]!=0:
      # print(f"JNZ to {inst[idx+1]}")
      # jump the instruction pointer..
      return inst[idx+1]
  elif op==4:   # bxc
    reg[1]=reg[1]^reg[2]
  elif op==5:   # out
    output.append(combo(inst[idx+1])%8)
  elif op==6:   # bdv
    reg[1] = int(reg[0]/2**combo(inst[idx+1]))
  elif op==7:   # cdv
    reg[2] = int(reg[0]/2**combo(inst[idx+1]))
  else:
    print("Noop")
  return idx+2
 

    

input = inst.copy()
a=0; b=0
while True:
  idx=0
  output=[]
  reg = [a,0,0]
  while True:
    if idx>=len(inst):
      break
    if len(output) > 5*len(input):  # lets just see if there's some weird cases..
      break
    # run the program at inst[idx]
    idx=proc(idx,inst,reg,output)
  a+=1
  
  same = (output == input)
  if same:
    print(f"Reg A: {a}, final output: {",".join(map(str,output))}, same: {same}")
    break
  





