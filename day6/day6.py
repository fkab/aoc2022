def read_input():
    with open("input.txt") as file:
        return file.readlines()[0]


def determine_marker(size):
    input_str = read_input()
    sliding_window = [set([s for s in input_str[i:i + size]]) for i in range(0, len(input_str)) if
                      len(input_str) - i > size - 1]

    for i, e in enumerate(sliding_window):
        if len(e) == size:
            print(i + size)
            break


def part_one():
    determine_marker(4)


def part_two():
    determine_marker(14)


if __name__ == '__main__':
    part_one()
    part_two()
