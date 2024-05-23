def parse_input(input_path: str) -> list[tuple[str, tuple[int]]]:
    with open(input_path, 'r') as f:
        lines = f.read().strip().split('\n')
        conditions = []
        for line in lines:
            springs, groups = line.split(' ')
            groups = tuple(int(num) for num in groups.split(','))
            conditions.append((springs, groups))
        return conditions

def count_solutions(springs: str, groups: tuple[int], seen: dict[tuple[str, tuple[int]], int]) -> int:
    if (springs, groups) in seen:
        return seen[(springs, groups)]
    
    # If no groups remain, only one possibility of all springs are operational
    if len(groups) == 0:
        return 0 if '#' in springs else 1

    # If no springs remain, only possibility is no groups remain (handled above)
    if len(springs) == 0:
        return 0

    g = groups[0]
    sols = 0

    # Consider skipping the first spring if it's not broken
    if springs[0] != '#':
        sols += count_solutions(springs[1:], groups, seen)

    # Consider the first g springs as a broken group
    if len(springs) >= g and '.' not in springs[:g]:
        # Handles edge case of having exactly g springs remaining
        if len(springs) == g or springs[g] != '#':
            sols += count_solutions(springs[g + 1:], groups[1:], seen)

    # Record previously calculated states for performance
    seen[(springs, groups)] = sols
    
    return sols

def part1(data: list[tuple[str, tuple[int]]]) -> int:
    total = 0
    for (springs, groups) in data:
        total += count_solutions(springs, groups, {})
    return total

def part2(data: list[tuple[str, tuple[int]]]) -> int:
    total = 0
    for (springs, groups) in data:
        unfolded_springs = '?'.join(5 * [springs])
        unfolded_groups = 5 * groups
        total += count_solutions(unfolded_springs, unfolded_groups, {})
    return total

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day12.txt')))
    print ('Part Two:', part2(parse_input('input/day12.txt')))
