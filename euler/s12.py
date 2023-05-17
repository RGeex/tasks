"""
Последовательность треугольных чисел образуется путем сложения натуральных
чисел. К примеру, 7-е треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
Первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим делители первых семи треугольных чисел:

     1: 1
     3: 1, 3
     6: 1, 2, 3, 6
    10: 1, 2, 5, 10
    15: 1, 3, 5, 15
    21: 1, 3, 7, 21
    28: 1, 2, 4, 7, 14, 28

Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более пятисот делителей?
"""

from typing import Generator


def triangle_num() -> Generator:
    """Генератор бесконечной последовательности треугольных чисел."""
    num = 1
    while True:
        num += 1
        yield num * (num - 1) // 2


find = 500


def get_num_triangle_limit_dividers(dividers: int) -> int | None:
    """Поиск треугольного числа с более N делителей."""
    if dividers:
        for num in triangle_num():

            result = 1 if num == 1 else 2
            for i in range(2, int(num ** 0.5)):
                if not num % i:
                    result += 2

            if result > dividers:
                return num

    return None


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert get_num_triangle_limit_dividers(5) == 28
    assert get_num_triangle_limit_dividers(500) == 76576500


if __name__ == '__main__':
    test()
