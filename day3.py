"""--- Day 3: Rucksack Reorganization ---"""


def get_data(input_data):
    with open(input_data, "r", encoding="utf8") as data:
        return data.readlines()


def part1(data):
    rucksack = {}
    for line in data:
        list1 = []
        for i in range(0, len(line), len(line)//2 ):
            list1.append(line[i:i+len(line)//2])
        print(list1)
            


def part2(data):
    print("todo")


print(part1(get_data(".\\input_data\\3.txt")))
# print(part2(get_data(".\\input_data\\3.txt")))
