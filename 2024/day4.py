import sys


class Search:
    def __init__(self, file: str):
        self.file = file
        self.rows = len(self.file)
        self.cols = len(self.file[0])
        self.directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        self.diagonal = [(1, 1), (-1, -1)]
        self.antidiagonal = [(1, -1), (-1, 1)]
        self.word = word_input

    def result(self) -> int:
        part_1 = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if self.file[i][j] == self.word[0]:
                    for coorX, coorY in self.directions:
                        if self.dfs(coorX, coorY, 0, i, j):
                            part_1 += 1

        return part_1

    def result_part2(self) -> int:
        result = []
        seen = []
        duplicates = []

        for i in range(self.rows):
            for j in range(self.cols):
                if self.file[i][j] == self.word[0]:
                    for coorX, coorY in self.diagonal:
                        if self.dfs(coorX, coorY, 0, i, j):
                            result.append(self.a_list(coorX, coorY, i, j))
                    for coorX, coorY in self.antidiagonal:
                        if self.dfs(coorX, coorY, 0, i, j):
                            result.append(self.a_list(coorX, coorY, i, j))

        for item in result:
            if item in seen:
                duplicates.append(item)
            else:
                seen.append(item)

        return len(duplicates)

    def a_list(self, coorX: int, coorY: int, x: int, y: int) -> dict[str:int]:
        res = {}
        key = self.file[x + coorX][y + coorY]
        values = (
            x + coorX,
            y + coorY,
        )

        if key in res:
            res[key].extend(values)

        else:
            res[key] = values

        return res

    def dfs(self, coorX: int, coorY: int, index: int, x: int, y: int) -> bool:
        if index == len(self.word):
            return True

        if self.out_of_bounds(x, y) and self.file[x][y] == self.word[index]:
            return self.dfs(coorX, coorY, index + 1, x + coorX, y + coorY)

    def out_of_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.cols


def file_set_up(file: list[str]) -> list[list[str]]:
    xmas_list = []
    for word in file:
        list_of_letter = [letter for letter in word]
        xmas_list.append(list_of_letter)

    return xmas_list


def main(filename: str) -> None:
    with open(filename) as output:
        file = output.read().splitlines()

        file_upgrade = file_set_up(file)

        result = Search(file_upgrade)

        print(f"Part 1: {result.result()}")

        print(f"Part 2: {result.result_part2()}")


word_input = input("Please enter a string: ")


main(sys.argv[1])
