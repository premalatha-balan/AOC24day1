import re

f = open("day3_input.txt", "r")

memory = [line.strip() for line in f]

tot = 0
dontsplit = re.split(r'(don\'t\(\))', memory[0]) 
#print(dontsplit[0])
#print(dontsplit[1])
#print(dontsplit[2])
#print(dontsplit[3])
mulmatch=re.findall(r'(mul\((\d+\d*\d*),(\d+\d*\d*\)))',dontsplit[0])
#print(mulmatch)
mults = [int(j[1])*int(j[2].strip(")")) for j in mulmatch]
tot+=sum(mults)
print(f"tot is {tot}")


for i in range(len(memory)):
  print(memory[i] if i<10 else 'stop program')
  mulmatch=re.findall(r'(mul\((\d+\d*\d*),(\d+\d*\d*\)))',memory[i])

  mults = [int(j[1])*int(j[2].strip(")")) for j in mulmatch]
  tot+=sum(mults)
  #print(mults)
  #y= input("enter a key:")

print(tot)
#175615763 part1
