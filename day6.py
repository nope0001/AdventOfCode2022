def get_data(input_data):
    with open(input_data, "r", encoding="utf8") as data:
        return data.read().strip()


def part1():
    input_str = get_data(".\\input_data\\6.txt")
    if input_str:
        for i in range(0, len(input_str)-3):
            if len(set(input_str[i:i+4])) == 4:
                    print(i+4)
                    break


def part2():
    input_str = get_data(".\\input_data\\6.txt")
    if input_str:
        for i in range(0, len(input_str)-13):
            if len(set(input_str[i:i+14])) == 14:
                    print(i+14)
                    break


part1()
part2()