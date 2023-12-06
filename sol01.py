import re

def parse_input(input_path: str) -> list[str]:
    with open(input_path, 'r') as f:
        return f.read().strip().split('\n')

def part1(data: list[str]) -> int:
    value_sum = 0
    for line in data:
        digits = re.findall('\d', line)
        value_sum += int(digits[0] + digits[-1])
    return value_sum

def part2(data: list[str]) -> int:
    # First and last characters are reserved due to edge cases -
    # e.g. oneight -> o1e8t rather than 1ight
    # Would need adjusting if digits shared more than one character or if a
    # digit has the same beginning and ending character, but not the case.
    TRANS = {'one': 'o1e',
             'two': 't2o',
             'three': 't3e',
             'four': 'f4r',
             'five': 'f5e',
             'six': 's6x',
             'seven': 's7n',
             'eight': 'e8t',
             'nine': 'n9e'}
    value_sum = 0
    for line in data:
        for num in TRANS:
            line = line.replace(num, TRANS[num])
        digits = re.findall('\d', line)
        value_sum += int(digits[0] + digits[-1])
    return value_sum

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day01.txt')))
    print ('Part Two:', part2(parse_input('input/day01.txt')))
