"""
Реализуйте функцию unique_in_order, которая принимает в качестве аргумента
последовательность и возвращает список элементов без каких-либо элементов
с одинаковым значением рядом друг с другом и сохраняет исходный порядок элементов.

Например:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""

from itertools import groupby


def unique_in_order(sequence: str) -> list:
    """
    Удаляет из строки дубликаты символов идущих подряд, сохраняя последовательность.
    """
    return [x for x, _ in groupby(sequence)]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("", []),
        ([], []),
        ((), []),
        ("A", ["A"]),
        ("AA", ["A"]),
        (["A"], ["A"]),
        (("A",), ["A"]),
        ([1, 2, 3, 3, -1], [1, 2, 3, -1]),
        ("ABBCcA", ["A", "B", "C", "c", "A"]),
        (["a", "b", "b", "a"], ["a", "b", "a"]),
        ("AAAABBBCCDAABBB", ["A", "B", "C", "D", "A", "B"]),
    )
    for key, val in data:
        assert unique_in_order(key) == val


if __name__ == '__main__':
    test()
