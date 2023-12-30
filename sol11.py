import itertools

def parse_input(input_path: str) -> tuple[list[tuple[int, int]], list[int], list[int]]:
    with open(input_path, 'r') as f:
        grid = f.read().strip().split('\n')
        rows, cols = len(grid), len(grid[0])
        star_rows = set()
        star_cols = set()
        stars = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '#':
                    star_rows.add(r)
                    star_cols.add(c)
                    stars.append((r, c))
        empty_rows = [r for r in range(rows) if r not in star_rows]
        empty_cols = [c for c in range(cols) if c not in star_cols]
        return stars, empty_rows, empty_cols

# Given 1-dimensional coordinates, expanding indices, and expansion factor,
# returns the post-expansion distance along that axis.
def distance_1d(coord1: int, coord2: int, expanding: list[int], factor: int) -> int:
    coord1, coord2 = min(coord1, coord2), max(coord1, coord2)
    return (coord2 - coord1) + factor * (sum(coord1 < n < coord2 for n in expanding))

def part1(data: tuple[list[tuple[int, int]], list[int], list[int]]) -> int:
    EXPANSION_FACTOR = 1
    stars, empty_rows, empty_cols = data
    total = 0
    for star1, star2 in itertools.combinations(stars, 2):
        total += distance_1d(star1[0], star2[0], empty_rows, EXPANSION_FACTOR)
        total += distance_1d(star1[1], star2[1], empty_cols, EXPANSION_FACTOR)
    return total

def part2(data: tuple[list[tuple[int, int]], list[int], list[int]]) -> int:
    EXPANSION_FACTOR = 10 ** 6 - 1
    stars, empty_rows, empty_cols = data
    total = 0
    for star1, star2 in itertools.combinations(stars, 2):
        total += distance_1d(star1[0], star2[0], empty_rows, EXPANSION_FACTOR)
        total += distance_1d(star1[1], star2[1], empty_cols, EXPANSION_FACTOR)
    return total

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day11.txt')))
    print ('Part Two:', part2(parse_input('input/day11.txt')))
