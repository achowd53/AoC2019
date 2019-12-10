def part1():
    orbits = {}
    for line in open("t6.txt").readlines():
        a,b = line.strip().split(")")
        if a in orbits:
            orbits[a].append(b)
        else:
            orbits[a] = [b]
    def orbitcount(check):
        count = 1
        if check in orbits:
            for x in orbits[check]:
                count += orbitcount(x)
        return count
    count = 0
    for direct in orbits:
        for indirect in orbits[direct]:
            count += orbitcount(indirect)
    print(count)
def part2():
    orbits = {}
    for line in open("t6.txt").readlines():
        a,b = line.strip().split(")")
        if a in orbits:
            orbits[a].append(b)
        else:
            orbits[a] = [b]
        if b in orbits:
            orbits[b].append(a)
        else:
            orbits[b] = [a]
    #Orbits is just a dictionary of all possible orbits you can jump to from one of them
    def orbitcount(check,nope):
        #nope is the list of visited orbits within the path, check is the current orbit
        count = 1
        #1 step every orbit
        found = False
        #when found is true it means the path to SAN was found
        if check in orbits['SAN']:
            found = True
            return count,found
        if check in orbits:
            for x in orbits[check]:
                #SAN not around current orbit so go to this orbit's orbits to look further
                if x in nope:
                    pass
                else:
                    #not in nope means new path to seach for SAN being made
                    add,found = orbitcount(x,nope+[x])
                    if found == True:
                        #If the path to SAN was found, add up the total steps in the path + 1 extra
                        count += add
                        break
                
        return count,found
    count = []
    for indirect in orbits['YOU']:
        add,found = orbitcount(indirect,[indirect])
        if not found:
            add = 1000
            #Just here to guarantee that a random wrong number wont appear if SAN wasn't found
        count += [add-1]
    print(min(count))
part1()
part2()
