import re

class Card:
    def __init__(self, winning: list[int], nums: list[int]):
        self.winning = winning
        self.nums = nums

    def num_matches(self) -> int:
        return sum(num in self.winning for num in self.nums)

    def num_points(self) -> int:
        matches = self.num_matches()
        if matches > 0:
            return 2 ** (matches - 1)
        return 0

def parse_input(input_path: str) -> list[Card]:
    with open(input_path, 'r') as f:
        lines = f.read().strip().split('\n')
        cards = []
        for line in lines:
            all_nums = line.split(':')[1]
            winning, nums = all_nums.split('|')
            winning = [int(num) for num in re.findall('\d+', winning)]
            nums = [int(num) for num in re.findall('\d+', nums)]
            cards.append(Card(winning, nums))
        return cards

def part1(data: list[Card]) -> int:
    score = 0
    for card in data:
        score += card.num_points()
    return score

def part2(data: list[Card]) -> int:
    num_cards = [1 for card in data]
    for i in range(len(data)):
        for j in range(data[i].num_matches()):
            num_cards[i + j + 1] += num_cards[i]
    return sum(num_cards)

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day04.txt')))
    print ('Part Two:', part2(parse_input('input/day04.txt')))
