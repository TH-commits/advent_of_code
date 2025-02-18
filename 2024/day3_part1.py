import sys
import re


class Mul:
    def __init__(self, file: str) -> None:
        self.file = file

    def part_1(self) -> int:
        total_line = 0
        for line in self.file:
            x = re.findall(r"mul\([0-9][0-9]*\,[0-9][0-9]*\)", line)

            pairs = self.parse_number(x)

            total_line += pairs

        return total_line

    def parse_number(self, multiply_list: list[str]) -> int:
        total_line = 0
        for element in multiply_list:
            x = re.split(r"\,", element)

            y = [int(re.sub(r"(mul\()|\)*", "", element_2)) for element_2 in x]

            a, b = y

            result = a * b

            total_line += result

        return total_line


def main(filename: str) -> None:
    with open(filename) as output:
        file = output.read().splitlines()

        results = Mul(file)

        print(results.part_1())


main(sys.argv[1])
