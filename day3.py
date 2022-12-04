import string


def get_data(input_data):
    with open(input_data, "r", encoding="utf8") as data:
        return data.read().split("\n")


def part1():
    alphabet = list(string.ascii_lowercase)

    upperAlphabet = list(string.ascii_uppercase)

    rucksackSum = 0

    for items in get_data(".\\input_data\\3.txt"):
        if items != "":
            firstContainer = slice(0, len(items) // 2)
            secondContainer = slice(len(items) // 2, len(items))
            for letter in list(items[firstContainer]):
                if letter in items[secondContainer]:
                    if letter not in alphabet:
                        rucksackSum += upperAlphabet.index(letter) + 27
                        break
                    else:
                        rucksackSum += alphabet.index(letter) + 1
                        break

    return rucksackSum


def part2():
    alphabet = list(string.ascii_lowercase)

    upperAlphabet = list(string.ascii_uppercase)
    rucksackSum = 0

    line = 0

    itemList = []

    for items in get_data(".\\input_data\\3.txt"):
        if items != "" and line == 2:
            line = 0
            itemList.append(items)
            for letter in itemList[0]:
                if letter in itemList[1] and letter in itemList[2]:
                    if letter not in alphabet:
                        rucksackSum += upperAlphabet.index(letter) + 27
                        break
                    else:
                        rucksackSum += alphabet.index(letter) + 1
                        break
            itemList = []
        else:
            itemList.append(items)
            line += 1

    return rucksackSum


print(part1())
print(part2())
