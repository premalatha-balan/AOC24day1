f = open("day1p1.txt", "r")

idlst1, idlst2 = [], []
lines_lst_str = f.readlines()
for line in lines_lst_str:
  line_lst = line.split()
  idlst1.append(int(line_lst[0]))
  idlst2.append(int(line_lst[1]))

ct = lambda same: idlst2.count(same)

score=0
for i in range(len(idlst1)):
  if i in idlst2: 
    score += ct(i)
print(score)