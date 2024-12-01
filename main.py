f = open("day1p1.txt", "r")

idlst1, idlst2 = [], []
lines_lst_str = f.readlines()
for line in lines_lst_str:
  #print(line)
  line_lst = line.split()
  #print(line_lst)
  idlst1.append(int(line_lst[0]))
  idlst2.append(int(line_lst[1]))
  #print(f"idlst1: {idlst1}")
  #print(f"and idlst2: {idlst2}")
  #y = input("enter a key :")

#print(f"idlst1: {idlst1}")
#print(f"and idlst2: {idlst2}")

idlst1.sort()
idlst2.sort()
dist = 0

diff = lambda x, y: abs(x - y)

for i in range(len(idlst1)):
  dist+=(diff(idlst1[i], idlst2[i]))
  """
  
  print(f"idlst1[{i}]: {idlst1[i]} and idlst2[{i}]: {idlst2[i]}")
  print(f"dist: {dist}")
  y = input("enter a key :") """

print(f"dist: {dist}")
