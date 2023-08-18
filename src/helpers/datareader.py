import re
from pathlib import Path


def read_data(data):
    array = [re.split(r'\s+', line.strip()) for line in data]
    if len(array) > 1:
        return array
    else:
        list0 = array[0]
        return list0 if len(list0) > 1 else list0[0]


def read_file(f_in):
    base_path = Path(__file__).parent
    file_path = (base_path / f_in).resolve()
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        return read_data(lines)


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
