"""
Число-палиндром с обеих сторон (справа налево и слева направо)
читается одинаково. Самое большое число-палиндром, полученное
умножением двух двузначных чисел – 9009 = 91 x 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""

from functools import reduce


def is_pal(num: int) -> bool:
    """Проверяет, является ли число палиндромом"""
    return (s := str(num)) == s[::-1]


def get_val(N: int) -> tuple:
    """Поиск максимальных N-значных чисел, дающих палиндром при умножении."""
    a, b = 0, 0
    maxx, minx = int('9' * N), int('9' + '0' * (N - 1))
    for i in range(maxx, minx, -1):
        if i * i < a * b:
            break
        for j in range(i, minx, -1):
            if is_pal(i * j):
                break
        if i * j > a * b:
            a, b = i, j
    return a, b


def func(*args) -> int:
    """Поиск самого большого палиндрома N-значных чисел."""
    return reduce(lambda a, b: a * b, get_val(*args))


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert get_val(2) == (99, 91)
    assert func(2) == 9009
    assert get_val(3) == (993, 913)
    assert func(3) == 906609


if __name__ == '__main__':
    test()
