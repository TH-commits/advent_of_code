import sys

from collections import Counter


class Historian:
    def __init__(self, file: list[str]) -> None:
        self.file = file

    def clean_file(self) -> int:
        clean_list = [x.split() for x in self.file]

        column1 = []
        column2 = []

        for line in clean_list:
            if len(line) == 2:
                column1.append(int(line[0]))
                column2.append(int(line[1]))

        part1 = self.part_1(column1, column2)

        part2 = self.part_2(column1, column2)

        return part1, part2

    def part_1(self, column1: list[int], column2: list[int]) -> int:
        part1 = 0
        for result in self.calculate_differences(column1, column2):
            part1 += result

        return part1

    def part_2(self, column1: list[int], column2: list[int]) -> int:
        part2 = 0
        for result in self.similarity(column1, column2):
            part2 += result

        return part2

    def calculate_differences(self, left_list: list[int], right_list: list[int]) -> int:
        differences = [
            abs(x - y) for x, y in zip(sorted(left_list), sorted(right_list))
        ]

        return differences

    def similarity(self, left_list: list[int], right_list: list[int]) -> int:
        counts = Counter(left_list)

        count_list = [element * counts[element] for element in right_list]

        return count_list


def main(filename: str) -> str:
    with open(filename) as outfile:
        file = outfile.read().splitlines()

        cleaned_file = Historian(file)

        part1, part2 = cleaned_file.clean_file()

        print(f"Part 1: {part1}")

        print(f"Part 2: {part2}")


main(sys.argv[1])
