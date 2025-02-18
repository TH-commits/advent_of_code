import sys
import re


class Mul:
    def __init__(self, file: str) -> None:
        self.file = file

    def part_2(self) -> int:
        total_line = 0

        matches = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", self.file)

        is_enabled = True
        for match in matches:
            if match == "do()":
                is_enabled = True

            elif match == "don't()":
                is_enabled = False

            elif match.startswith("mul") and is_enabled:
                a, b = self.parse_number(match)
                total_line += a * b

        return total_line

    def parse_number(self, x: str) -> int:
        numbers = re.findall(r"\d{1,3}", x)
        return int(numbers[0]), int(numbers[1])


def main(filename: str) -> None:
    with open(filename) as output:
        file = output.read()

        results = Mul(file)

        print(results.part_2())


main(sys.argv[1])
