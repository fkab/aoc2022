def read_input():
    inputs = []
    with open("input.txt") as file:
        for line in file:
            pair = [set(range(int(x.split('-')[0]), int(x.split('-')[1]) + 1)) for x in line.split(',')]
            inputs.append(pair)
    return inputs


def contains_subset(setx, sety):
    return set.issubset(setx, sety) or set.issubset(sety, setx)


def intersects(setx, sety):
    return len(set.intersection(setx, sety)) > 0


def part_one():
    print([contains_subset(x[0], x[1]) for x in read_input()].count(True))


def part_two():
    print([intersects(x[0], x[1]) for x in read_input()].count(True))


if __name__ == '__main__':
    part_one()
    part_two()
