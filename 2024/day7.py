import sys

import math


class Operator:
    def __init__(self, file: list[str]):
        self.file = file

    def clean_file(self) -> dict[int, list[int]]:
        equation_dict = {}
        for equation in self.file:
            ans, element = equation.split(":")

            new_element = element.strip().split(" ")

            element_int = [int(element) for element in new_element]

            new_ans = int(ans)

            equation_dict[new_ans] = element_int

        return equation_dict

    def part_1(self) -> int:
        part1 = 0

        value_list = list(self.clean_file().items())

        for key, value in value_list:
            if self.is_valid(value[0], key, value, 1):
                part1 += key

        return part1

    def is_valid(self, value: int, key: int, value_list: list[int], index: int) -> bool:
        if value == key and index == len(value_list):
            return True
        if value > key or index >= len(value_list):
            return False

        combined_value = self.combine_numbers(value, value_list[index])

        combine = self.is_valid(combined_value, key, value_list, index + 1)

        mult = self.is_valid(value * value_list[index], key, value_list, index + 1)

        add = self.is_valid(value + value_list[index], key, value_list, index + 1)

        return mult or add or combine

    def combine_numbers(self, num1: int, num2: int) -> int:
        if num2 == 0:
            multiplier = 1
        else:
            multiplier = 10 ** (int(math.log10(num2)) + 1)
        return num1 * multiplier + num2


def main(filename: str) -> None:
    with open(filename) as file:
        result = file.read().splitlines()

        part1 = Operator(result)

        print(f"Part 1/2 Solution: {part1.part_1()}")


main(sys.argv[1])
