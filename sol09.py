def parse_input(input_path: str) -> list[list[int]]:
    with open(input_path, 'r') as f:
        lines = f.read().strip().split('\n')
        return [[int(i) for i in seq.split(' ')] for seq in lines]

# Handles prediction through recursion, base case of constant sequence
def predict(seq: list[int]) -> int:
    constant = True
    for elem in seq:
        if elem != seq[0]:
            constant = False
    if constant:
        return seq[0]

    diff = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
    return seq[-1] + predict(diff)

def part1(data: list[list[int]]) -> int:
    total = 0
    for seq in data:
        total += predict(seq)
    return total

def part2(data: list[list[int]]) -> int:
    total = 0
    for seq in data:
        # Backwards extrapolation equivalent to extrapolating sequence in reverse
        total += predict(seq[::-1])
    return total

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day09.txt')))
    print ('Part Two:', part2(parse_input('input/day09.txt')))
