index = 0
#p is the puzzle input
def signal(setting, signalstrength,index,loop):
    p = [3,8,1001,8,10,8,105,1,0,0,21,34,51,64,81,102,183,264,345,426,99999,3,9,102,2,9,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,5,9,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,1002,9,5,9,4,9,99,3,9,102,3,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,5,9,101,3,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99]

    def smallercode(numoutputs,mode,puzzle,main = True):
        while (len(mode) < numoutputs):
                mode = "0" + mode
        #adds in non mentioned modes for arguments
        if main:
            assert mode[0] == "0"
            mode = "1" + mode[1:]
        output = [puzzle[index+x] if mode[-x] == "1" else puzzle[puzzle[index + x]] for x in range(1,numoutputs+1)]
        #makes each argument equal to position or value based on mode
        return output

    Nug = loop
    while True:
      
        opcode = p[index] % 100
        modes = str(p[index] // 100)
        if opcode == 1:
            i1,i2,i3 = smallercode(3,modes,p)
            #i1,i2, and i3 are the arguments after being set to either a value or a position
            p[i3] = i1 + i2
            index += 4
            #skips next 3 numbers since they were the arguments
        elif opcode == 2:
            i1,i2,i3 = smallercode(3,modes,p)
            p[i3] = i1 * i2
            index += 4
        elif opcode == 3:
            i1 = p[index+1]
            if Nug == False:
                p[i1] = setting #Input Number
            else:
                #print(signalstrength)
                p[i1] = signalstrength
            Nug = True
            index += 2
        elif opcode == 4:
            i1 = p[index+1]
            index += 2
            return p[i1],index
        elif opcode == 5:
            i1,i2 = smallercode(2,modes,p,False)
            if i1 != 0:
                index = i2
            else:
                index += 3
        elif opcode == 6:
            i1,i2 = smallercode(2,modes,p,False)
            if i1 == 0:
                index = i2
            else:
                index += 3
        elif opcode == 7:
            i1,i2,i3 = smallercode(3,modes,p)
            if i1 < i2:
                p[i3] = 1
            else:
                p[i3] = 0
            index += 4
        elif opcode == 8:
            i1,i2,i3 = smallercode(3,modes,p)
            if i1 == i2:
                p[i3] = 1
            else:
                p[i3] = 0
            index += 4
        else:
            assert opcode == 99,opcode
            return None,index

from itertools import permutations
l = list(permutations(range(5,10)))

ans = []
for x in l:
    b = True
    signals = [0 for z in range(5)]
    indexes = [0 for z in range(5)]
    loop = False
    while b:
        for y in range(5):
            test,indexes[y] = signal(x[y],signals[y],indexes[y],loop)
            #print(x,y,signals[y],indexes[y])
            if test == None:
                b = False
                break
            else:
                print(x,test)
                signals[(y+1)%5] = test
            #print(signals)
            ans.append(test)
        loop = True
print(max(ans))






