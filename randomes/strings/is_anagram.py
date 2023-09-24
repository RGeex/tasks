"""
- Определить: можно ли из символов
первой строки, составить вторую.
"""

from functools import reduce
from collections import Counter


def is_bility1(a: str, b: str) -> bool:
    """
    Проверяет, можно ли составить из первой строки вторую,
    используя только данное кол-во каждого символа из первой строки.
    """
    return reduce(lambda a, b: a & b == b, map(Counter, (a, b)))


def is_bility2(a: str, b: str) -> bool:
    """
    Проверяет, можно ли составить из первой строки вторую,
    используя любое кол-во каждого символа из первой строки.
    """
    return reduce(lambda a, b: b <= a, map(set, (a, b)))


def is_bility3(a: str, b: str) -> bool:
    """
    Проверяет, можно ли составить из первой строки вторую,
    используя только данное кол-во каждого символа из первой строки,
    без использования библиотек. Функционально аналогична func1.
    """
    for k, v in count_ident(b).items():
        if not (k := count_ident(a).get(k)) or min(k, v) != v:
            return False
    return True


def count_ident(string: str) -> dict[str, int]:
    """
    Подсчитывает кол-во одинаковых символов в строке.
    """
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    return result


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data_1 = [
        (('abcd', 'dab'), True),
        (('abcd', 'daa'), False),
    ]
    data_2 = [
        (('abcd', 'daa'), True),
        (('abcd', 'dag'), False),
    ]

    for args, value in data_1:
        assert is_bility1(*args) == value
        assert is_bility3(*args) == value

    for args, value in data_2:
        assert is_bility2(*args) == value


if __name__ == '__main__':
    test()
