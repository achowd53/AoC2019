import math
t = open("t10.txt")
asteroids = [x.strip() for x in t.readlines()]
coords = []
for row in range(len(asteroids)):
    for column in range(len(asteroids[0])):
        if asteroids[row][column] == '#':
            coords += [(row,column)]
            #only looking at asteroids
def f(x,y):
    return x if y==0 else f(y, x%y)
#Euclid's Algorithm for finding greatest common factor
ans = (0,0,0)
for x in coords:
    removed = set()
    for y in coords:
        if (x[0] != y[0] or x[1] != y[1]):
            distancex = y[0]-x[0]
            distancey = y[1]-x[1]
            #slope but without the division
            factor = abs(f(distancex,distancey))
            #gotta reduce slope somehow
            removed.add((-distancex//factor,distancey//factor))
    if len(removed) > ans[0]:
        ans = (len(removed),x,removed)
ans,x,removed = ans
coordx,coordy = x
print(ans)
vaporized = [(math.atan2(x,y)-(2 * math.pi if math.atan2(x,y) > math.pi/2 else 0),(x,y)) for x,y in removed]
vaporized.sort(key = lambda vaporized:vaporized[0], reverse=True)
a,b = vaporized[199][1]
x,y = coordx - a,coordy + b
while asteroids[x][y]!='#':
    x,y = x-a,y+b
print(y*100+x)
        
    
