"""--- Day 1: Calorie Counting Part One ---"""


def get_data(input_data):
    with open(input_data, "r", encoding="utf8") as data:
        return data.readlines()


def solve(data):
    list1 = []
    for line in data:
        list1.append(line.strip())

    list2 = []
    for elf in ("\n".join(list1)).split("\n\n"):
        q = 0
        for x in elf.split("\n"):
            q += int(x)
        list2.append(q)
    list2 = sorted(list2)
    print(list2[-1])
    print(list2[-1] + list2[-2] + list2[-3])


solve(get_data(".\\input_data\\1.txt"))
