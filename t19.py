filename = str(input("Filename: "))
filename = open(filename)
def comp(filename,input_value,memory):
    p = [int(x) for x in open(filename).read().split(',')] 
    p += [0] * (memory - len(p))
    relative = 0
    index = 0
    o = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    while (p[index] != 99):
        modes = [int(x) for x in str(p[index])[:-2]][::-1] + [0,0,0]
        opcode = int(str(p[index])[-2:])
        position = [p[index+x+1] if modes[x]==1 else p[(relative if modes[x]==2 else 0)+p[index+x+1]] for x in range(o[opcode])]
        if opcode == 1:
            p[(relative if modes[2]==2 else 0)+p[index+3]] = position[0]+ position[1]
        elif opcode == 2:
            p[(relative if modes[2]==2 else 0)+p[index+3]] = position[0]* position[1]
        elif opcode == 3:
            p[(relative if modes[0] == 2 else 0) + p[index+1]] = input_value[0]
            input_value.pop(0)#Input Value
        elif opcode == 4:
            return position[0]
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
ans = 0
for y in range(50):
    for x in range(50):
        c = comp(filename, [x,y], 10000)
        if c == 1:
            ans+=1
print(ans)

checky = 10000 
checkx = 10000

for y in range(100,checky): 
    done = False
    for x in range(checkx):
        c = comp(filename, [x,y], 10000)
        if c == 1:
            if comp(filename, [x+99,y-99], 10000) == 1:
                print(x * 10000 + y-99)
                done = True
            break
    if done:
        break
