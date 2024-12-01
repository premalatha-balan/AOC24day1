f = open("day1_input.txt", "r")

idlst1, idlst2 = [], []
lines_lst_str = f.readlines()
for line in lines_lst_str:
  line_lst = line.split()
  #print(line_lst)
  idlst1.append(int(line_lst[0]))
  idlst2.append(int(line_lst[1]))

ct = lambda same: idlst2.count(same)

score=0
for i in idlst1:
  if i in idlst2: 
    score += ct(i)*i
print(score)

