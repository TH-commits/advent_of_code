import sys


class Historian:
    def __init__(self, file: list[str]) -> None:
        self.file = file

    def clean_file(self) -> int:
        clean_list = [x.split() for x in self.file]

        for i, element in enumerate(clean_list):
            clean_list[i] = [int(x) for x in clean_list[i]]

        part1 = self.count_reports(clean_list)

        return part1

    def count_reports(self, clean_list: list[list[int]]) -> int:
        count = 0
        for list in clean_list:
            if self.increase_or_decrease(list) and self.adjacent_levels(list):
                count += 1

        return count

    def adjacent_levels(self, input_list: list[int]) -> bool:
        return all(
            abs(x - y) >= 1 and abs(x - y) <= 3
            for x, y in zip(input_list, input_list[1:])
        )

    def increase_or_decrease(self, input_list: list[int]) -> bool:
        return self.is_increase(input_list) or self.is_decrease(input_list)

    def is_increase(self, input_list: list[int]) -> bool:
        return all(x < y for x, y in zip(input_list, input_list[1:]))

    def is_decrease(self, input_list: list[int]) -> bool:
        return all(x > y for x, y in zip(input_list, input_list[1:]))


def main(filename: str) -> str:
    with open(filename) as outfile:
        file = outfile.read().splitlines()

        clean_file = Historian(file)

        answer = clean_file.clean_file()

        print(f"Part 1: {answer}")


main(sys.argv[1])
