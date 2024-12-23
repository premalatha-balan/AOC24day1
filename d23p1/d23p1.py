
f = open("/workspaces/Advent-of-Code-2024/d23p1/day23_input.txt", "r")

line = f.readlines()
nets = [i.strip().split("-") for i in line]

for i in nets:
    if (i[0][0] or i[1][0]) == "t":
        print(i)
        y=input("enter a key")
        for j in nets:
            if (i[0] or i[1]) in j and (i!=j):
                print(j)
                y=input("enter a key")
                if j[0] not in i:
                    

