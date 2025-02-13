import sys


class Historian:
    def __init__(self, file: list[str]) -> None:
        self.file = file

    def answer(self) -> int:
        clean_list = [x.split() for x in self.file]

        for i, element in enumerate(clean_list):
            clean_list[i] = [int(x) for x in clean_list[i]]

        part1 = self.part_1(clean_list)

        part2 = self.part_2(clean_list)

        return part1, part2

    def part_1(self, clean_list: list[list[int]]) -> int:
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

    def part_2(self, input_list: list[int]) -> int:
        count = 0
        for level in input_list:
            if self.increase_or_decrease(level) and self.adjacent_levels(level):
                count += 1

            else:
                if self.case_check(level):
                    count += 1

        return count

    def case_check(self, level: list[(int, int)]) -> bool:
        for i in range(len(level)):
            modified_report = [x for j, x in enumerate(level) if j != i]

            if self.increase_or_decrease(modified_report) and self.adjacent_levels(
                modified_report
            ):
                return True

        return False


def main(filename: str) -> str:
    with open(filename) as outfile:
        file = outfile.read().splitlines()

        results = Historian(file)

        part1, part2 = results.answer()

        print(f"Part 1: {part1}")

        print(f"Part 2: {part2}")


main(sys.argv[1])
