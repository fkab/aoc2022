from math import prod


def read_input():
    with open("input.txt") as file:
        matrix = [[int(y) for y in x.strip()] for x in file.readlines()]
    return matrix


def column(matrix, j):
    return [r[j] for r in matrix]


def row(matrix, i):
    return matrix[i]


def scenic_score(direction):
    score = 0
    cur_element = direction[0]

    for e in direction[1:]:
        score += 1
        if cur_element <= e:
            return score

    return score


def is_tree_visible(height, trees):
    return max(trees) == height and trees.count(height) == 1


def part_one():
    trees = read_input()
    counter = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            if i == 0 or j == 0 or i == len(trees) - 1 or j == len(trees[0]) - 1:
                counter += 1
            else:
                up = column(trees, j)[0:i + 1]
                down = column(trees, j)[i:len(trees)]
                left = row(trees, i)[0:j + 1]
                right = row(trees, i)[j:len(trees[0])]

                if is_tree_visible(trees[i][j], up) or is_tree_visible(trees[i][j], down) or is_tree_visible(
                        trees[i][j], left) or is_tree_visible(trees[i][j], right):
                    counter += 1

    print(counter)


def part_two():
    trees = read_input()
    scenic_scores = []
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            if i == 0 or j == 0 or i == len(trees) - 1 or j == len(trees[0]) - 1:
                continue
            else:

                up = column(trees, j)[0:i + 1]
                up.reverse()
                down = column(trees, j)[i:len(trees)]
                left = row(trees, i)[0:j + 1]
                left.reverse()
                right = row(trees, i)[j:len(trees[0])]

                scenic_scores.append(prod(list(map(scenic_score, [up, down, left, right]))))

    print(max(scenic_scores))


if __name__ == '__main__':
    part_one()
    part_two()
