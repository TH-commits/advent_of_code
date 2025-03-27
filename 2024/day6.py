import sys


class Guard:
    def __init__(self, file) -> None:
        self.file = file
        self.rows = len(file)
        self.cols = len(self.file[0])
        self.char = "^"
        self.block = "#"
        self.period = "."
        self._start = self.guard_position()
        self._path = set()

    def guard_position(self) -> tuple[int, int]:
        for i, row in enumerate(self.file):
            for j, c in enumerate(row):
                if c == self.char:
                    return (i, j)
        raise Exception("Oops")

    def result(self) -> tuple[int, int]:
        part_2 = 0

        part_1 = self.guard_check(*self._start)
        grid = [[c for c in row] for row in self.file]

        for i, j in self._path:
            if (i, j) == self._start:
                continue
            # place block
            grid[i][j] = self.block
            if self.loop_check(grid, *self._start):
                part_2 += 1
            # remove block
            grid[i][j] = self.period
        return part_1, part_2

    def guard_check(self, x: int, y: int) -> int:
        dx, dy = -1, 0

        while True:
            self._path.add((x, y))
            if not self.in_bounds(x + dx, y + dy):
                break
            if self.file[x + dx][y + dy] == self.block:
                dx, dy = dy, -dx
            else:
                x += dx
                y += dy

        return len(self._path)

    def loop_check(self, grid: list[list[str]], x: int, y: int) -> bool:
        dx, dy = -1, 0
        visited = set()

        while True:
            if (x, y, dx, dy) in visited:
                return True
            visited.add((x, y, dx, dy))
            if not self.in_bounds(x + dx, y + dy):
                return False
            if grid[x + dx][y + dy] == self.block:
                dx, dy = dy, -dx
            else:
                x += dx
                y += dy

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.cols


def file_clean(file: list[str]) -> list[list[str]]:
    return [list(row) for row in file]


def main(filename: str) -> None:
    with open(filename) as output:
        file = output.read().splitlines()

        new_file = file_clean(file)

        result = Guard(new_file)

        part1, part2 = result.result()

        print(f"Part 1: {part1}")

        print(f"Part 2: {part2}")


main(sys.argv[1])
