class Directory:

    def __init__(self, name):
        self.children = []
        self.parent = None
        self.size = None
        self.name = name

    def is_folder(self):
        return self.size is None

    def __str__(self):
        return self.name + ': ' + ', '.join([c.name for c in self.children])


def cd(cmd, directory):
    if cmd == '/':
        return directory

    if cmd == '..':
        return directory.parent

    return next(x for x in directory.children if x.name == cmd)


def ls(cmd, directory):
    output1 = cmd.split()[0]
    output2 = cmd.split()[1]
    if not any(d.name == output2 for d in directory.children):
        new_dir = Directory(output2)
        new_dir.parent = directory
        if output1 != 'dir':
            new_dir.size = int(output1)
        directory.children.append(new_dir)


def read_file():
    with open("input.txt") as file:
        inputs = []
        lines = file.readlines()

        for line in lines:

            if line.startswith('$ cd'):
                inputs.append(('cd', line.strip().split()[2]))
                continue

            if line.startswith('$ ls'):
                continue
            else:
                inputs.append(('ls', line.strip()))

        return inputs


def dir_structure():
    current_dir = Directory('root')
    cmds = read_file()
    for cmd in cmds:
        if cmd[0] == 'cd':
            current_dir = cd(cmd[1], current_dir)
        else:
            ls(cmd[1], current_dir)

    while current_dir.parent is not None:
        current_dir = current_dir.parent

    return current_dir


def dir_size(directory):
    if directory.is_folder() and len(directory.children) == 0:  # empty dir
        return 0

    if not directory.is_folder():
        return directory.size

    return sum([dir_size(d) for d in directory.children])


def traverse(directory, sizes):
    if not directory.is_folder():
        return

    for d in directory.children:
        if d.is_folder():
            sizes.append(dir_size(d))
            traverse(d, sizes)


def part_one():
    root = dir_structure()
    acc = []
    traverse(root, acc)
    print(sum(x for x in acc if x < 100000))


def part_two():
    root = dir_structure()
    acc = []
    traverse(root, acc)
    to_be_deleted = 30000000 - (70000000 - dir_size(root))
    print(min([x for x in acc if x > to_be_deleted]))


if __name__ == '__main__':
    part_one()
    part_two()
