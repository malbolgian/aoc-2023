from collections import Counter

def parse_input(input_path: str) -> list[tuple[str, int]]:
    with open(input_path, 'r') as f:
        lines = f.read().strip().split('\n')
        return [(hand.split()[0], int(hand.split()[1])) for hand in lines]

# Assigns a score from 0-6 to a given hand
def score_hand(hand: str, jokers = False) -> int:
    COUNTS = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
    # Remove jokers for now to not count towards frequencies
    if jokers:
        hand = hand.replace('J', '')
    cards = sorted(list(Counter(hand).values()))
    # Jokers should always be used as the most frequent card when scoring
    if jokers:
        # Handles 5 jokers case
        if not cards:
            cards = [0]
        cards[-1] += (5 - sum(cards))
    return COUNTS.index(cards)

# Translates each hand into sortable lists (handling face cards)
def translate_hand(hand: str, jokers = False) -> list[int]:
    strengths = 'J23456789TQKA' if jokers else '23456789TJQKA'
    return [strengths.index(card) for card in hand]

def part1(data: list[tuple[str, int]]) -> int:
    hands = []
    for hand, bid in data:
        # Prioritize by score then individual cards for sorting, bid is last element
        processed_hand = [score_hand(hand)] + translate_hand(hand) + [bid]
        hands.append(processed_hand)
    hands.sort()

    total = 0
    for rank, hand in enumerate(hands):
        total += (rank + 1) * hand[-1]    
    return total

def part2(data: list[tuple[str, int]]) -> int:
    hands = []
    for hand, bid in data:
        processed_hand = [score_hand(hand, jokers = True)] + translate_hand(hand, jokers = True) + [bid]
        hands.append(processed_hand)
    hands.sort()

    total = 0
    for rank, hand in enumerate(hands):
        total += (rank + 1) * hand[-1]
    return total

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day07.txt')))
    print ('Part Two:', part2(parse_input('input/day07.txt')))
