
def unsafeSeries(a):
  if len(a)<3: print(len(a))
  minus_f = a[0] - a[1]
  if minus_f == 0 or abs(minus_f)>3 or abs(minus_f) <1:
    return False 
  if minus_f>0: # decreasing series
    for i in range(1,len(a)-1):
      minus = a[i] - a[i+1]
      if minus <= 0: #increased
        return False
      elif abs(minus) > 3: # difference is bigger than 3
        return False
      elif abs(minus)<1: # difference is less than 1
        return False
      else: continue 
    return True
  elif minus_f<0: #increasing series
    for i in range(1, len(a)-1):
      minus = a[i] - a[i+1]
      if minus >= 0: #decreased
        return False
      elif abs(minus) > 3: # difference is bigger than 3
        return False
      elif abs(minus)<1: # difference is less than 1
        return False
      else: continue 
    return True 
  else: return False

  

f = open("day2_input.txt", "r")

line_lst_str = f.readlines()

print(len(line_lst_str))

reports=[]

for line in line_lst_str:
  line_lst = [int(i) for i in line.split()]

  if unsafeSeries(line_lst):
    reports.append(line_lst)
  else:
    #print(line_lst)
    #y = input("enter a key:")
    for i in line_lst:
        #new_line =[j for j in line_lst if j!=i]
        new_line = line_lst.copy()
        new_line.remove(i)
        #print(f"line_lis: {line_lst}")
        #print(f"new_line: {new_line}")
        #y = input("enter a key:")
        #if len(new_line)<3:
          #print(f"this is new_line {new_line}")
          #y = input("enter a key:")
        if unsafeSeries(new_line):
          reports.append(new_line)
          break
      
        



"""   #print(line_lst)
    #y = input("enter a key:") 
  elif len(line_lst)>2:
    print(f"calling from the unsafe loop: length = {len(line_lst)}")
    for i in line_lst:
      new_line =[j for j in line_lst if j!=i]
      #print(new_line)
      if unsafeSeries(new_line):
      #print(f"ncount is {ncount}")
      #y = input("enter a key:")
        reports.append(new_line)
        #print(f"added {new_line}")
        #y = input("enter a key:")
  else: 
    print(f"unsafe and small: {len(line_lst)}")
    y = input("enter a key:") 
"""

print(len(reports))

    
  

  
    
