import sys


class Operator:
    def __init__(self, file: list[str]):
        self.file = file
        self.add = "+"
        self.multiply = "*"

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

        for key, value_list in self.clean_file().items():
            if self.calculate(value_list, key):
                part1 += key

        return part1

    def calculate(self, value_list: list[int], key: int) -> bool:
        res = 1
        for value in value_list:
            res = res * value
            if key == res:
                return True


def main(filename: str) -> None:
    with open(filename) as file:
        result = file.read().splitlines()

        part1 = Operator(result)

        print(part1.part_1())

        # print(part1.clean_file())


main(sys.argv[1])
