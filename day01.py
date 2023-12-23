# Part 1
from operator import itemgetter
import re


with open("data/day01.txt") as infile:
    sum = 0
    for line in infile:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)

        sum = sum + int(digits[0]) * 10 + int(digits[-1])

    print(f"part 1: {sum}")

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# Part 2
with open("data/day01.txt") as infile:
    sum = 0
    for line in infile:
        digits = []
        for idx, char in enumerate(line):
            if char.isdigit():
                digits.append((int(char), idx))

        for number_str, _ in numbers.items():
            find_idxs = [
                (numbers[number_str], match.start())
                for match in re.finditer(number_str, line)
            ]
            digits.extend(find_idxs)

        digits.sort(key=itemgetter(1))

        sum = sum + int(digits[0][0]) * 10 + int(digits[-1][0])

    print(f"part 2: {sum}")
