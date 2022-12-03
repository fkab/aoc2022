def read_input():
    inputs = []
    with open("input.txt") as file:
        sublist = []
        for line in file:
            if not line.strip():
                inputs.append(sublist)
                sublist = []
            else:
                sublist.append(int(line))
    return inputs


if __name__ == '__main__':
    # part 1
    print(max([sum(sublist) for sublist in read_input()]))

    # part 2
    print(sum(sorted([sum(sublist) for sublist in read_input()])[-3:]))
