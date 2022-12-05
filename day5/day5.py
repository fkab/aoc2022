import re


def read_input():
    with open("input.txt") as file:
        stacks = parse_stacks(file)
        instructions = parse_instructions(file)

        for stack in stacks:
            stack.reverse()

    return stacks, instructions


def crate_mover9000(amount, from_stack, to_stack):
    for i in range(amount):
        to_stack.append(from_stack.pop())


def crate_mover9001(amount, from_stack, to_stack):
    temp_stack = []
    for i in range(amount):
        temp_stack.append(from_stack.pop())

    temp_stack.reverse()
    to_stack.extend(temp_stack)


def parse_instructions(file):
    return [re.sub(r'[^0-9 ]', '', x).lstrip().split() for x in file.readlines()]


def parse_stacks(file):
    raw_stack_info = []

    for line in file:
        if line.strip():
            raw_stack_info.append([re.sub(r'\W+', '', line[i:i + 4]) for i in range(0, len(line), 4)])
        else:
            break

    for raw_line in raw_stack_info:
        while len(raw_line) != len(raw_stack_info[-1]):
            raw_line.append('')

    return [[e for e in s if e != ''] for s in map(list, zip(*raw_stack_info[0:-1]))]


def part_one():
    stacks, instructions = read_input()
    for instruction in instructions:
        crate_mover9000(int(instruction[0]), stacks[int(instruction[1]) - 1], stacks[int(instruction[2]) - 1])

    print(''.join([stack[-1] for stack in stacks]))


def part_two():
    stacks, instructions = read_input()
    for instruction in instructions:
        crate_mover9001(int(instruction[0]), stacks[int(instruction[1]) - 1], stacks[int(instruction[2]) - 1])

    print(''.join([stack[-1] for stack in stacks]))


if __name__ == '__main__':
    part_one()
    part_two()
