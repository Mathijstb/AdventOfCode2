from pathlib import Path


def from_str(s):
    return s.split('\n')


def from_file(f_in):
    base_path = Path(__file__).parent
    file_path = (base_path / f_in).resolve()
    with open(file_path, 'r') as file:
        array = [line.strip('\n') for line in file.readlines()]
        return array if len(array) > 1 else array[0]


def split(data, sep=''):
    groups = []
    current_group = []
    for x in data:
        if x == sep:
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(x)
    groups.append(current_group)

    return groups
