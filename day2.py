from typing import Callable

from util.reader import Read


def count(items: list, fn: Callable) -> int:
    return len([i for i in items if is_valid(i, fn)])


def is_valid(val: list, fn: Callable) -> bool:
    return fn(tuple([int(r) for r in val[0].split('-')]), val[1][0], val[2])


def test1(bounds, letter, password) -> bool:
    return password.count(letter) in range(bounds[0], bounds[1] + 1)


def test2(bounds, letter, password) -> bool:
    return (password[bounds[0] - 1] == letter) is not (password[bounds[1] - 1] == letter)


entries = Read.lines_to_list('resources/day2/passwords.txt', lambda line: line.split())

print(f'Answer 1: {count(entries, test1)}')
print(f'Answer 2: {count(entries, test2)}')
