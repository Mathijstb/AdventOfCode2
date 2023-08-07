import os
from unittest import TestCase

from parameterized import parameterized

import datareader


class Day3:

    def __init__(self, input_data):
        self.data = input_data

    def solve1(self):
        return self.data

    def solve2(self):
        return self.data


if __name__ == "__main__":
    file = os.path.join('../2017/data/input3.csv')
    data = datareader.from_file(file)
    P = Day3(data)
    print(P.solve1())
    print(P.solve2())


class Test(TestCase):
    @parameterized.expand([
        ["0", "0"],
    ])
    def test_part_1(self, sample, expected):
        p = Day3(datareader.from_str(sample))
        assert p.solve1() == expected

    @parameterized.expand([
        ["0", "0"],
    ])
    def test_part_2(self, sample, expected):
        p = Day3(datareader.from_str(sample))
        assert p.solve2() == expected
