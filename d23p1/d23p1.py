
f = open("/workspaces/Advent-of-Code-2024/d23p1/day23_input.txt", "r")

line = f.readlines()
nets = [i.strip().split("-") for i in line]

count = 0
# for i in nets:
#     if (i[0][0] or i[1][0]) == "t":
#         print(i)
#         y=input("enter a key")
#         for j in nets:
#             if (i[0] or i[1]) in j and (i!=j):
#                 print(j)
#                 y=input("enter a key")
#                 if (j[0] not in i) and (i[1] not in j):
#                     if ([j[0],i[1]] in nets): count+=1
#                 elif (j[0] not in i) and (i[0] not in j):
#                     if ([j[0],i[0]] in nets): count+=1
#                 elif (j[1] not in i) and (i[1] not in j):
#                     if ([j[1],i[1]] in nets): count+=1
#                 elif (j[1] not in i) and (i[0] not in j):
#                     if ([j[1],i[0]] in nets): count+=1
#                 print(f"count = {count} for {i} and {j}")
#                 y = input("enter a key")



    





