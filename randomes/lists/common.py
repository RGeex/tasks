"""
Учитывая три массива целых чисел, верните сумму элементов,
которые являются общими во всех трех массивах. 
"""


from functools import reduce
from collections import Counter


def common(*args: list) -> int:
    """
    Поиск суммы одинаковых элементов спиков.
    """
    return sum(reduce(lambda a, b: a & b, map(Counter, args)).elements())


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1, 2, 3], [5, 3, 2], [7, 3, 2]), 5),
        (([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]), 7),
        (([1], [1], [1]), 1),
        (([1], [1], [2]), 0),
    )
    for key, val in data:
        assert common(*key) == val


if __name__ == '__main__':
    test()
