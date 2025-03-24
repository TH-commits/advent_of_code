import sys


class Guard:
    def __init__(self, file) -> None:
        self.file = file
        self.rows = len(file)
        self.cols = len(self.file[0])
        self.char = "^"
        self.block = "#"
        self.period = "."

    def result(self) -> int:
        for i in range(self.rows):
            for j in range(self.cols):
                if self.file[i][j] == self.char:
                    return self.guard_check(i, j)
        return 0

    def guard_check(self, x: int, y: int) -> int:
        dx, dy = -1, 0
        visited = set()

        while True:
            visited.add((x, y))
            if not self.in_bounds(x + dx, y + dy):
                break
            if self.file[x + dx][y + dy] == self.block:
                dx, dy = dy, -dx
            else:
                x += dx
                y += dy

        return len(visited)

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.cols


def file_clean(file: list[str]) -> list[list[str]]:
    return [list(row) for row in file]


def main(filename: str) -> None:
    with open(filename) as output:
        file = output.read().splitlines()

        new_file = file_clean(file)

        result = Guard(new_file)

        print(f"Part 1: {result.result()}")


main(sys.argv[1])
