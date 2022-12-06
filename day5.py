def get_data(input_data):
    with open(input_data, "r", encoding="utf8") as data:
        return data.read().split("\n")


def part1():
    stacks = []
    for line in get_data(".\\input_data\\5.txt"):
        if line.strip():
            if line.startswith("move"):
                move = [int(x) for x in line.split() if x.isdigit()]
                crates = stacks[move[1]-1][:move[0]]
                for crate in crates:
                    stacks[move[1]-1].remove(crate)
                    stacks[move[2]-1].insert(0, crate)
            else:
                for i in range(1, len(line), 4):
                    try:
                        stacks[(i-1)//4]
                    except IndexError:
                        stacks.append([])    
                    if line[i].isupper():
                        stacks[(i-1)//4].append(line[i])

    for stack in stacks:
        print(stack[0])
def part2():
    stacks = []

    for line in get_data(".\\input_data\\5.txt"):
        if line.strip():
            if line.startswith("move"):
                move = [int(x) for x in line.split() if x.isdigit()]
                crates = stacks[move[1]-1][:move[0]]
                for crate in crates:
                    stacks[move[1]-1].remove(crate)
                crates.extend(stacks[move[2]-1])
                stacks[move[2]-1] = crates
            else:
                for i in range(1, len(line), 4):
                    try:
                        stacks[(i-1)//4]
                    except IndexError:
                        stacks.append([])    
                    if line[i].isupper():
                        stacks[(i-1)//4].append(line[i])

    for stack in stacks:
        print(stack[0])


part1()
print("---")
part2()