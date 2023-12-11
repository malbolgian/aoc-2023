import itertools

def parse_input(input_path: str) -> tuple[dict[tuple[int, int], str], dict[tuple[int, int], str]]:
    with open(input_path, 'r') as f:
        lines = f.read().split('\n')
        parts = dict()
        digits = dict()

        for row in range(len(lines)):
            line = lines[row]
            for col in range(len(line)):
                if lines[row][col].isdigit():
                    digits[(row, col)] = lines[row][col]
                elif lines[row][col] != '.':
                    parts[(row, col)] = lines[row][col]
        return parts, digits

def part1(data: tuple[dict[tuple[int, int], str], dict[tuple[int, int], str]]) -> int:
    parts, digits = data
    total = 0
    
    for (part_row, part_col) in parts:
        for (shift_row, shift_col) in itertools.product([-1, 0, 1], [-1, 0, 1]):
            check_row = part_row + shift_row
            check_col = part_col + shift_col
            if (check_row, check_col) not in digits:
                continue
            while (check_row, check_col - 1) in digits:
                check_col -= 1
            num = ''
            while (check_row, check_col) in digits:
                num += digits.pop((check_row, check_col))
                check_col += 1
            total += int(num)
    return total

def part2(data: tuple[dict[tuple[int, int], str], dict[tuple[int, int], str]]) -> int:
    parts, digits = data
    total = 0

    gears = [pos for (pos, part) in parts.items() if part == '*']
    for (gear_row, gear_col) in gears:
        visited = set()
        num_list = []
        for (shift_row, shift_col) in itertools.product([-1, 0, 1], [-1, 0, 1]):
            check_row = gear_row + shift_row
            check_col = gear_col + shift_col
            if (check_row, check_col) not in digits or (check_row, check_col) in visited:
                continue
            while (check_row, check_col - 1) in digits:
                check_col -= 1
            num = ''
            while (check_row, check_col) in digits:
                num += digits[(check_row, check_col)]
                visited.add((check_row, check_col))
                check_col += 1
            num_list.append(int(num))
        if len(num_list) == 2:
            total += (num_list[0] * num_list[1])
    return total

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day03.txt')))
    print ('Part Two:', part2(parse_input('input/day03.txt')))
