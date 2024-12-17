import re

def split_n_del(line):
  new_line=re.split(r'(do\(\))', line)
  new_line.pop(0)
  return new_line [1::2]



f = open("day3_input.txt", "r")

memory = [line.strip() for line in f]

tot = 0
dontsplit = re.split(r'(don\'t\(\))', memory[0]) 

mulmatch=re.findall(r'(mul\((\d+\d*\d*),(\d+\d*\d*\)))',dontsplit[0])

mults = [int(j[1])*int(j[2].strip(")")) for j in mulmatch]
tot+=sum(mults)
print(f"tot is {tot}")

allnotdonts = dontsplit[2::2]

dotext = split_n_del(allnotdonts[-1])

dotextall=[]
for i in range(len(allnotdonts)):
  dotext = split_n_del(allnotdonts[i])
  if len(dotext)!=0: dotextall.extend(dotext)

#print(f"length of useful text is {len(dotextall)}")
#y = input("enter a key:")
for j in range(1,len(memory)):
  dontsplit = re.split(r'(don\'t\(\))', memory[j])
  if dontsplit[0]!="don\'t()":
    allnotdonts = dontsplit[::2]
    #print("first is not don't")
  else:
    allnotdonts = dontsplit[1::2]
    #print("first is don't")
  #print(len(allnotdonts))
  #y = input("enter a key:")

  for i in allnotdonts:
    dotext = split_n_del(i)
    if len(dotext)!=0: dotextall.extend(dotext)
    #print(f"length of useful text is {len(dotextall)}")
    #y = input("enter a key:")

for i in dotextall:
  mulmatch=re.findall(r'(mul\((\d+\d*\d*),(\d+\d*\d*\)))',i)
  
  mults = [int(j[1])*int(j[2].strip(")")) for j in mulmatch]
  tot+=sum(mults)
  #print(mults)
  #y= input("enter a key:")

print(tot)
#175615763 part1
