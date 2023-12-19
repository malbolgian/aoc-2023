import re

EPS = 1e-10 # Used to handle edge case for integral roots

def parse_input(input_path: str) -> list[tuple[int, int]]:
    with open(input_path, 'r') as f:
        lines = f.read().split('\n')
        times = [int(num) for num in re.findall('\d+', lines[0])]
        dists = [int(num) for num in re.findall('\d+', lines[1])]        
        return list(zip(times, dists))

def part1(data: list[tuple[int, int]]) -> int:
    # Solving quadratic x * (t - x) > d
    combos = 1
    for time, dist in data:
        lo = (time - (time ** 2 - 4 * dist) ** 0.5) / 2 + EPS
        hi = (time + (time ** 2 - 4 * dist) ** 0.5) / 2 - EPS
        combos *= (int(hi) - int(lo))
    return combos

def part2(data: list[tuple[int, int]]) -> int:
    time = int(''.join(str(tup[0]) for tup in data))
    dist = int(''.join(str(tup[1]) for tup in data))
    lo = (time - (time ** 2 - 4 * dist) ** 0.5) / 2 + EPS
    hi = (time + (time ** 2 - 4 * dist) ** 0.5) / 2 - EPS
    return int(hi) - int(lo)

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day06.txt')))
    print ('Part Two:', part2(parse_input('input/day06.txt')))
