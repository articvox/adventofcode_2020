from itertools import combinations
from util.reader import Read
from functools import reduce
from operator import mul


def get_combinations(items: list, target: int, n: int) -> list:
    return [a for b in [c for c in combinations(items, n) if sum(c) == target] for a in b]


numbers = Read.lines_to_list('resources/day1/numbers.txt', lambda line: int(line))

print(f'Answer 1: {reduce(mul, get_combinations(numbers, 2020, 2))}')
print(f'Answer 2: {reduce(mul, get_combinations(numbers, 2020, 3))}')
