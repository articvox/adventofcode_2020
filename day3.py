from util.reader import Read
from functools import reduce
from operator import mul


def padded(line, x):
    while len(line) <= x:
        line = line + line

    return line


def get_encounters(x: int, y: int) -> int:
    r = [line for idx, line in enumerate(range(y, len(lines), y)) if
         padded(lines[line], x * (idx + 1))[x * (idx + 1)] is tree]

    return len(r)


lines = Read.lines_to_list('resources/day3/map.txt', lambda line: line.strip())
tree = '#'

print(f'Answer 1: {get_encounters(3, 1)}')
print(f'Answer 2: {reduce(mul, [get_encounters(d[0], d[1]) for d in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]])}')
