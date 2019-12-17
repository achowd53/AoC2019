def comp(filename,input_value=[]):
    p = [int(x) for x in open(filename).read().split(',')] 
    p += [0] * 10000
    relative = 0
    index = 0
    o = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    output = []
    #Manually calculated routes
    main = "A,B,A,B,C,C,B,C,B,A\n"
    A = "R,12,L,8,R,12\n"
    B = "R,8,R,6,R,6,R,8\n"
    C = "R,8,L,8,R,8,R,4,R,4\n"
    cvf = "n\n"
    input_value=[ord(s) for s in main+A+B+C+cvf]
    p[0] = 2
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
            output.append(position[0])
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
    print(output[-1])
comp("t17.txt")

