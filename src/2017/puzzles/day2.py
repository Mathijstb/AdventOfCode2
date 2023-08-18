import os
from unittest import TestCase

from parameterized import parameterized
import itertools

from src.helpers import datareader


class Day2:

    def __init__(self, input_data):
        self.data = input_data

    def solve1(self):
        int_list = [list(map(int, x)) for x in self.data]
        return sum([max(numbers) - min(numbers) for numbers in int_list])

    def solve2(self):
        int_list = [list(map(int, x)) for x in self.data]
        result = 0
        for row in int_list:
            for (a, b) in itertools.permutations(row, 2):
                if a % b == 0:
                    result += int(a / b)
        return result


if __name__ == "__main__":
    file = os.path.join('../2017/data/input2.csv')
    data = datareader.read_file(file)
    P = Day2(data)
    print(P.solve1())
    print(P.solve2())


class Test(TestCase):
    @parameterized.expand([
        [["5 1 9 5",
          "7 5 3  ",
          "2 4 6 8"], 18]
    ])
    def test_part_1(self, sample, expected):
        p = Day2(datareader.read_data(sample))
        assert p.solve1() == expected

    @parameterized.expand([
        [["5 9 2 8",
          "9 4 7 3",
          "3 8 6 5"], 9]
    ])
    def test_part_2(self, sample, expected):
        p = Day2(datareader.read_data(sample))
        assert p.solve2() == expected
