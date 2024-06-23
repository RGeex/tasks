"""
Напишите функцию, которая определяет, схожи ли переданные последовательности.
Подобное означает, что они содержат одни и те же элементы и одинаковое
количество вхождений элементов.

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 1, 2, 4, 3]
arr3 = [1, 2, 3, 4]
arr4 = [1, 2, 3, "4"]

arrays_similar(arr1, arr2) # Should equal true
arrays_similar(arr2, arr3) # Should equal false
arrays_similar(arr3, arr4) # Should equal false
"""

from typing import Any
from operator import eq
from collections import Counter


def arrays_similar(*seq: list[Any]) -> bool:
    """
    Определяет схожесть, переданных списков.
    """
    return eq(*map(Counter, seq))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1, 2, 2, 3, 4], [2, 1, 2, 4, 3]), True),
        (([2, 1, 2, 4, 3], [1, 2, 2, 3, 4]), True),
        ((['1', 1], [1, '1']), True),
        (([2, 1, 2, 4, 3], [1, 1, 2]), False),
        (([1, 1, 2], [4, 3, 2, 1, 1]), False),
        (([1, 2, 2, 3], [3, 3, 2, 1]), False),
        (([1, 2], ['1', 2]), False),
        ((['1', 1], [1, 1]), False),
    )
    for key, val in data:
        assert arrays_similar(*key) == val


if __name__ == '__main__':
    test()
