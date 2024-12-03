import re

f = open("day3_input.txt", "r")

memory = [line.strip() for line in f]

tot = 0
for i in range(len(memory)):
  mulmatch=re.findall(r'(mul\((\d+\d*\d*),(\d+\d*\d*\)))',memory[i])

  mults = [int(j[1])*int(j[2].strip(")")) for j in mulmatch]
  tot+=sum(mults)
  #print(mults)
  #y= input("enter a key:")

print(tot)
#175615763 part1
