"""
Задача:

Напишите функцию, которая принимает целое число nи возвращает сумму
факториалов первого n Числа Фибоначчи.

Примеры:
sum_fib(2)  = 2    # 0! + 1! = 2
sum_fib(3)  = 3    # 0! + 1! + 1! = 3
sum_fib(4)  = 5    # 0! + 1! + 1! + 2! = 5
sum_fib(10) = 295232799039604140898709551821456501251

Ограничения:

    2 ≤ N ≤ 22
"""

import math


def sum_fib(n: int) -> int:
    """
    Вычисляет сумму факториалов N чисел фибоначи.
    """
    r, a, b = 0, 0, 1
    while n:
        r += math.factorial(a)
        a, b = b, a + b
        n -= 1
    return r


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 11),
        (6, 131),
    )
    for key, val in data:
        assert sum_fib(key) == val


if __name__ == '__main__':
    test()