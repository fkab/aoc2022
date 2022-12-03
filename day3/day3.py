def read_input():
    inputs = []
    with open("input.txt") as file:
        for line in file:
            inputs.append(line.strip())
    return inputs


def priority(letter):
    return ord(letter) - 38 if letter.isupper() else ord(letter) - 96


def split_into(string, slice_size):
    num_of_elements = int(len(string) / slice_size)
    return [string[i:i + num_of_elements] for i in range(0, len(string), num_of_elements)]


def group_into(flat_list, group_size):
    return [flat_list[i:i + group_size] for i in range(0, len(flat_list), group_size)]


def tokenize(string):
    return [x for i, x in enumerate(string)]


def find_intersection_of_strings(strings):
    return set.intersection(*(set(tokenize(x)) for x in strings)).pop()


def part_one():
    print(sum([priority(find_intersection_of_strings(split_into(x, 2))) for x in read_input()]))


def part_two():
    print(sum([priority(find_intersection_of_strings(y)) for y in group_into([x for x in read_input()], 3)]))


if __name__ == '__main__':
    part_one()
    part_two()
