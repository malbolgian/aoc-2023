import re
from math import lcm

def parse_input(input_path: str) -> tuple[str, dict[str, dict[str, str]]]:
    with open(input_path, 'r') as f:
        seq, node_str = f.read().strip().split('\n\n')
        lines = node_str.split('\n')
        node_dict = {}
        for line in lines:
            nodes = re.findall('\w+', line)
            node_dict[nodes[0]] = {'L': nodes[1], 'R': nodes[2]}
        return (seq, node_dict)

def part1(data: tuple[str, dict[str, dict[str, str]]]) -> int:
    seq, node_dict = data
    pos = 'AAA'
    step = 0
    while pos != 'ZZZ':
        dir = seq[step % len(seq)]
        pos = node_dict[pos][dir]
        step += 1
    return step

def part2(data: tuple[str, dict[str, dict[str, str]]]) -> int:
    # Mapping out paths of relevant nodes reveals that only one node ending in
    # 'Z' is visited in a cycle and that cycle length = initial offset, so final
    # answer is just an LCM of initial path lengths to an ending node
    seq, node_dict = data
    result = 1
    for node in node_dict:
        if node[-1] != 'A':
            continue
        pos = node
        step = 0
        end_nodes = []
        while len(end_nodes) < 2:
            dir = seq[step % len(seq)]
            pos = node_dict[pos][dir]
            step += 1
            if pos[-1] == 'Z':
                end_nodes.append((pos, step))
        # Assertions of previous claims
        assert end_nodes[0][0] == end_nodes[1][0]
        assert end_nodes[1][1] == 2 * end_nodes[0][1]
        result = lcm(result, end_nodes[0][1])
    return result

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day08.txt')))
    print ('Part Two:', part2(parse_input('input/day08.txt')))
