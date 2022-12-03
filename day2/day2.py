def read_input():
    inputs = []
    with open("input.txt") as file:
        for line in file:
            inputs.append(line.strip())
    return inputs


def part_one():
    results = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
    }

    print(sum([results.get(x) for x in read_input()]))


def part_two():
    results = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }

    print(sum([results.get(x) for x in read_input()]))


if __name__ == '__main__':
    part_one()
    part_two()
