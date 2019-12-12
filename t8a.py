
def part1():
    #
    inp = [int(x) for x in open("input.txt").read()]
    image = [[inp[y*150+x] for x in range(25*6)] for y in range(10)]
    fewy = [image[x].count(0) for x in range(10)].index(min([image[x].count(0) for x in range(10)]))
    ones = image[fewy].count(1)
    twos = image[fewy].count(2)
    print(ones*twos)
def part2():
    print("Accidentally deleted part 2, too lazy to recode :p")

part1()
part2()