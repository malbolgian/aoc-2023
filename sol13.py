def parse_input(input_path: str) -> list[list[str]]:
    with open(input_path, 'r') as f:
        grids = f.read().strip().split('\n\n')
        grids = [g.split('\n') for g in grids]
        return grids

# Finds the row number of a mirror if one exists, otherwise returns 0
# mistakes is 0 if Part 1, 1 if Part 2
def find_row_mirror(grid: list[str], mistakes: int) -> int:
    # Calculates total different characters of two strings equal in length
    diff = lambda s1, s2: sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
    rows, cols = len(grid), len(grid[0])
    for mir in range(1, rows):
        to_check = min(mir, rows - mir)
        total_diff = 0
        for i in range(to_check):
            total_diff += diff(grid[mir - 1 - i], grid[mir + i])
        if total_diff == mistakes:
            return mir
    return 0

# Finds the mirror number of a grid by checking for a row mirror and transposing
# the grid to check for a column mirror if it didn't exist
# mistakes is 0 if Part 1, 1 if Part 2
def find_mirror_number(grid: list[str], mistakes: int) -> int:
    num = find_row_mirror(grid, mistakes)
    if num:
        return 100 * num
    # Transposes the grid
    grid_t = [[row[i] for row in grid] for i in range(len(grid[0]))]
    return find_row_mirror(grid_t, mistakes)

def part1(data: list[list[str]]) -> int:
    total = 0
    for grid in data:
        total += find_mirror_number(grid, 0)
    return total

def part2(data: list[list[str]]) -> int:
    total = 0
    for grid in data:
        # Smudge indicates a total difference of 1 across the mirror
        total += find_mirror_number(grid, 1)
    return total

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day13.txt')))
    print ('Part Two:', part2(parse_input('input/day13.txt')))
