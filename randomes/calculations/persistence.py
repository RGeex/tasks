"""
Напишите функцию, persistence, который принимает положительный параметр num
и возвращает его мультипликативную устойчивость, которая представляет собой
количество раз, которое вы должны умножить цифры в numпока не дойдете до
одной цифры.
"""

from operator import mul
from functools import reduce


def persistence(n: int) -> int:
    c, n = 0, str(n)
    while 1 < len(n):
        c += 1
        n = str(reduce(mul, map(int, n)))
    return c


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (4, 0),
        (25, 2),
        (39, 3),
        (999, 4),
    )
    for key, val in data:
        assert persistence(key) == val


if __name__ == '__main__':
    test()
