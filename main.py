
diff = lambda a, b: abs(a-b)

def pos(a0, a1):
  if a0 > a1:
    return True
  else: return False


def unsafeOrder(a):
  if pos(a[0] ,a[1]): # decreasing series
    for i in range(1,len(a)-1):
      if pos(a[i], a[i+1]):
        if diff(a[i], a[i+1])<=3 and diff(a[0], a[i])>=1:
          return True
        else: return False
      else: return False 
  else: #increasing series
    for i in range(1, len(a)-1):
      if pos(a[i], a[i+1]): #decreasing 
        return False
      else: 
        if diff(a[i], a[i+1]<=3) and diff(a[0], a[i])>=1:
          return True
        else: return False


f = open("day2_input.txt", "r")

line_lst_str = f.readlines()

print(len(line_lst_str))

reports=[]

for line in line_lst_str:
  line_lst = [int(i) for i in line.split()]

  #print(line_lst)
  #print(unsafeOrder(line_lst))
  #y = input("enter a key:")
  if unsafeOrder(line_lst):
    reports.append(line_lst)
  

#reports = [[int(i) for i in line.split()] for line in line_lst_str if unsafeOrder([int(i) for i in line.split()])]

print(len(reports))
#print(reports)