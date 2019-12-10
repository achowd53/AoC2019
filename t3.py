wire1,wire2 = open("t3.txt").read().split('\n')
wire1,wire2 = [x.split(',') for x in [wire1,wire2]]
def point(p):
    x = 0
    y = 0
    out = {}
    length = 0
    for h in p:
        ins = h[0]
        num = int(h[1:])
        for z in range(num):
            if ins == "U":
                y += 1
            if ins == "D":
                y -= 1
            if ins == "L":
                x -= 1
            if ins == "R":
                x += 1
            length += 1
            if (x,y) not in out:
                out[(x,y)] = length
    return out
wire1p = point(wire1)
wire2p = point(wire2)
both = set(wire1p.keys())&set(wire2p.keys())
out = min([wire1p[w] + wire2p[w] for w in both])
print(out)
