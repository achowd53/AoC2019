from itertools import permutations
moons = {1:[0,4,0,0,0,0],2:[-10,-6,-14,0,0,0],3:[9,-16,-3,0,0,0],4:[6,-1,2,0,0,0]}
#Manually input original values in form of a dict where keys are 1,2,3,4 and values are the moon's posx,poy,posz,velx,vely,velz
pairs = list(permutations(moons,2))
for steps in range(1000):
    pairs = list(permutations(moons,2))
    for x in pairs:
        a,b = x
        for z in range(3):
            if moons[a][z] > moons[b][z]:
                moons[a][z+3] -= .5
                moons[b][3+z] += .5
            elif moons[a][z] < moons[b][z]:
                moons[a][3+z] += .5
                moons[b][3+z] -= .5

    for x in moons:
        for z in range(3):
            moons[x][z] += moons[x][z+3]
total = 0
for x in moons:
    y = moons[x]
    PE = abs(y[0])+abs(y[1])+abs(y[2])
    KE = abs(y[3])+abs(y[4])+abs(y[5])
    TE = PE * KE
    total += TE
print(total)


end = 1
moons = {1:[0,4,0,0,0,0],2:[-10,-6,-14,0,0,0],3:[9,-16,-3,0,0,0],4:[6,-1,2,0,0,0]}
#same as at the top
pairs = list(permutations(moons,2))
steps = 0
rx = [[0,-10,9,6,0,0,0,0]]
ry = [[4,-6,-16,-1,0,0,0,0]]
rz = [[0,-14,-3,2,0,0,0,0]]
ax = True
bx = True
cx = True
factors = 0
while True:
    steps += 1
    pairs = list(permutations(moons,2))
    for x in pairs:
        a,b = x
        for z in range(3):
            if moons[a][z] > moons[b][z]:
                moons[a][z+3] -= .5
                moons[b][3+z] += .5
            elif moons[a][z] < moons[b][z]:
                moons[a][3+z] += .5
                moons[b][3+z] -= .5
    for x in moons:
        for z in range(3):
            moons[x][z] += moons[x][z+3]
    mx = [moons[x][0] for x in range(1,5)] + [moons[x][3] for x in range(1,5)]
    my = [moons[x][1] for x in range(1,5)] + [moons[x][4] for x in range(1,5)]
    mz = [moons[x][2] for x in range(1,5)] + [moons[x][5] for x in range(1,5)]
    if mx in rx and ax:
        factors += 1
        ax = False
        endx = steps
    if my in ry and bx:
        factors += 1
        bx = False
        endy = steps
    if mz in rz and cx:
        factors += 1
        end = np.lcm(end,steps)
        cx = False
        endz = steps
    if factors == 3:
        break
def f(x,y):
    return x if y==0 else f(y, x%y)
def lcm(x, y):
   return (x*y)//f(x,y)   
print(lcm(lcm(endx,endy),endz))
   
    




    
