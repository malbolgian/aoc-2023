DIRS = {'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)}

class Grid:
    def __init__(self, grid_lines: list[str]):
        self.rows, self.cols = len(grid_lines), len(grid_lines[0])
        # Blocks are fixed location, rocks can roll when tilted
        self.blocks = set()
        self.rocks = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if grid_lines[r][c] == '#':
                    self.blocks.add((r, c))
                elif grid_lines[r][c] == 'O':
                    self.rocks.add((r, c))

    def tilt(self, d: tuple[int, int]) -> None:
        # Sorting key is a hack to ensure the closest rocks (in whichever direction
        # the grid is being tilted) are processed first since 1000 >> rows, cols
        rocks_list = sorted(self.rocks,
                            key = lambda r: -1000 * (r[0] * d[0] + r[1] * d[1]))
        for rock in rocks_list:
            # Moves the rock to the furthest possible distance in given direction
            self.rocks.remove(rock)
            while (0 <= rock[0] < self.rows) and (0 <= rock[1] < self.cols) and\
                  (rock not in self.blocks) and (rock not in self.rocks):
                rock = (rock[0] + d[0], rock[1] + d[1])
            self.rocks.add((rock[0] - d[0], rock[1] - d[1]))

    def calc_load(self) -> int:
        total = 0
        for rock in self.rocks:
            total += (self.rows - rock[0])
        return total

def parse_input(input_path: str) -> Grid:
    with open(input_path, 'r') as f:
        lines = f.read().strip().split('\n')
        return Grid(lines)

def part1(data: Grid) -> int:
    data.tilt(DIRS['N'])
    return data.calc_load()

def part2(data: Grid) -> int:
    CYCLES = 10 ** 9
    # seen maps all rock orientations to the number of cycles it took to get there
    seen = {frozenset(data.rocks): 0}

    for i in range(CYCLES):
        for d in 'NWSE':
            data.tilt(DIRS[d])
        if frozenset(data.rocks) in seen:
            cycle_start, cycle_end = seen[frozenset(data.rocks)], i + 1
            break
        seen[frozenset(data.rocks)] = i + 1

    # Once we find a loop, only run through the partial loop that would exist at
    # the end of the billion cycles
    cycle_len = cycle_end - cycle_start
    cycles_left = (CYCLES - cycle_end) % cycle_len
    for i in range(cycles_left):
        for d in 'NWSE':
            data.tilt(DIRS[d])
    return data.calc_load()

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day14.txt')))
    print ('Part Two:', part2(parse_input('input/day14.txt')))
