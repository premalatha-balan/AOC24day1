import re

f = open("day3_input.txt", "r")

memory = [line.strip() for line in f]
#print(f"length of memory is {len(memory)}")

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

for i in range(2,len(dontsplit)):
  #print(dontsplit[i])
  if dontsplit[i]!="don\'t\(\)":
    newsplit=re.split(r'(do)', dontsplit[i])
    newsplit.pop(0)
    #print(len(newsplit))
    #y=input("enter a key:")
    if len(newsplit)!=0:
      for dos in newsplit:
        mulmatch=re.findall(r'(mul\((\d+\d*\d*),(\d+\d*\d*\)))',dos)
        mults = [int(j[1])*int(j[2].strip(")")) for j in mulmatch]
        tot+=sum(mults)
      #print(f"tot is {tot}")
print(f"tot is {tot}")

for m in range(1,len(memory)):
  #print(f"I am inside the new loop")
  dontsplit = re.split(r'(don\'t\(\))', memory[m])
  print(len(dontsplit))

  for d in range(len(dontsplit)):
    if dontsplit[d]!="don\'t":
      newsplit=re.split(r'(do\(\))', dontsplit[d])
      newsplit.pop(0)
      #print(len(newsplit))
      #y=input("enter a key:")
      if len(newsplit)!=0:
        for dos in newsplit:
          mulmatch=re.findall(r'(mul\((\d+\d*\d*),(\d+\d*\d*\)))',dos)
          mults = [int(j[1])*int(j[2].strip(")")) for j in mulmatch]
          #if len(newsplit)<=2:
            #print(f"mults is {mults}")
          tot+=sum(mults)
        print(f"tot is {tot}")

  

print(tot)
#175615763 part1

#66993248
#64351118
#2036780
#2642130
#8621928