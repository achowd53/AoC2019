import matplotlib.pyplot as m
import numpy as np
def comp(start,filename,memory=10000):
    p = [int(x) for x in open(filename).read().split(',')] 
    p += [0] * (memory - len(p))
    o = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    index = 0
    relative = 0
    pos = (0,0)
    grid = {(0,0):start}
    t = 1
    tv = [(1,0),(0,1),(-1,0),(0,-1)]
    output = []
    while (p[index] != 99):
        modes = [int(x) for x in str(p[index])[:-2]][::-1] + [0,0,0]
        opcode = int(str(p[index])[-2:])
        position = [p[index+x+1] if modes[x]==1 else p[(relative if modes[x]==2 else 0)+p[index+x+1]] for x in range(o[opcode])]
        if opcode == 1:
            p[(relative if modes[2]==2 else 0)+p[index+3]] = position[0]+ position[1]
        elif opcode == 2:
            p[(relative if modes[2]==2 else 0)+p[index+3]] = position[0]* position[1]
        elif opcode == 3:
            p[(relative if modes[0] == 2 else 0) + p[index+1]] = 0 if pos not in grid else grid[pos]#Input Value
        elif opcode == 4:
            output.append(position[0])
            if len(output) == 2:
                grid[pos] = output[0]
                if output[1] == 0:
                    t -= 1
                else:
                    t += 1
                t = t % 4
                x,y = tv[t] 
                pos = (pos[0]+x,pos[1]+y)
                output = []
        elif opcode == 5:
            index = (position[1]- 3 if position[0]!= 0 else index)
        elif opcode == 6:
            index = (position[1]- 3 if position[0]== 0 else index)
        elif opcode == 7:
            p[(relative if modes[2] == 2 else 0) + p[index+3]] = (1 if position[0]< position[1]else 0)
        elif opcode == 8:
            p[(relative if modes[2] == 2 else 0) + p[index+3]] = (1 if position[0]== position[1]else 0)
        elif opcode == 9:
            relative += position[0]
        index += o[opcode] + 1
    if start == 0:
        print(len(grid))
    else:
        out = []
        for x in grid:
            if grid[x] == 1:
                a,b = x
                out.append((-a,b))
        print(out)
filename = input("Name of File: ")
print()
print("Part 1:")
comp(0,filename)
print()
print("Part 2: ")
comp(1,filename)
print("Copy this point dump excluding brackets and put into https://www.desmos.com/calculator/mhq4hsncnh")
