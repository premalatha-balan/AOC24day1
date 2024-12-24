

f = open("/workspaces/Advent-of-Code-2024/d23p1/day23_input.txt", "r")

line = f.readlines()
nets = [i.strip().split("-") for i in line]



count = 0
# for i in nets:
#     if (i[0][0] or i[1][0]) == "t":
#         #print(i)
#         #y=input("enter a key")
#         for j in nets:
#             if (i[0] or i[1]) in j and (i!=j):
#                 #print(j)
#                 #y=input("enter a key")
#                 if (j[0] not in i) and (i[1] not in j):
#                     if ([j[0],i[1]] in nets): count+=1
#                 elif (j[0] not in i) and (i[0] not in j):
#                     if ([j[0],i[0]] in nets): count+=1
#                 elif (j[1] not in i) and (i[1] not in j):
#                     if ([j[1],i[1]] in nets): count+=1
#                 elif (j[1] not in i) and (i[0] not in j):
#                     if ([j[1],i[0]] in nets): count+=1
#                 #print(f"count = {count} for {i} and {j}")
#                 #y = input("enter a key")



# def triangle(t_list, big_list):
#     for i in big_list:
#         if i!=t_list[0]:
#             if i[0] == t_list[0] and [i[1],t_list[1]] in big_list: count+=1

# for i in nets:
#     if (i[0][0] or i[1][0]) == "t":
#         for j in nets:
#             if i!=j and ((j[0] in i) or (j[1] in i)):
#                 #print(f"i={i} and j={j}")
#                 #y=input("enter a key")

#                 ti = 

#                 # if i[0][0]=="t": 
#                 #     apex1=i[1]

#                 # elif i[1][0]=="t": apex1=i[0]
#                 # else: apex1 =""
#                 # if j[0][0]=="t": apex2=j[1]
#                 # elif j[1][0]=="t": apex2=j[0]
#                 # else: apex2=""
#                 # if ([apex1, apex2] in nets) or ([apex2, apex1] in nets): count+=1


apex1, apex2 = "", ""

# for i in nets:
#     if (i[0][0] or i[1][0]) == "t":
#         for j in nets.remove(i):
#             if j[0] or j[1] in i:
#                 if j[0] == i[0]:
#                     apex1=j[1]
#                     apex2=i[1]
#                 elif j[0] == i[1]:
#                     apex1=j[1]
#                     apex2=i[0]
#                 elif j[1]==i[0]:
#                     apex1=j[0]
#                     apex2=i[1]
#                 elif j[1]==i[1]:
#                     apex1 = j[0]
#                     apex2 = i[2]


for i in nets:
    if (i[0][0] or i[1][0]) == "t":
        for j in nets.remove(i):
            if j[0] or j[1] in i:
                match(j[0]):
                    case i[0]:
                        apex1=j[1]
                        apex2=i[1]
                    case i[1]:
                        apex1=j[1]
                        apex2=i[0]
                match (j[1]):
                    case i[0]:
                        apex1=j[0]
                        apex2=i[1]
                    case i[1]:
                        apex1=j[0]
                        apex2=i[0]

                


                



print(f"count = {count}")





    





