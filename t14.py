import math
reactions = {}
filename = "t14.txt"
for line in open(filename).read().strip().split("\n"):
    k,v = line.split(" => ")
    k = k.split(', ')
    k = [(int(x.split(" ")[0]),x.split(" ")[1]) for x in k]
    v = (v.split(" ")[0],v.split(" ")[1])
    reactions[v[1]] = (int(v[0]),k)
def fuelsearch(fuel):
    ore = 0
    search = ["FUEL"] #search is what you're trying to produce
    amount = [fuel] #amount is how much of the corresponding search you want
    excess = {} #excess is all the extra chemicals produced in each reaction
    while len(search) > 0:
        if search[0] in excess:
            s = search[0]
            a = amount[0]
            if a >= excess[s]:
                amount[0] -= excess[s]
                excess[s] = 0
            if excess[s] > a:
                excess[s] -= a
                search.pop(0)
                amount.pop(0)
                continue               
        if search[0] == "ORE":
            ore += amount[0]
            search.pop(0)
            amount.pop(0)
            continue
        mult = math.ceil(amount[0]/reactions[search[0]][0])
        recieved = mult * reactions[search[0]][0]
        if search[0] in excess:
            excess[search[0]] += recieved - amount[0]
        else:
            excess[search[0]] = recieved - amount[0]
        reaction = reactions[search[0]][1]
        for y in reaction:
            search.append(y[1])
            amount.append(y[0]*mult)
        search.pop(0)
        amount.pop(0)
    return ore
print(fuelsearch(1))
#playing hi-lo game kind-of to find minimum amount of fuel to make 1 trillion ORE
high = 10000000
low = 1
mid = (high + low) // 2
while low < high:
    if fuelsearch(mid) > 1000000000000:
        high = mid - 1
    else:
        low = mid
    mid = (high + low) // 2
print(low)



