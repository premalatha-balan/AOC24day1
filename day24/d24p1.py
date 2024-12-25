
f = open("/workspaces/Advent-of-Code-2024/day24/testdata.txt", "r")
line = f.readlines()
#starts = [line[i].strip().split(": ") for i in range(90)]
#print(starts)
connects = [l.strip().split() for l in line]
#print(connects[91])
starts = connects[:10]
#print(starts[0])

starts_dict = {s[0].strip(":"):int(s[1]) for s in starts}

#print(starts_dict)
#print(starts[89])
#print(len(starts))
connects = connects[11:]
# print(connects[0])
# y=input("enter a key")


# for conx in connects:
#     match conx[1]:
#         case AND:
#             starts_dict[conx[0]]

# for s in starts_dict:
#     print(s)
#     print(starts_dict[s])
#     y = input("enter a key")

noConx = {0}
while True:
    # print(noConx)
    # y=input("enter a key")
    for conx in connects:
        if conx[4] not in starts_dict:
            if (conx[0] in starts_dict) and (conx[2] in starts_dict):
                # print(f"key = {conx[0]} and value is {starts_dict[conx[0]]}")
                # print(f"key = {conx[2]} and value is {starts_dict[conx[2]]}")
                # y=input("enter a key")
                match conx[1]:
                    case "AND":
                        # print(conx[0], starts_dict[conx[0]])
                        # print(conx[2], starts_dict[conx[2]])
                        # y=input("enter a key")
                        output = starts_dict[conx[0]]*starts_dict[conx[2]]
                        # print(f"{conx[4]} is {output} for {conx[1]}")
                        # y=input("enter a key")
                        starts_dict[conx[4]] = output
                    case "OR":
                        # print(conx[0], starts_dict[conx[0]])
                        # print(conx[2], starts_dict[conx[2]])
                        if starts_dict[conx[0]]+starts_dict[conx[2]] !=0: output = 1
                        else: output = 0
                        # print(f"{conx[4]} is {output} for {conx[1]}")
                        # y=input("enter a key")
                        starts_dict[conx[4]] = output
                    case "XOR":
                        # print(conx[0], starts_dict[conx[0]])
                        # print(conx[2], starts_dict[conx[2]])
                        if starts_dict[conx[0]]!=starts_dict[conx[2]]: output = 1 
                        else: output = 0
                        # print(f"{conx[4]} is {output} for {conx[1]}")
                        # y=input("enter a key")
                        starts_dict[conx[4]] = output
                # print(f"key is {conx[4]} and value is {output}")
                # print(f"key is {conx[4]} and value is {starts_dict[conx[4]]}")
                # y=input("enter a key")
            elif conx[0] not in starts_dict:
                noConx.add(conx[0])
            elif conx[2] not in starts_dict:
                noConx.add(conx[2])
            else: noConx.add(conx[4])
    
    common = set(starts_dict.keys()) & noConx
    for k in common:
        noConx.remove(k)

    if len(noConx)<2: break

# print(len(starts_dict))
# print(len(noConx))

zs={s:starts_dict[s] for s in starts_dict if s[0]=="z"}
# print(zs)
# print(len(zs))    
zs_keys = list(zs.keys())
zs_keys.sort(reverse=True)
# print(zs_keys)

zbin_lst = [str(zs[sk]) for sk in zs_keys]
#print(zbin_lst)
zbin = "".join(zbin_lst)
print(zbin)
print(int(zbin,2))

#first attempt answer is 2166808167225 is too low
#reversing gives        21545258828784 is too low 100111001100001100101011111111100001111110000