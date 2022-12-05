def get_data(input_data):
    with open(input_data, "r", encoding="utf8") as data:
        return data.read().split("\n")


def part1():

    fullpairs = 0

    for line in get_data(".\\input_data\\4.txt"):
        if line != "":
            A = line.replace(",", "-").split("-")
            x1,x2,y1,y2 = int(A[0]),int(A[1]),int(A[2]),int(A[3])
            if x1 <= y1 and y2 <= x2 or y1 <= x1 and x2 <= y2:
                fullpairs += 1
    return fullpairs


def part2():

    fullpairs = 0

    for line in get_data(".\\input_data\\4.txt"):
        if line != "":
            A = line.replace(",", "-").split("-")
            x1,x2,y1,y2 = int(A[0]),int(A[1]),int(A[2]),int(A[3])
            if not (x2 < y1 or x1 > y2):
                fullpairs += 1
    return fullpairs


print(part1())
print(part2())
