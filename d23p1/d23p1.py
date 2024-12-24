import fnmatch

def tri_match(a, b, in_lst):
    if a[0]==b[0]:
        apex1=a[1]
        apex2=b[1]
    elif a[1]==b[1]:
        apex1=a[0]
        apex2=b[0]
    elif a[0]==b[1]:
        apex1 = a[1]
        apex2 = b[0]
    elif a[1]==b[0]:
        apex1=a[0]
        apex2=b[1]
    elif a[0]==b[1]:
        apex1=a[1]
        apex2=b[0]
    

    # for k in in_lst:
    #     if ([apex1, apex2] in k) or ([apex2, apex1] in k): return k

    return apex1, apex2

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


# for i in nets:
#     if (i[0][0] or i[1][0]) == "t":
#         for j in nets:
#             if (j[0] or j[1] in i) and j!=i:
#                 match(j[0]):
#                     case i[0]:
#                         apex1=j[1]
#                         apex2=i[1]
#                     case i[1]:
#                         apex1=j[1]
#                         apex2=i[0]
#                 match (j[1]):
#                     case i[0]:
#                         apex1=j[0]
#                         apex2=i[1]
#                     case i[1]:
#                         apex1=j[0]
#                         apex2=i[0]
#                 if ([apex1, apex2] in nets) or ([apex2, apex1] in nets): count+=1

#triangle = [(i, j, k) for i in nets for j in nets for k in nets if ((i!=j and i!=k and j!=k) and ((i[0][0]=="t") or (i[1][0]=="t")) and ((j[0] in i) or j[1] in i) and ((k[0] in i and k[1] in j) or (k[1] in i and k[0] in j)))]

#print(f"{triangle} length of triangle is {len(triangle)}")


#triangle = [(k[0], k[1], new) for k in double if (tri_match[k[0], k[1], nets][0] in nets or (tri_match(k[0], k[1], nets)[1] in nets)) ]

# for k in double:
#     new = tri_match(k[0], k[1], nets)
#     if (new[0] in nets) or new[1] in nets: 
#         count+=1
#         print(f"k[0] = {k[0]}, k[1] = {k[1]} and new[0] = {new[0]}")
#         y=input("enter a key")

# print(f"count = {count}")


# double = [(i, j) for i in nets for j in nets if ((i!=j) and ((i[0][0]=="t") or (i[1][0]=="t")) and ((j[0] in i) or j[1] in i) )]


# for k in double:
#     apex1, apex2 = tri_match(k[0], k[1], nets)
#     if ([apex1, apex2] in nets or [apex2, apex1] in nets):
#         count+=1
#         print(f"double is {k} and match is {apex1, apex2}")
#         print(f"count is {count}")
        
#         apex3 = list(set(k[0])&set(k[1]))
#         print(f"apex3 is {apex3}")
        
#         tri = set([apex1, apex2, apex3[0]])
#         tri_l  = [apex1, apex2, apex3[0]]
#         print(f"tri is {tri}")
#         y=input("enter a key")




double = [(i,j) for i in nets for j in nets if ((i!=j) and any(x in i for x in j) and ((i[0][0]=="t") or (i[1][0]=="t"))) ]
print(len(double))
# triangle = set()
# triangle.add((1,2,3))
# triangle.add((3,2,1))
# test_triangle = list(dict.fromkeys({1,2,3}, {3,2,1}))
# print(f"triangle is {triangle}")
# print(f"test_triangle is {test_triangle}")
# y=input("enter a key")
triangle = []
for i in double:
    common = list(set(i[0])&set(i[1]))
    #print(f"common ={common[0]}")
    threes = set (i[0]+i[1])
    twos =[x for x in threes if x != common[0]]
    # print(f"triangle is {triangle}")
    # print(f"threes is {threes}")
    # y=input("enter a key")
    if threes not in triangle:
        # print(f"triangle is {triangle}")
        # print(f"threes is {threes} and twos is {twos}")
        # y=input("enter a key")
        if ((twos[0], twos[1] in nets) or (twos[1], twos[0] in nets)): triangle.append(threes)
        #if (twos[0], twos[1])in nets: triangle.append
            # print(f"in nets twos is {twos[0]}-{twos[1]} and threes is {threes}")
            # print(f"i is {i} and common is {common[0]}")
            # y=input("enter a key")
        #if (twos[1], twos[0] in nets):triangle.append
            # print(f"in nets twos is {twos[1]}-{twos[0]} and threes is {threes}")
            # print(f"i is {i} common is {common[0]}")     
            # y=input("enter a key")   
    #if (twos[0], twos[1])in nets or (twos[1], twos[0] in nets) and (threes not in triangle) : triangle.append(threes)

        


#second attempt answer is 4376 - too high
#third attempt answer is 5256 - too high
#fourth attempt answer is 1738 - too high
print(triangle)
#print(len(triangle))


#print(f"count = {count}")





    





