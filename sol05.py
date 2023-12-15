import re

class Map:
    def __init__(self, intervals: list[list[int]]):
        self.intervals = intervals
        self.intervals.sort(key = lambda x: x[1])

    def translate(self, location: int) -> int:
        for dst, src, rng in self.intervals:
            if (src <= location < src + rng):
                return location - src + dst
        return location

    def reverse_translate(self, location: int) -> int:
        for dst, src, rng in self.intervals:
            if (dst <= location < dst + rng):
                return location - dst + src
        return location

def parse_input(input_path: str) -> tuple[list[int], list[Map]]:
    with open(input_path, 'r') as f:
        blocks = f.read().strip().split('\n\n')
        seeds = [int(num) for num in re.findall('\d+', blocks[0])]
        maps = []
        for m in blocks[1:]:
            intervals = []
            for line in m.split('\n')[1:]:
                intervals.append([int(num) for num in line.split(' ')])
            maps.append(Map(intervals))
        return seeds, maps

def part1(data: tuple[list[int], list[Map]]) -> int:
    seeds, maps = data
    min_loc = float('inf')
    for seed in seeds:
        loc = seed
        for map in maps:
            loc = map.translate(loc)
        min_loc = min(min_loc, loc)
    return min_loc

def part2(data: tuple[list[int], list[Map]]) -> int:
    # TODO: Optimize to not have to individually check final destinations
    seeds, maps = data
    min_loc = 0

    while True:
        loc = min_loc
        for map in maps[::-1]:
            loc = map.reverse_translate(loc)
        range_check = False
        for i in range(0, len(seeds), 2):
            if (seeds[i] <= loc < seeds[i] + seeds[i + 1]):
                range_check = True
        if range_check:
            break
        min_loc += 1
    return min_loc

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day05.txt')))
    print ('Part Two:', part2(parse_input('input/day05.txt')))
