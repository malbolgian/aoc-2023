from typing import Optional

PIPE_ADJ = {'|': [(-1, 0), (1, 0)],
            '-': [(0, -1), (0, 1)],
            'L': [(-1, 0), (0, 1)],
            'J': [(-1, 0), (0, -1)],
            '7': [(1, 0), (0, -1)],
            'F': [(1, 0), (0, 1)]}

def parse_input(input_path: str) -> dict[tuple[int, int], str]:
    with open(input_path, 'r') as f:
        lines = f.read().strip().split('\n')
        tiles = {}
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                if lines[row][col] != '.':
                    tiles[(row, col)] = lines[row][col]
        return tiles

# Takes in a dictionary of each pipe shape as well as a starting pipe shape.
# Returns a list of coordinates representing the loop, or None if one doesn't
# exist with the given starting pipe shape.
def find_loop(tiles: dict[tuple[int, int], str], start_pipe: str) -> Optional[list[tuple[int, int]]]:
    adj = {}
    for loc in tiles:
        if tiles[loc] == 'S':
            start_loc = loc
            pipe = start_pipe
        else:
            pipe = tiles[loc]
        dir1, dir2 = PIPE_ADJ[pipe]
        adj[loc] = [(loc[0] + dir1[0], loc[1] + dir1[1]), (loc[0] + dir2[0], loc[1] + dir2[1])]

    loop = [start_loc]
    current = adj[start_loc][0]
    while current != start_loc:
        # If pipes are not connected both ways, not a valid loop
        if (current not in adj) or (loop[-1] not in adj[current]):
            return
        loop.append(current)
        # Set the next point in loop to be the other adjacent location
        current = adj[current][1 - adj[current].index(loop[-2])]

    # If we make it to the starting pipe from the other adjacent location, the loop is valid
    if loop[-1] == adj[start_loc][1]:
        return loop
    return

def part1(data: dict[tuple[int, int], str]) -> int:
    for start_pipe in PIPE_ADJ:
        loop = find_loop(data, start_pipe)
        if loop:
            return len(loop) // 2
    # Something went wrong :(
    assert loop

def part2(data: dict[tuple[int, int], str]) -> int:
    for start_pipe in PIPE_ADJ:
        loop = find_loop(data, start_pipe)
        if loop:
            break
    assert loop

    boundary = len(loop)
    loop.append(loop[0])
    # Shoelace area formula
    area = abs(sum(loop[i][0] * loop[i + 1][1] - loop[i][1] * loop[i + 1][0] for i in range(len(loop) - 1))) // 2
    # Pick's Theorem
    return (area + 1 - boundary // 2)

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day10.txt')))
    print ('Part Two:', part2(parse_input('input/day10.txt')))
