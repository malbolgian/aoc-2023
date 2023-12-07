def parse_input(input_path: str) -> list[dict[str, int]]:
    with open(input_path, 'r') as f:
        games = f.read().strip().split('\n')
        capacities = []
        for g in games:
            rounds = g.split(': ')[1]
            rounds = rounds.replace(';', ',')
            cap = {'red': 0, 'green': 0, 'blue': 0}
            for cubes in rounds.split(', '):
                num, color = cubes.split(' ')
                cap[color] = max(cap[color], int(num))
            capacities.append(cap)
        return capacities

def part1(data: list[str]) -> int:
    id_sum = 0
    for id, caps in enumerate(data):
        if caps['red'] <= 12 and caps['green'] <= 13 and caps['blue'] <= 14:
            id_sum += (id + 1)
    return id_sum

def part2(data: list[str]) -> int:
    power_sum = 0
    for caps in data:
        power_sum += (caps['red'] * caps['green'] * caps['blue'])
    return power_sum

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day02.txt')))
    print ('Part Two:', part2(parse_input('input/day02.txt')))
