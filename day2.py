"""--- Day 2: Rock Paper Scissors ---"""


def get_data(input_data):
    with open(input_data, "r", encoding="utf8") as data:
        return data.readlines()


"""
A, X = Rock 1
B, Y = Paper 2
C, Z = Scissors 3
"""


def part1(data):
    score = 0
    # get base score
    for line in data:
        if line[2] == "X":
            score += 1
        if line[2] == "Y":
            score += 2
        if line[2] == "Z":
            score += 3
    for line in data:
        # rock
        if line[0] == "A" and line[2] == "X":
            # draw
            score += 3
        if line[0] == "B" and line[2] == "X":
            # lose
            score += 0
        if line[0] == "C" and line[2] == "X":
            # win
            score += 6
        # paper
        if line[0] == "B" and line[2] == "Y":
            # draw
            score += 3
        if line[0] == "C" and line[2] == "Y":
            # lose
            score += 0
        if line[0] == "A" and line[2] == "Y":
            # win
            score += 6
        # scissors
        if line[0] == "C" and line[2] == "Z":
            # draw
            score += 3
        if line[0] == "A" and line[2] == "Z":
            # lose
            score += 0
        if line[0] == "B" and line[2] == "Z":
            # win
            score += 6
    return score


def part2(data):
    score = 0
    for line in data:
        # rock
        if line[0] == "A" and line[2] == "X":
            # lose
            score += 0 + 3
        if line[0] == "A" and line[2] == "Y":
            # draw
            score += 3 + 1
        if line[0] == "A" and line[2] == "Z":
            # win
            score += 6 + 2
        # paper
        if line[0] == "B" and line[2] == "X":
            # lose
            score += 0 + 1
        if line[0] == "B" and line[2] == "Y":
            # draw
            score += 3 + 2
        if line[0] == "B" and line[2] == "Z":
            # win
            score += 6 + 3
        # scissors
        if line[0] == "C" and line[2] == "X":
            # lose
            score += 0 + 2
        if line[0] == "C" and line[2] == "Y":
            # draw
            score += 3 + 3
        if line[0] == "C" and line[2] == "Z":
            # win
            score += 6 + 1
    return score


print(part1(get_data(".\\input_data\\2.txt")))
print(part2(get_data(".\\input_data\\2.txt")))
